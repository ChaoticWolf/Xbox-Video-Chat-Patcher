# Xbox Video Chat Patcher
A tool that patches the Original Xbox Video Chat software to allow it to be used with a PS2 EyeToy camera.

The Xbox camera that comes bundled with the software is somewhat expensive and rare to find as it was exclusive to Japan. With the software patched, you can use an EyeToy camera with a modification using the ConsoleMods guide [here](https://consolemods.org/wiki/Xbox:EyeToy_Mod_Guide).

Only the Namtai models of the camera will work. The Logitech models do not work. It's unknown if Chicony models work, though they are more rare.

## Using the tool
Python 2.6 or newer needs to be installed. You can download it [here](https://www.python.org/).

If you're using Windows, you can download the exe from the releases. Python does not need to be installed to use it.

Place the patcher and the Xbox Video Chat xbe in the same directory. From the command line (Command Prompt in Windows, Terminal in Mac and Linux) running in the same directory, type in the following to patch it:

    xboxvideochatpatcher.py default.xbe
	
If you're using the exe, you would type in:

    xboxvideochatpatcher.exe default.xbe
	
You can also drag the xbe onto the tool to patch it.

Once the xbe has been patched, you can use the modified PS2 EyeToy with the software.

## Credits
[Ryzee119](https://github.com/Ryzee119) and [Libby](https://github.com/libbers) - Device ID patch

[Harcroft](https://github.com/OGXHarcroft) - ConsoleMods guide

[Insignia](https://insignia.live) - Xbox Live server
