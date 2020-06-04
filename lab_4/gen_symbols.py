import argparse
import random
import string


def create(input_fn, output_fn):
    with open(input_fn, 'r') as input, open(output_fn, 'w') as output:
        l = len(input.read())
        for _ in range(l):
            output.write(random.choice(string.ascii_lowercase))


def main():
    a_parser = argparse.ArgumentParser()
    a_parser.add_argument('--input', required=True, help='File to create a new file of the same size')
    a_parser.add_argument('--output', required=True, help='File for new file')
    args = a_parser.parse_args()

    create(args.input, args.output)


if __name__ == '__main__':
    main()
