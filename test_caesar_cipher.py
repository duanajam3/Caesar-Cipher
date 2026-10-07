from caesar_cipher import caesar_cipher

assert caesar_cipher("ABC", 3) == "DEF"
assert caesar_cipher("abc", 3) == "def"
assert caesar_cipher("Hello, World!", 3) == "Khoor, Zruog!"
assert caesar_cipher("Khoor, Zruog!", -3) == "Hello, World!"
assert caesar_cipher("XYZ xyz!", 3) == "ABC abc!"

print("All Caesar Cipher tests passed.")
