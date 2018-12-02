
# File utility functions for every day Python scripts

import os
import csv
import sys
import shutil


def files_with_suffix(suffix, start = None):
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



def files_with_prefix(prefix, start = None):
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




tempdir = None

def create_tempdir():
	'''
	Creates a temporary directory for processing
	files outside of main workspace. Maintain one
	and only one temporary folder at all times. 
	'''
	global tempdir
	tempdir = os.path.abspath(tempfile.mkdtemp())
	return tempdir


def get_tempdir():
	'''
	Fetches the temporary directory. Automatically
	create a new temp directory if it doesn't exist
	or is inaccessible.
	'''
	global tempdir
	if tempdir is None or not os.path.exists(tempdir):
		tempdir = os.path.abspath(tempfile.mkdtemp())
	return tempdir


def clean_tempdir():
	'''
	Wipes all contents inside the current temp directory.
	Will not delete the actual folder itself; returns
	empty temp directory.
	'''
	global tempdir
	if not os.listdir(tempdir):
		return tempdir
	elif tempdir is None or not os.path.exists(tempdir):
		tempdir = os.path.abspath(tempfile.mkdtemp())
		return tempdir
	for root, subdirs, files in os.walk(tempdir):
		for f in files:
			os.unlink(os.path.join(root, f))
		for d in subdirs:
			shutil.rmtree(os.path.join(root, d), ignore_errors = True)
	return tempdir


def delete_tempdir(force = True):
	'''
	Completely destroys the temp directory (including
	the folder itself).
	'''
	global tempdir
	shutil.rmtree(tempdir, ignore_errors = force)
	tempdir = None
	return



