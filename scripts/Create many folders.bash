NUMFOLDERS=31

for ((x=1;x< = $NUMFOLDERS;x+=1)); do mkdir `printf "%02d" $x`; done

