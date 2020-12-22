"""
Replicated command: cat

Print the contents of a file to the output stream.
"""

import argparse
from utils import file_utils as fu
from echo import echo


def main():
	"""
	Parse and handle user's call.
	"""
	parser = setup_argument_parser()
	arguments = parser.parse_args()
	file_path = arguments.file_path
	cat(file_path)


def setup_argument_parser():
	"""
	Setup argument parser wtih required arguments and their properties.
	"""
	parser = argparse.ArgumentParser(
		description="Print the file's content to the output stream."
	)
	parser.add_argument(
		"file_path",
		help="The path for the file to print its content to the output stream."
	)
	return parser


def cat(file_path):
	"""
	Print file's content to the output stream.
	"""
	if not fu.does_file_exist(file_path):
		print(f"File {file_path} does not exist.")
		return
	with open(file_path, "r") as file:
		for line in file:
			echo(line, end="")


if __name__ == "__main__":
	main()
