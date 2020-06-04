import argparse


def parser(input_fn, output_fn):
    with open(input_fn, 'r') as input, open(output_fn, 'w') as output:
        for row in input:
            str = ''
            for ch in row:
                if ch.isalpha():
                    output.write(ch.lower())

def main():
    a_parser = argparse.ArgumentParser()
    a_parser.add_argument('--input', required=True, help='File for input')
    a_parser.add_argument('--output', required=True, help='File for output')
    args = a_parser.parse_args()
    parser(args.input, args.output)


if __name__ == "__main__":
    main()
