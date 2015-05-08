# similar-file-names is a script which will search for files named similarly to other files in the same folders. #
## This can be used, for example, to quickly search for duplicate files in your music or document collection. ##

To use in Windows, you will need to install Python 3 (not 2).
I suggest ActivePython: www.activestate.com/activepython/downloads

Linux and similar likely already has Python installed.

To use:
1) Download and similar-file-names.py with Notepad or your favorite editor.

2) You will see the following near the top:
{{{searchPaths = ['c:\itunes', 'c:\music']
fileExtensions = ['**.m4p', '**.mp3', '**.flac']}}}**

`searchPaths` is a list of paths on your computer to search within.
`fileExtensions` is a list of... file extensions to search.

Change the search paths and file extenions. For example, if you want to find duplicate songs in c:\mymedia and c:\mymusic, then change searchPaths to:
`searchPaths = ['c:\mymedia', 'c:\mymusic']`

If you want to search for documents instead of music, change searchPaths to your documents directory (e.g. `C:\Users\charles` ) then change fileExtensions to something like:
`fileExtensions = ['*.doc', '*.docx', '*.txt'] `

You can search as many directories and extensions as you like; just use the format shown in the file, e.g. `['path1', 'path2']`

If you want to search ALL files in the specified paths, just use '**':
`fileExtensions = ['*']`**

3) Save the file and run it. If Windows asks you what to use to run the program, select "Python".