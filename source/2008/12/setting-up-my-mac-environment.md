---
title: 'setting up my mac environment'
date: '2008-12-31T08:13:27-08:00'
status: draft
id: 573
category: general
---
vimfiles go into ~/.vim (this is different from gvim on windows where I had them in $VIMRUNTIME/vimfiles)

tobin:~ brandon$ defaults write com.apple.finder AppleShowAllFiles TRUE  
tobin:~ brandon$ killall Finder

via [devnulled](http://devnulled.com/content/2007/08/how-to-show-hidden-and-protected-files-in-os-x-finder/)

add to vimrc:  
filetype plugin on  
in .vim/ftplugins  
lzx.vim  
[xml.vim](http://www.vim.org/scripts/script.php?script_id=301)

debugging tips:  
– when errors are displayed too quickly on startup  
:messages  
will show a list of recent messages

to find out what filetype vim thinks is in the current buffer  
:set filetype