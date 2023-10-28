#Xbox Video Chat Patcher

import os
import sys
import shutil

version = 'v1.0'

xbe_magic = b'\x58\x42\x45\x48'
xbe_signature = b'\x08\xCE\x66\x4B\x21\x78\x1A\xC2\x65\x94\x19\x22\x83\xCE\x2B\xDF'
patch = b'\x00\x66\x81\x7C\x24\x1C\x4C\x05\x0F\x85\xCA\x01\x00\x00\x66\x81\x7C\x24\x1E\x55\x01'


def patch_xbe(file):
    #Open the file
    with open (file, 'r+b') as f:
    
        #Check if the file is an xbe
        if not xbe_magic in f.read(4):
            print("The file does not appear to be an xbe")
            sys.exit(1)

        #Verify that it's Xbox Video Chat
        print("Verifying xbe...")
        if not xbe_signature in f.read(16):
            print("This doesn't appear to be an xbe for Xbox Video Chat")
            sys.exit(1)

        #Check if the xbe has already been patched
        f.seek(0x1AC3F0)
        patch_offset = f.tell()
        if patch in f.read(21):
            print("The xbe has already been patched")
            sys.exit(1)

        #Create a backup
        print("Backing up...")
        shutil.copy2(file, (file)+".bak")

        #Patch the xbe
        print("Patching...")
        f.seek(patch_offset)
        f.write(patch)
        print("The xbe has been patched!")
        
       
def main():
    print("==================================")
    print("== Xbox Video Chat Patcher %s ==" % version)
    print("==================================\r\n")
    
    #Check if the tool is running as an exe
    if getattr(sys, 'frozen', False):
        extension = 'exe'
    else:
        extension = 'py'

    #Get file input
    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        print("Usage: xboxvideochatpatcher.%s default.xbe" % extension)
        sys.exit()
    
    #Check if the file exists
    if not os.path.exists(file):
        print("File not found")
        sys.exit(1)
    
    patch_xbe(file)


if __name__ == '__main__':
    main()