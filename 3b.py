# import sys
import sys


def rev_sentence(sentence):
    #  first split the string into words
    words = sentence.split(' ')

    #     then reverse the split string list and join using space
    reverse_sentence = ' '.join(reversed(words)).upper()
    #     finally return the joined string
    return reverse_sentence


if __name__ == "__main__":
    line = input("enter sentence: ")

    sys.stdout.write(rev_sentence(line))
