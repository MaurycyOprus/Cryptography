def matrix_generator(entry_key):
    key = []
    for i in list(entry_key):
        if i not in key:
            if i == 'j':
                if 'i' not in key:
                    key.append('i')
            else:
                key.append(i)

    for i in [x for x in range(65, 91) if x != 74]:
        if chr(i).lower() not in key:
            key.append(chr(i).lower())

    index = 0
    for i in range(0, 5):
        for j in range(0, 5):
            matrix[i][j] = key[index]
            index += 1

    return matrix


def char_index(searched_char, matrix_0):
    global down, right
    for i in range(0, 5):
        for j in range(0, 5):
            if searched_char == matrix_0[i][j]:
                down, right = i, j
                break
    return down, right


def encode_text(txt):
    encoded_text = []
    i = 0
    while i < len(txt):
        if i == len(txt) - 1 and i % 2 == 0:
            txt.append("x")
        elif txt[i] == txt[i + 1]:
            down, right = char_index(txt[i], matrix)
            down_1, right_1 = char_index('x', matrix)  # filtr
            if down == down_1:
                encoded_text.append(matrix[down][(right + 1) % 5])
                encoded_text.append(matrix[down_1][(right_1 + 1) % 5])
            elif right == right_1:
                encoded_text.append(matrix[(down + 1) % 5][right])
                encoded_text.append(matrix[(down_1 + 1) % 5][right_1])
            else:
                encoded_text.append(matrix[down][right_1])
                encoded_text.append(matrix[down_1][right])
            i += 1
        else:
            down, right = char_index(txt[i], matrix)
            down_1, right_1 = char_index(txt[i + 1], matrix)
            if down == down_1:
                encoded_text.append(matrix[down][(right + 1) % 5])
                encoded_text.append(matrix[down_1][(right_1 + 1) % 5])
            elif right == right_1:
                encoded_text.append(matrix[(down + 1) % 5][right])
                encoded_text.append(matrix[(down_1 + 1) % 5][right_1])
            else:
                encoded_text.append(matrix[down][right_1])
                encoded_text.append(matrix[down_1][right])
            i += 2
    return encoded_text


def decode_text(txt):
    decoded_text = []
    i = 0
    if len(txt) % 2 != 0:
        txt.append('x')
    while i < len(text):
        down, right = char_index(txt[i], matrix)
        down_1, right_1 = char_index(txt[i + 1], matrix)
        if down == down_1:
            decoded_text.append(matrix[down][(right + 4) % 5])
            decoded_text.append(matrix[down_1][(right_1 + 4) % 5])
        elif right == right_1:
            decoded_text.append(matrix[(down + 4) % 5][right])
            decoded_text.append(matrix[(down_1 + 4) % 5][right_1])
        else:
            decoded_text.append(matrix[down][right_1])
            decoded_text.append(matrix[down_1][right])
        i += 2
    return decoded_text


# text_to_decode = "sbdlamlihzfsendqnyndlyahnboutxuznxduscme"


matrix = [[0 for i in range(5)] for j in range(5)]

while True:
    print("Menu: ")
    print("1) Encode text")
    print("2) Decode text")
    print("3) Exit")
    print("4) Ready file to encode")
    option = int(input("Your choice: "))
    if option == 1:
        key_1 = input("Enter keyword: ")
        matrix_generator(key_1)
        print(matrix)
        text = input("Enter text to encode: ")
        text_1 = list(text.translate(str.maketrans('', '', " .,!?()-'")).lower())
        print("Encoded text:")
        print(''.join(encode_text(text_1)))
    elif option == 2:
        key_1 = input("Enter keyword: ")
        matrix_generator(key_1)
        text = input("Enter encoded text: ")
        print(''.join(decode_text(list(text))))
    elif option == 3:
        break
    elif option == 4:
        key_1 = input("Enter keyword: ")
        matrix_generator(key_1)
        with open('data.txt', 'r') as file:
            data = file.read().replace('\n', '')
        text = list(data.translate(str.maketrans('', '', " '.,!?()-'")).lower())
        print("Encoded text:")
        print(''.join(encode_text(text)))
        print(len(text))
    else:
        print("Wrong option!")
