import sublime, sublime_plugin, shutil, functools

class FileSyncBuild( sublime_plugin.EventListener ):

	def on_post_save( self, view ):

		settings = view.settings().get('filesync')

		if settings is not None:

			for stSync in settings:

				pp = stSync.get('source')
				sp = stSync.get('destination')
				fn = view.file_name()
				bSync = 0

				if (pp in fn):
					dest = fn.replace(pp,sp)
					shutil.copy2(fn,dest)
					bSync = 1
					self.updateStatus( 'Sync: ' + fn + ' -> ' + dest )

			if bSync == 0:
				self.updateStatus('file not in sync path')

		else:
			self.updateStatus('filesync not configured in settings')




	# delayed update to status text to prevent overwriting by saved message
	def updateStatus(self, text):
		sublime.set_timeout(functools.partial(sublime.status_message, text), 1000)


