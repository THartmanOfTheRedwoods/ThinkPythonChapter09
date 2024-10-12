#!/usr/bin/evn python3

def total_length(str_list):
    return sum(len(a.strip()) for a in str_list)

def run():
    print(total_length(['hello', 'world', 'I\'m', 'here']))

def main():
    with open('files/words.txt', 'r') as file:
        print(total_length(file.readlines()))

if __name__ == '__main__':
    #run()
    main()