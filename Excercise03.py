#!/usr/bin/evn python3

def is_palindrome(word):
    return ''.join(reversed(word)) == word

def run():
    print(is_palindrome('civic'))
    print(is_palindrome('tops'))

def main():
    count = 0
    with open('files/words.txt', 'r') as file:
        for word in file:
            word = word.strip().lower()
            if len(word) >= 7 and is_palindrome(word):
                count += 1
                print(word)
    print(f'Found {count} anagrams for takes')

if __name__ == '__main__':
    # run()
    main()