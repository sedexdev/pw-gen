"""
Create a strong password generator that allows you
to set number of mixed-case letters, symbols, and
numbers present
"""

import argparse
import os
import sys

from random import randint, seed
from string import ascii_lowercase, ascii_uppercase


def add_args(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    """
    Adds arguments to an instance of argparse.ArgumentParser
    then returns the generated Namespace object

    Args:
        parser (argparse.ArgumentParser): argument parsing object
    Returns:
        argparse.ArgumentParser: argument parsing object
    """
    parser.add_argument("-l", "--letters",
                        dest="letters",
                        type=int,
                        required=True,
                        help="Number of letters to use in generated password")
    parser.add_argument("-n", "--numbers",
                        dest="numbers",
                        type=int,
                        required=True,
                        help="Number of numbers to use in generated password")
    parser.add_argument("-s", "--symbols",
                        dest="symbols",
                        type=int,
                        required=True,
                        help="Number of symbols to use in generated password")
    return parser


def get_args() -> argparse.Namespace:
    """
    Gets command line arguments from the user

    Returns:
        argparse.Namespace: terminal arguments from user
    """
    parser = argparse.ArgumentParser()
    add_args(parser)
    args = parser.parse_args()
    return args


def get_pw_chars(l, n, s) -> str:
    """
    Randomly select the chars for the
    password

    Args:
        l (int): number of letters to use
        n (str): number of numbers to use
        s (str): number of symbols to use
    Returns:
        str: chars for password
    """
    numbers = "".join([str(i) for i in range(10)])
    symbols = "\"#$%&'()*+,-.\\/:;<=>?@[] ^_`{|}~"

    chars = ""
    # split letter count to get lower and upper case letters
    letter_split = l // 2
    lower_count = l - letter_split
    upper_count = l - lower_count

    # append lower_count lower case letters
    for _ in range(lower_count):
        chars += ascii_lowercase[randint(0, len(ascii_lowercase)-1)]

    # append upper_count upper case letters
    for _ in range(upper_count):
        chars += ascii_uppercase[randint(0, len(ascii_uppercase)-1)]

    # append n numbers
    for _ in range(n):
        chars += numbers[randint(0, len(numbers)-1)]

    # append s symbols
    for _ in range(s):
        chars += symbols[randint(0, len(symbols)-1)]

    print(chars)

    return chars


def gen_password(chars) -> str:
    """
    Creates a secure password from the
    randomly selected chars by shuffling
    the <chars> string

    Args:
        chars (str): chars that were randomly chosen
    Returns:
        str: shuffled chars as the password
    """
    password = ""

    while len(chars) > 0:
        index = randint(0, len(chars)-1)
        password += chars[index]
        chars = chars[:index] + chars[index+1:]

    return password


def main() -> None:
    """
    Main function
    """
    args = get_args()

    num_letters = args.letters
    num_numbers = args.numbers
    num_symbols = args.symbols

    pw_length = num_letters + num_numbers + num_symbols

    if pw_length < 8:
        print("[-] A password should be a minimum of 8 characters for better security")
        sys.exit()
    else:
        chars = get_pw_chars(num_letters, num_numbers, num_symbols)
        password = gen_password(chars)
        print("*" * len(password))
        print(password)
        print("*" * len(password))


if __name__ == "__main__":
    seed(os.urandom(16))
    print("\t\n-- Python random Password Generator --\n")
    main()
