sudo apt-add-repository ppa:ehoover/compholio &&
sudo apt-add-repository ppa:mqchael/pipelight &&
sudo apt-get update &&
sudo apt-get install pipelight-multi &&
sudo pipelight-plugin --enable silverlight &&
sudo pipelight-plugin --enable flash &&
firefox "https://addons.mozilla.org/en-US/firefox/addon/user-agent-overrider"
