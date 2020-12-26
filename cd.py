"""
Replicated command: cd

Change current working directory.
"""

import argparse
import os
from utils import file_utils as fu

def main():
	"""
	Parse and handle user's call.
	"""
	parser = setup_argument_parser()
	arguments = parser.parse_args()
	dir_path = arguments.dir_path
	change_dir(dir_path)

def setup_argument_parser():
	"""
	Setup argument parser with required arguments and their properties.
	"""
	parser = argparse.ArgumentParser(
			description = "Change current working directory."
	)
	parser.add_argument(
		"dir_path",
		help = "The path to the directory to go to."
	)
	return parser

def change_dir(dir_path):
	"""
	Change current working directory.

	Does not change the current working directory for the parent process.
	"""
	if not fu.does_dir_exist(dir_path):
		print(f"Directory ${dir_path} does not exist.")
		return
	full_path = fu.nested_path(os.getcwd(), dir_path)
	os.chdir(full_path)

if __name__ == "__main__":
	main()
