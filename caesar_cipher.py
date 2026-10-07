def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
        elif char.islower():
            result += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
        else:
            result += char

    return result


def main():
    text = input("Enter text: ")
    shift = int(input("Enter shift: "))

    encrypted = caesar_cipher(text, shift)
    decrypted = caesar_cipher(encrypted, -shift)

    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)


if __name__ == "__main__":
    main()
