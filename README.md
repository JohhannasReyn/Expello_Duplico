Expelloduplico
==============

This package adds a simple feature to Sublime Text that allows you to quickly select or remove duplicates.

It's home is here on [GitHub](https://github.com/JohhannasReyn/Expelloduplico/).

Features
---
  - Easily select duplicate values
  - Easily remove duplicate values
  - Works for any kind of file
  - Delimiters are automatically detected
  - If needed delimiter can be specified in this packages settings.

Installation Options
---
  - (Hopefully this will be available soon from within Sublime Text's Package Control)
  - In the meantime, download this zipped folder, save it with the extension "*.sublime-package"
    (i.e. "Expelloduplico.sublime-package") in your "Sublime Text/Installed Packages" directory.
    (On Windows this is usually "C://Users/<UserName>/AppData/Roaming/Sublime Text/Installed Packages/")
    If Sublime Text is already open and you don't see it listed under menu,
    "Preferences -> Package Settings", restart Sublime Text.

Usage Options
---
  - Right click on the ducument or selected text and select 
    "Select or Remove Duplicates (Expelloduplico)"
  - With the desired target being the entire document, select
    from the menu under, 'Edit' -> 'Select or Remove Duplicates'
  - If only a portion of the document is the desired target, 
    select the text to target and either right click the selection,
    or from the menu bar, under 'Edit', click 
    "Select or Remove Duplicates" to run this plugin.
  - If you have enabled the suggested key bindings for this 
    package, then simply use "Ctrl+Shift+U" to invoke this plugin.
  
Configuration
---
  - Options can be configured in Expelloduplico.sublime-settings
    To access: *Preferences -> Package Settings -> Expelloduplico*
  - For more information reguarding the variables found in 'Settings'
    see the install.txt file found in this packages folder, or in the 
    settings file itself.

License & Contributing
---
 - [MIT license](LICENSE)
