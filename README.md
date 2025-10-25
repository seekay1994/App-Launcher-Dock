# App-Launcher-Dock
App Launcher Dock for Wallpaper Engine

All source files for the App Launcher Dock, including build files for the setup.exe.

The setup is a python-script which was compiled into an EXE by PyInstaller. 
It will check if a folder called "materials" and a file called "project.json" extst in it´s directory. If so then it´s reasonable to assume that it´s located in a WPE project folder.
It will then create a backup of your project.json, merge the user properties needed for the App Launcher Dock and copy the texture files into the material folder.
