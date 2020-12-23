"""
Replicated command: touch

Create a new empty file if file does not exist.
If it exists update access and modification times.
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
	file_path = arguments.file_path
	touch(file_path)

def setup_argument_parser():
	"""
	Setup argument parser with required arguments and their properties.
	"""
	parser = argparse.ArgumentParser(
		description = "Create a new file if it does not exist and update access and modification time if does."
	)
	parser.add_argument(
		"file_path",
		help = "The name of the file to be created, or get it's time updated."
	)
	return parser

def touch(file_path):
	"""
	Create file if it does not exist. Update access and modification time if it
	does.
	"""
	if fu.does_file_exist(file_path):
		os.utime(file_path)
	else:
		with open(file_path, "w") as _:
			# Just create an empty file.
			pass

if __name__ == "__main__":
	main()
