alias cp="cp -i"
alias rm="rm -i"
alias mv="mv -i"

export PS1="\[\e[94m\][\h] \[\e[33m\](\W)\[\e[1;32m\] %\[\e[0m\] "
export EDITOR="/usr/bin/vim"
set -o vi
alias yum='sudo yum'
alias vi='vim'
alias ls='ls -FAh --color --group-directories-first'
alias sl='ls -FAh --color --group-directories-first'
alias l='ls -FAh --color --group-directories-first'
alias ll='ls -lhGAtc --color --group-directories-first'
alias dir=''
alias forest='tree -C | less -R'
alias d='tree -dLl 1'
alias d2='tree -dLl 2'
alias d3='tree -dLl 3'
alias dd='clear && ls -FAh --color --group-directories-first */'
alias wipe='history -w && history -c'

function cd {
    builtin cd "$@" && ls -FAh --color --group-directories-first
}

function mkdircd {
    mkdir "$@" && cd "$@"
}

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
HISTIGNORE='ls:history:dir:l:ll:d:d2:d3:dd:clear:ls *: dir *'
PROMPT_COMMAND='history -a'
shopt -s cmdhist
alias wipe='history -w && history -c'
