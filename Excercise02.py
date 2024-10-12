#!/usr/bin/evn python3

def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    return sorted(word1) == sorted(word2)

def run():
    print(is_anagram('tame', 'fame'))
    print(is_anagram('tops', 'stop'))

def main():
    count = 0
    with open('files/words.txt', 'r') as file:
        for word in file:
            word = word.strip().lower()
            if is_anagram(word, 'takes'):
                count += 1
                print(word)
    print(f'Found {count} anagrams for takes')

if __name__ == '__main__':
    # run()
    main()