Basic file synchronisation for Sublime Text 2
=============================================

what it does
------------
whenever a file in the project path is saved it will be synced to the file sync path

how to use it
-------------

install the plugin as per any plugin.

in your settings file add project_path and file_sync_path entries.

I use the project specific xxx.sublime-project file, which looks something like:

```json
	"settings": {
		"project_path": "/Users/njs50/Documents/workspaces/ruby/xxx",
		"file_sync_path": "/Volumes/ubuntu_apps/xxx"
	}
```

what is should do but doesn't
-----------------------------

* check that the paths are defined in your settings
* take an array of paths to check/sync so you can set up multiple projects in a global config
* have the ability to toggle on and off
* have a sync all functionality (perhaps some option to invoke rsync)

when will these features be added
---------------------------------
probably only when I actually need them (which may be never)!