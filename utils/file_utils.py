"""
Utilities for dealing with files and directories.
"""

import os


def does_file_exist(path):
	"""
	Return True if a file with the given path exists.
	Return False otherwise.
	"""
	return os.path.exists(path) and os.path.isfile(path)


def does_dir_exist(path):
	"""
	Return True if a directory with the given path exists.
	Return False otherwise.
	"""
	return os.path.exists(path) and os.path.isdir(path)


def nested_path(directory, nested_entry):
	"""
	Return path for nested_entry which is inside directory.
	In the form directory/nested_entry
	"""
	return os.path.normpath(f"{directory}/{nested_entry}")


def basename(path):
	"""
	Return the name for the most nested entry in a path.
	Works for both files and directoris.
	"""
	return os.path.basename(path.rstrip("/"))
