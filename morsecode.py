# -*- coding: utf8 -*-
import re


# Help Function - 수정하지 말 것
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code


# Help Function - 수정하지 말 것
def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"

    return message


def is_help_command(user_input):    
    return user_input.upper() in ('H', 'HELP')


def is_validated_english_sentence(user_input):
    # user_input = 'This is Gachon University.'
    # print(re.search('[^a-zA-Z.,!?\s]', user_input))
    # print(re.search('[a-zA-Z]', user_input))
    # print(re.match('[^.,!?\s]', user_input))
    return True if not re.search('[^a-zA-Z.,!?\s]', user_input) and re.search('[^.,!?\s]', user_input) else False


def search_validated_morse_code(user_input):
    morse_code = get_morse_code_dict()
    for morse in user_input.split():
        if not morse in get_morse_code_dict().values(): return False
    return True


def is_validated_morse_code(user_input):
    return not re.search('[^-.\s]', user_input) and re.search('[-.]', user_input) and search_validated_morse_code(user_input)


def get_cleaned_english_sentence(raw_english_sentence):
    for punctuation in '.,!?':
        raw_english_sentence = raw_english_sentence.replace(punctuation, '')
    return raw_english_sentence.strip()


def decoding_character(morse_character):
    for k, v in get_morse_code_dict().items():
        if v == morse_character: return k


def encoding_character(english_character):
    return get_morse_code_dict()[english_character]


def decoding_sentence(morse_sentence):
    result = ''
    morses = re.findall('[.-]+\s{1,2}', morse_sentence)
    
    for morse in morses:
        morse_sentence = morse_sentence.replace(morse, '', 1)
        result += decoding_character(morse.strip())
        if morse.count('  '): result += ' '
    result += decoding_character(morse_sentence)
    
    return result


def encoding_sentence(english_sentence):
    result = ''
    english_sentence = get_cleaned_english_sentence(english_sentence)

    for word in english_sentence.split():
        for char in word:
            result += encoding_character(char.upper()) + ' '
        result += ' '
    return result.rstrip()


def is_zero(user_input):
    return user_input == '0'


def main():
    print("Morse Code Program!!")
    # ===Modify codes below=============

    # test = '!X!'
    # print(is_validated_english_sentence(test))
    while(True):
        user_input = input('Input your message(H - Help, 0 - Exit): ')

        if is_help_command(user_input):
            get_help_message()

        elif is_zero(user_input):
            break  

        elif is_validated_english_sentence(user_input.strip()):
            print(encoding_sentence(user_input.strip()))
        
        elif is_validated_morse_code(user_input.strip()):
            print(decoding_sentence(user_input.strip()))

        else:
            print('Wrong Input')

    encoding_sentence('Hello! This is CS fifty Class.')

    # ==================================
    print("Good Bye")
    print("Morse Code Program Finished!!")

#입력받고 strip()

if __name__ == "__main__":
    main()