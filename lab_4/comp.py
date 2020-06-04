import argparse


def cmp(input_fn_1, input_fn_2):
    with open(input_fn_1, 'r') as input1, open(input_fn_2, 'r') as input2:
        alpha1 = [0 for _ in range(26)]
        alpha2 = [0 for _ in range(26)]
        s1 = input1.read()
        s2 = input2.read()
        if len(s1) > len(s2):
            s1 = s1[:len(s2)]
        else:
            s2 = s2[:len(s1)]
        all_chars = len(s1)
        success = 0
        for ch in s1:
            alpha1[ord(ch) - ord('a')] += 1
        for ch in s2:
            alpha2[ord(ch) - ord('a')] += 1

        for i in range(26):
            success += min(alpha1[i], alpha2[i])

        return success / all_chars


def main():
    a_parser = argparse.ArgumentParser()
    a_parser.add_argument('--input1', required=True, help='File for input №1')
    a_parser.add_argument('--input2', required=True, help='File for input №2')
    args = a_parser.parse_args()
    print(cmp(args.input1, args.input2))


if __name__ == "__main__":
    main()
