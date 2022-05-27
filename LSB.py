import cv2
import numpy as np


def message2binary(message):
    if type(message) == str:
        return ''.join([format(ord(i), "08b") for i in message])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [format(i, "08b") for i in message]
    elif type(message) == int or type(message) == np.uint8:
        return format(message, "08b")
    else:
        raise TypeError("Wejście nieobsługiwane")


def hide_data(image, secret_message):

    n_bytes = image.shape[0] * image.shape[1] * 3 // 8
    print("Maksymalna długość wiadomości do zakodowania w bitach: ", n_bytes)

    # sprawdzenie, czy wiadomość zmieści się w obrazie
    if len(secret_message) > n_bytes:
        raise ValueError("Potrzeba większego obrazu lub mniejszej wiadomości!")

    # miejsce zakończenia wiadomości
    secret_message += "#end#"

    data_index = 0
    # zapis binarny wiadomości
    binary_secret_msg = message2binary(secret_message)

    data_len = len(binary_secret_msg)   # ilość bitów
    for values in image:
        for pixel in values:
            # zamiana RGB na zapis binarny
            r, g, b = message2binary(pixel)
            # zamiana LSB
            if data_index < data_len:   # czerwony
                pixel[0] = int(r[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            if data_index < data_len:   # zielony
                pixel[1] = int(g[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            if data_index < data_len:   # niebieski
                pixel[2] = int(b[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
                if data_index >= data_len:
                    break
        return image


def show_data(image):
    binary_data = ""
    for values in image:
        for pixel in values:
            r, g, b = message2binary(pixel)
            # odzyskiwanie zakodowanych bitów
            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]
    all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8)]
    # zamiana bitów na znaki
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "#end#":    # szukanie końca wiadomości
            break
    return decoded_data[:-5]    # usunięcie #end# z wiadomości


# Encode data into image 
def encode_text():
    image_name = input("Podaj nazwę pliku do zakodowania wiadomości: ") + ".png"
    image = cv2.imread(image_name)

    print("Wielkość obrazu: ", image.shape)
    data = input("Wiadomość do zakodowania : ")
    if len(data) == 0:
        raise ValueError('Brak wiadomości!')

    filename = input("Podaj nazwę pliku wynikowego z zakodowaną wiadomością: ") + ".png"
    encoded_image = hide_data(image, data)
    cv2.imwrite(filename, encoded_image)


def decode_text():
    image_name = input("Podaj nazwę pliku do odkodowania wiadomości: ") + ".png"
    image = cv2.imread(image_name)
    text = show_data(image)
    return text


def steganography():
    while True:
        a = input("Steganografia \n 1. Zakoduj wiadomość \n 2. Odkoduj wiadomość \n 3. Zakończ program \n Twój wybór: ")
        userinput = int(a)
        if userinput == 1:
            encode_text()
        elif userinput == 2:
            print("Zakodowana wiadomość: " + decode_text())
        elif userinput == 3:
            break
        else:
            raise Exception("Złe wejście!")


if __name__ == "__main__":
    steganography()
