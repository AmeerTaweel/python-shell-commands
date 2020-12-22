"""
Replicated command: cp

Copy files and/or directories to another or directory.
"""

import argparse
import os
from utils import file_utils as fu
from mkdir import make_dir

def main():
	"""
	Parse and handle user's call.
	"""
	parser = setup_argument_parser()
	arguments = parser.parse_args()
	sources, destination = (arguments.sources, arguments.destination)

	files_count = 0
	dirs_count = 0
	for source in sources:
		if fu.does_file_exist(source):
			files_count += 1
			copy_file(source, destination)
		elif fu.does_dir_exist(source):
			dirs_count += 1
			copy_dir(source, destination)

	print(f"Copied {files_count} files and {dirs_count} directories.")

def setup_argument_parser():
	"""
	Setup argument parser with required arguments and their properties.
	"""
	parser = argparse.ArgumentParser(
		description="Copy files and/or directories to another or directory."
	)
	parser.add_argument(
		"sources",
		nargs="+",
		help="The file/s or directory/ies to be copied."
	)
	parser.add_argument(
		"destination",
		help="The directory to copy to."
	)
	return parser

def copy_file(src, dest):
	"""
	Copy the file from src to dest.
	"""
	if not fu.does_file_exist(src):
		print(f"File {src} does not exist.")
		return

	make_dir(dest)

	dest_file = fu.nested_path(dest, fu.basename(src))

	if fu.does_file_exist(dest_file):
		can_override = ask_user_permission(
			f"File {src} already exists in {dest}, override?"
		)
		if not can_override:
			print(f"File {dest_file} was not overridden.")
			return
		os.remove(dest_file)
		print(f"File {dest_file} was overridden.")

	with open(src, "r") as file, open(dest_file, "a") as copy:
		# Copying the file at once can cause memory problems on large files.
		for line in file:
			copy.write(line)

def copy_dir(src, dest):
	"""
	Copy the dir from src to dest.
	"""
	if not fu.does_dir_exist(src):
		print(f"Directory {src} does not exist.")
		return

	make_dir(dest)

	dest_dir = fu.nested_path(dest, fu.basename(src))

	if fu.does_dir_exist(dest_dir):
		can_override = ask_user_permission(
			f"Directory {src} already exists in {dest}, override?"
		)
		if not can_override:
			print(f"Directory {dest_dir} was not override D.")
			return
		os.rmdir(dest_dir)
		print(f"Directory {dest_dir} was override D.")

	make_dir(dest_dir)
	with os.scandir(src) as dir_entries:
		for entry in dir_entries:
			if entry.is_file():
				copy_file(entry.path, dest_dir)
			elif entry.is_dir():
				copy_dir(entry.path, dest_dir)

def ask_user_permission(question, default_to_no=True):
	"""
	Ask question to user and return True if he agrees, and False if he does not.
	"""
	yes = ["yes", "y"]
	no = ["no", "n"]
	answer = input(f"{question} ({'N/y' if default_to_no else 'Y/n'}) >>> ")
	if default_to_no:
		return answer.lower() in yes
	return answer.lower() not in no

if __name__ == "__main__":
	main()
