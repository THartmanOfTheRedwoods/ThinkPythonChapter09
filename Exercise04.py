#!/usr/bin/evn python3

def reverse_sentence(sentence):
    print(' '.join(
        reversed(
            sentence.split(' '))).lower().capitalize())

def main():
    reverse_sentence('Reverse this sentence')
    reverse_sentence('Unlearn what you have learned')
    reverse_sentence('Feel the Force')

if __name__ == '__main__':
    main()