"""
Replicated command: pwd

Print the current working directory.
"""

import argparse
import os

def main():
	"""
	Parse and handle user's call.
	"""
	parser = setup_argument_parser()
	# There should be no arguments
	arguments = parser.parse_args()
	print_working_dir()

def setup_argument_parser():
	"""
	Setup argument parser with required arguments and their properties.
	"""
	parser = argparse.ArgumentParser(
		description = "Print the current working directory."
	)
	return parser

def print_working_dir():
	"""
	Print the current working directory.
	"""
	print(os.getcwd())

if __name__ == "__main__":
	main()
