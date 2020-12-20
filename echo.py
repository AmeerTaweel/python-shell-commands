"""
Replicated command: echo

Print the passed argument to the output stream.
"""

import argparse

def main():
	"""
	Parse and handle user's call.
	"""
	parser = setup_argument_parser()
	arguments = parser.parse_args()
	to_print = arguments.to_print
	print(to_print)

def setup_argument_parser():
	"""
	Setup argument parser wtih required arguments and their properties.
	"""
	parser = argparse.ArgumentParser(
		description = "Print the passed argument to the output stream."
	)
	parser.add_argument(
		"to_print",
		help = "The text to print."
	)
	return parser

if __name__ == "__main__":
	main()
