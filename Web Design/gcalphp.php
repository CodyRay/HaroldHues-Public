<?php
//https://github.com/media-uk/GCalPHP

/////////
//Configuration
//

// Your private feed - which you get by right-clicking the 'xml' button in the 'Private Address' section of 'Calendar Details'.
if (!isset($calendarfeed)) {$calendarfeed = "http://www.google.com/calendar/feeds/oregonstate.edu_ft4hid43m06o242cvj4dtpv0ec%40group.calendar.google.com/public/basic"; }

// Date format you want your details to appear
$dateformat="F j Y";
$timeformat="g:ia";

// The timezone that your user/venue is in (i.e. the time you're entering stuff in Google Calendar.) http://www.php.net/manual/en/timezones.php has a full list
date_default_timezone_set('America/Los_Angeles');

// How you want each thing to display.
// By default, this contains all the bits you can grab. You can put ###DATE### in here too if you want to, and disable the 'group by date' below.
$event_display="<P><B>###TITLE###</b> - from ###FROM### ###DATESTART### until ###UNTIL### ###DATEEND### (<a href='###LINK###' target='_blank'>add this</a>)<BR>###WHERE### (<a href='###MAPLINK###' target='_blank'>map</a>)<br>###DESCRIPTION###</p>";
$all_day_catch="from   until   ";
$all_day_text="all day ";

// What happens if there's nothing to display
$event_error="<P>There are no events to display.</p>";

// The separate date header is here
$event_dateheader="<P><B>###DATE###</b></P>";
$GroupByDate=true;
// Change the above to 'false' if you don't want to group this by dates.

// ...and how many you want to display (leave at 999 for everything)
$items_to_show=10;

// And finally, change this to 'true' to see lots of fancy debug code
$debug_mode=false;

//
//End of configuration block
/////////

if ($debug_mode) {error_reporting (E_ALL); ini_set('display_errors', 1);
ini_set('error_reporting', E_ALL); echo "<P>Debug mode is on. Hello there.<BR>Your server thinks the time is ".date(DATE_RFC822)."</p>";}

// Form the XML address.
$calendar_xml_address = str_replace("/basic","/full?singleevents=true&futureevents=true&max-results".$items_to_show."&orderby=starttime&sortorder=a",$calendarfeed); //This goes and gets future events in your feed.

if ($debug_mode) {
echo "<P>We're going to go and grab <a href='$calendar_xml_address'>this feed</a>.<P>";}

$xml = simplexml_load_file($calendar_xml_address);


if ($debug_mode) {echo "<P>Successfully got the GCal feed.</p>";}

$items_shown=0;
$old_date="";
$xml->asXML();

foreach ($xml->entry as $entry){
	$ns_gd = $entry->children('http://schemas.google.com/g/2005');
	//Do some niceness to the description
	//Make any URLs used in the description clickable
	$description = preg_replace('"\b(https://\S+)"', '<a href="$1" target="_blank">$1</a>', $entry->content);
	$description = preg_replace('"\b(http://\S+)"', '<a href="$1" target="_blank">$1</a>', $description);
	
	// Make email addresses in the description clickable
	$description = preg_replace("`([-_a-z0-9]+(\.[-_a-z0-9]+)*@[-a-z0-9]+(\.[-a-z0-9]+)*\.[a-z]{2,6})`i","<a href=\"mailto:\\1\" title=\"mailto:\\1\">\\1</a>", $description);

	if ($debug_mode) { echo "<P>Here's the next item's start time... GCal says ".$ns_gd->when->attributes()->startTime." PHP says ".date("g.ia  -Z",strtotime($ns_gd->when->attributes()->startTime))."</p>"; }
    //Original Script Needed Better Support for Multi-Day Events if the length is long there is a time in there so it is ok to do it the way it origonally was
    if (strlen($ns_gd->when->attributes()->startTime) > 10) {
        // These are the dates we'll display
        $gCalDate = date($dateformat, strtotime($ns_gd->when->attributes()->startTime));
        $gCalDateStart = date($dateformat, strtotime($ns_gd->when->attributes()->startTime));
        $gCalDateEnd = date($dateformat, strtotime($ns_gd->when->attributes()->endTime));
        $gCalStartTime = date($timeformat, strtotime($ns_gd->when->attributes()->startTime));
        $gCalEndTime = date($timeformat, strtotime($ns_gd->when->attributes()->endTime));
    }
    //On the otherhand this formats it better for multiday events
    else {
        // These are the dates we'll display
        $gCalDate = date($dateformat, strtotime($ns_gd->when->attributes()->startTime));
        $gCalDateStart = date($dateformat, strtotime($ns_gd->when->attributes()->startTime));
        $gCalDateEnd = date($dateformat, strtotime($ns_gd->when->attributes()->endTime ) - 1);//Day is allways one to big go back a day
        $gCalStartTime = "";
        $gCalEndTime = "";
    }

                   
	// Now, let's run it through some str_replaces, and store it with the date for easy sorting later
	$temp_event=$event_display;
	$temp_dateheader=$event_dateheader;
	$temp_event=str_replace("###TITLE###",$entry->title,$temp_event);
	$temp_event=str_replace("###DESCRIPTION###",$description,$temp_event);


	if ($gCalDateStart!=$gCalDateEnd) {
	//This starts and ends on a different date, so show the dates
	$temp_event=str_replace("###DATESTART###",$gCalDateStart,$temp_event);
	$temp_event=str_replace("###DATEEND###",$gCalDateEnd,$temp_event);
	} else {
	$temp_event=str_replace("###DATESTART###",'',$temp_event);
	$temp_event=str_replace("###DATEEND###",'',$temp_event);
	}

	$temp_event=str_replace("###DATE###",$gCalDate,$temp_event);
	$temp_dateheader=str_replace("###DATE###",$gCalDate,$temp_dateheader);
	$temp_event=str_replace("###FROM###",$gCalStartTime,$temp_event);
	$temp_event=str_replace("###UNTIL###",$gCalEndTime,$temp_event);
	$temp_event=str_replace("###WHERE###",$ns_gd->where->attributes()->valueString,$temp_event);
	$temp_event=str_replace("###LINK###",$entry->link->attributes()->href,$temp_event);
	$temp_event=str_replace("###MAPLINK###","http://maps.google.com/?q=".urlencode($ns_gd->where->attributes()->valueString),$temp_event);
	// Replaces the from and untill and replaces it with something different for all day
	$temp_event=str_replace($all_day_catch,$all_day_text,$temp_event);
	// Accept and translate HTML
	$temp_event=str_replace("&lt;","<",$temp_event);
	$temp_event=str_replace("&gt;",">",$temp_event);
	$temp_event=str_replace("&quot;","\"",$temp_event);
                   
	if (($items_to_show>0 AND $items_shown<$items_to_show)) {
                if ($GroupByDate) {if ($gCalDate!=$old_date) { echo $temp_dateheader; $old_date=$gCalDate;}}
		echo $temp_event;
		$items_shown++;
	}
}

if (!$items_shown) { echo $event_error; }

