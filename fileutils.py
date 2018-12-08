
# File utility functions for every day Python scripts

import os
import csv
import sys
import shutil
import tempfile


def match_suffix(suffix, start = None):
	'''
	Find all files with a specific file ending,
	starting at the `start` file location (generator).
	'''
	if start is None:
		start = os.path.abspath(os.getcwd())

	assert os.path.exists(start), 'Error -' \
		' specified path does not exist...'

	for root, subdirs, files in os.walk(start):
		for f in files:
			if f.endswith(suffix):
				yield os.path.join(root, f)



def match_prefix(prefix, start = None):
	'''
	Find all files that begin with a specific
	string sequence, starting at the `start`
	file location (generator).
	'''
	if start is None:
		start = os.path.abspath(os.getcwd())

	assert os.path.exists(start), 'Error -' \
		' specified path does not exist...'

	for root, subdirs, files in os.walk(start):
		for f in files:
			if f.startswith(prefix):
				yield os.path.join(root, f)



class Tempdir:

	__instance = None
	_tempfolder = None

	def __init__(self):
		if __class__.__instance is not None:
			raise Exception('Error - There can only be one '\
				'instance; call .getInstance() method.')
		else:
			__class__.__instance = self

	@staticmethod
	def getInstance():
		if __class__.__instance is None:
			__class__()
		return __class__.__instance

	def fetch(self):
		if self._tempfolder is None:
			self._tempfolder = self._create_new()
		return self._tempfolder

	def clear(self):
		if not os.listdir(self._tempfolder):
			return self._tempfolder
		elif self._tempfolder is None or not os.path.exists(self._tempfolder):
			self._tempfolder = self._create_new()
			return self._tempfolder
		for root, subdirs, files in os.walk(self._tempfolder):
			for f in files:
				os.unlink(os.path.join(root, f))
			for d in subdirs:
				shutil.rmtree(os.path.join(root, d), ignore_errors = True)

		assert not os.listdir(self._tempfolder), 'Error - temporary directory' \
			' has not been cleared: {}'.format(self._tempfolder)

		return self._tempfolder

	def delete(self):
		if self._tempfolder is not None and os.path.exists(self._tempfolder):
			shutil.rmtree(self._tempfolder, ignore_errors = True)

		assert not os.path.exists(self._tempfolder), 'Error - temporary directory' \
			' has not been deleted: {}'.format(self._tempfolder)

		self._tempfolder = None
		return

	def _create_new(self):
		return os.path.exists(tempfile.mkdtemp())



