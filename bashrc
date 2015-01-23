alias cp="cp -i"
alias rm="rm -i"
alias mv="mv -i"

export PS1="\[\e[33m\](\h) [\W]\[\e[0m\] \[\e[1;32m\]!\! %\[\e[0m\] "

alias ls='ls -F --color'
alias sl='ls -F --color'
alias l='ls -FA --color'
alias ll='ls -lhGAtc --color'
alias dir='ls -FA --color'
alias d='tree -dLl 1'
alias d2='tree -dLl 2'
alias d3='tree -dLl 3'
alias dd='clear && ls -F --color */'
alias wipe='history -w && history -c'

function cd {
    builtin cd "$@" && ls -pFLa --color | grep -v / | tr "\n" "\t" && echo ""
}

#Servers
alias irc="ssh -tA shell.onid.oregonstate.edu screen -dr"
alias milo="ssh -tA milo.nws.oregonstate.edu"
alias onid="ssh -tA shell.onid.oregonstate.edu"
alias engr="ssh -tA access.engr.oregonstate.edu"
alias os-class="ssh -tA access.engr.oregonstate.edu ssh os-class"


#stty erase #For Oregon State Engr servers 

if [ $(hostname -s) == "os-class" ] #CS 344
    then
        cd ~/cs344
fi

#History Optimization
shopt -s histappend
HISTFILESIZE=10000000
HISTSIZE=1000000
HISTCONTROL=ignorespace
HISTIGNORE='ls:history:cd *:dir:l:ll:d:d2:d3:dd:clear:ls *: dir *'
HISTTIMEFORMAT='%F %T '
PROMPT_COMMAND='history -a'
shopt -s cmdhist
alias wipe='history -w && history -c'