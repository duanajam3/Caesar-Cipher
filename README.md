# Caesar Cipher

**AVIP 2026 Cybersecurity — Task 1**

## Objective
Implement a configurable Caesar Cipher that can encrypt and decrypt text using a shift value.

## Features
- Encrypts uppercase and lowercase letters.
- Preserves spaces, numbers, and punctuation.
- Supports positive and negative shifts.
- Includes encryption/decryption demonstration.
- Includes automated tests.

## Files
- `caesar_cipher.py` — main program
- `tests/test_caesar_cipher.py` — test cases
- `sample_output.txt` — example run

## How to Run

```bash
python caesar_cipher.py
```

Example:
```text
Enter text: Hello, World!
Enter shift: 3
Encrypted: Khoor, Zruog!
Decrypted: Hello, World!
```

## How to Run Tests

```bash
python tests/test_caesar_cipher.py
```

Expected:
```text
All Caesar Cipher tests passed.
```

## Cybersecurity Concept
The Caesar Cipher is a basic classical substitution cipher. It is useful for learning the fundamentals of encryption, decryption, and key/shift-based transformations.

## Ethics
This project is for educational purposes and demonstrates a classical cipher. It should not be considered secure encryption for protecting real confidential information.
