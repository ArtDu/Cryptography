import argparse
import random


def isWordAlpha(word):
    for ch in word:
        if not ch.isalpha():
            return False
    return True

    
def create(input_fn, output_fn, dict_fn):
    with open(input_fn, 'r') as input, \
            open(output_fn, 'w') as output, \
            open(dict_fn, 'r') as dict_fl:
        words = []
        for word in dict_fl:
            if word[-1] == '\n':
                word = word[:-1]
            words.append(word)

        l = len(input.read())
        new_l = 0
        while True:
            word = random.choice(words)
            if not isWordAlpha(word):
                continue
            word = word.lower()
            if new_l < l:
                output.write(word)
                new_l += len(word)
            else:
                output.write(word[:l - new_l])
                break


def main():
    a_parser = argparse.ArgumentParser()
    a_parser.add_argument('--input', required=True, help='File to create a new file of the same size')
    a_parser.add_argument('--dict', required=True, help='File with words(dictionary)')
    a_parser.add_argument('--output', required=True, help='File for new file')
    args = a_parser.parse_args()

    create(args.input, args.output, args.dict)


if __name__ == '__main__':
    main()
