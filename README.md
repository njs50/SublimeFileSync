Basic file synchronisation for Sublime Text 2
=============================================

what it does
------------
whenever a file in the project path is saved it will be synced to the file sync path

how to use it
-------------

install the plugin as per any plugin.

in your settings file add a filesync array of project_path and file_sync_path entries.

I use the project specific xxx.sublime-project file, which looks something like:

```json
	"settings": {
		"filesync": [
			{
				"source": "/Users/njs50/Documents/workspaces/ruby/leaseManager",
				"destination": "/Volumes/ubuntu_apps/leaseManager"
			}
		]		
	}
```

you can have multiple source/destination pairs in the array. 

what is should do but doesn't
-----------------------------

* have the ability to toggle on and off
* have a sync all functionality (perhaps some option to invoke rsync)
* check that the pathes are valid

when will these features be added
---------------------------------
probably only when I actually need them or when someone else writes them for me (hint hint)!