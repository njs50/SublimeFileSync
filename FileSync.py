import sublime, sublime_plugin, shutil

class FileSyncBuild( sublime_plugin.EventListener ):

	def on_post_save( self, view ):
		s = view.settings()

		pp = s.get('project_path')
		sp = s.get('file_sync_path')
		fn = view.file_name()

		if (pp in fn):
			dest = fn.replace(pp,sp)
			shutil.copy2(fn,dest)