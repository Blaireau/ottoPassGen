# Alphabet "hardcoded" in the ROM
alphabet = 'qw2rty534plkjhgfds1zxcvbnm'
# Dictionary set up, following the previous alphabet
alpha_dict = {'q': 0, 'w': 1, '2': 2, 'r': 3, 't': 4, 'y': 5, '5': 6, '3': 7, '4': 8, 'p': 9, 'l': 10, 'k': 11, 'j': 12,
              'h': 13, 'g': 14, 'f': 15, 'd': 16, 's': 17, '1': 18, 'z': 19, 'x': 20, 'c': 21, 'v': 22, 'b': 23,
              'n': 24, 'm': 25}
list_out = open("otto", "w")


def reduction(my_letter):
    while my_letter >= 0:
        my_letter = my_letter - 26
    return my_letter + 26


def my_sub(number1, number2):
    result = number2 - number1
    if result < 0:
        result += 26
    return result


for letter1 in alphabet:
    for letter2 in alphabet:
        for letter3 in alphabet:
            for letter4 in alphabet:
                for letter5 in alphabet:
                    a, b, c, d, e = alpha_dict[letter1], alpha_dict[letter2], alpha_dict[letter3], alpha_dict[letter4], \
                                    alpha_dict[letter5]
                    a = reduction(a)
                    b = reduction(b + a)
                    c = reduction(b + c)
                    d = reduction(d + c)

                    # If the checksum is passed, we have a valid code.
                    # Let's calculate the result that it should give.
                    if d == e:
                        # Let's implement the lvl number and life calculation !
                        # See Readme for technical details
                        first_letter, second_letter, third_letter, fourth_letter = apha_dict[letter1], alpha_dict[
                            letter2], alpha_dict[letter3], alpha_dict[letter4]

                        # First we have to sub the value of the "first" letter to all the others letters.
                        # One time for the first, two times for the second and three times for the third.
                        # I decided to mimic the ASM code (i.e. calling a func to do that)

                        # 1 call
                        second_letter = my_sub(first_letter, second_letter)

                        # 2 calls
                        third_letter = my_sub(first_letter, third_letter)
                        third_letter = my_sub(first_letter, third_letter)

                        # 3 calls
                        fourth_letter = my_sub(first_letter, fourth_letter)
                        fourth_letter = my_sub(first_letter, fourth_letter)
                        fourth_letter = my_sub(first_letter, fourth_letter)

list_out.close()
