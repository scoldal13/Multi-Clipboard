# this is a multiboard clip board
# usage:
#       py.exe m.pyw save <keyword> - saves whatever is on the clipboard to the shelve file
#       py.exe m.pyw <keyword> - loads that clip to the clipboard for pasting
#       py.exe m.pyw list - loads all keywords to the clipboard for reference
#       py.exe m.pyw delete <keyword> - deletes that specific bit of data
#       py.exe m.pyw deleteA - deletes all the keywords

import shelve, pyperclip, sys, os

#function to remove the shelve file data
def remove_files():
    mShelf.close()
    
    if os.path.exists("m.dir") :
        os.remove("m.bak")
        os.remove("m.dir")
        os.remove("m.dat")
    else :
        print("the files do not exist")
        
mShelf = shelve.open('m')


#save clipboard content
if len(sys.argv) == 3 and sys.argv[1] == 'save' :
    mShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2 :
    if sys.argv[1].lower() == 'list' :
        pyperclip.copy(str(list(mShelf.keys())))
    elif sys.argv[1] in mShelf :
        pyperclip.copy(mShelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'deletea':
        remove_files()
elif len(sys.argv) == 3 and sys.argv[1] == 'delete' :
    if sys.argv[2] in mShelf :
        del mShelf[sys.argv[2]]

#close shelve file 
mShelf.close()
