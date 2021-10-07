#Given a string of odd length greater than 7, return a new string made of the middle three characters of a given String

def get_middle_char(string):
    if len(string) % 2 == 0:
        return None
    elif len(string) <= 1:
        return None

    str_len = int(len(string)/2)

    return string[str_len]

def main():
    print('Enter a odd length string: ')
    odd_string = input()
    print('The middle character is', get_middle_char(odd_string))

main() 