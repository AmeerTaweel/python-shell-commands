"""
Replicated command: mkdir

Create a new empty directory.
Does not return an error if the directory exists.
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
	dir_name = arguments.dir_name
	make_dir(dir_name)

def setup_argument_parser():
	"""
	Setup argument parser with required arguments and their properties.
	"""
	parser = argparse.ArgumentParser(
		description = "Create a new empty directory."
	)
	parser.add_argument(
		"dir_name",
		help = "The name of the directory to be created."
	)
	return parser

def make_dir(path):
	"""
	Create directory if it does not exist. Do nothing otherwise.
	"""
	if not fu.does_dir_exist(path):
		os.mkdir(path)

if __name__ == "__main__":
	main()
