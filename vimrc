"Enable Mouse Support, Line Numbers, and Turn on Spellchecking
"Also see http://amix.dk/vim/vimrc.html or https://github.com/amix/vimrc
set number
set mouse=a
set spell
"Makes better tab complete
set wildmenu
"Always show the position in document
set ruler
set cmdheight=2
set hid
"Search Optimization
set smartcase
set hlsearch
""Turns of sounds and flashes
set noerrorbells
set novisualbell
set tm=500
"Make sure syntax highlighter is on
syntax enable
set smarttab
"Wrap Long Lines Instead of Hide
set wrap
set statusline=\ %{HasPaste()}%F%m%r%h\ %w\ \ CWD:\ %r%{getcwd()}%h\ \ \ Line:\ %l 
"These Lines change the format of misspelt words to an underline
hi clear SpellBad
hi SpellBad cterm=underline
""Enables Supper Awesome Copy and Paste
vmap <C-c> "+yi
vmap <C-x> "+c
vmap <C-v> c<ESC>"+p
imap <C-v> <C-r><C-o>+
"Moves Number Line to the Left
set numberwidth=1
""Hypothetically Allows Save if you forgot to sudo vim
"type the command :w!! to use
"cmap w!! w !sudo tee > /dev/null %
"If you are in a python, c, or Cpp document pressing F5 will save, compile, and run your code (with correct conventions)
autocmd filetype python nnoremap <F5> :w <bar> exec '!python '.shellescape('%')<CR>
autocmd filetype c nnoremap <F5> :w <bar> exec '!gcc '.shellescape('%').' -o '.shellescape('%:r').' && ./'.shellescape('%:r')<CR>
autocmd filetype cpp nnoremap <F5> :w <bar> exec '!g++ '.shellescape('%').' -o '.shellescape('%:r').' && ./'.shellescape('%:r')<CR>
set smartindent
set tabstop=4
set shiftwidth=4
set expandtab

