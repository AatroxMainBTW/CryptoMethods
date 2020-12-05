def cz_cipher(text, key):
    list1 = [char for char in text];
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    final = []
    for letter2 in alphabet:

        for letter in list1:
            if letter2 == key:
                pos = alphabet.index(key)
                if letter in alphabet:
                    ti = alphabet.index(letter)
                    ti += pos
                    if ti > 25:
                        ti -= 26
                    final.append(alphabet[ti])
                else:
                    final.append(letter)
    print("Crypt: " + str(final))


def cz_decode(text, key):
    list1 = [char for char in text];
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    final = []
    for letter2 in alphabet:
        for letter in list1:
            if letter2 == key:
                pos = alphabet.index(key)
                if letter in alphabet:
                    ti = alphabet.index(letter)
                    ti -= pos
                    if ti < 0:
                        ti += 26
                    final.append(alphabet[ti])
                else:
                    final.append(letter)
    print("Decrypt: " + str(final))


def main():
    cz_cipher("hammouda", "r")
    cz_decode("yrddflur", "r")


main()
