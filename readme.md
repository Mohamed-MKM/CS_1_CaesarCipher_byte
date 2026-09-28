# Caesar Cipher — Text Encryption & Decryption

A simple Python implementation of the **Caesar Cipher**, a classical substitution cipher that shifts alphabetic characters by a configurable number of positions.

This project was completed as part of the **B.Y.T.E by Arithmatrix CyberSecurity Internship — Task 1**.

## Features

* Encrypt plaintext using a configurable shift value.
* Decrypt ciphertext using the same shift value.
* Supports both uppercase and lowercase letters.
* Preserves spaces, numbers, punctuation, and other non-alphabetic characters.
* Handles positive and negative shift values.
* Provides clear input/output examples.
* Includes test cases for encryption and decryption.

## How Caesar Cipher Works

The Caesar Cipher replaces each alphabetic character with another character a fixed number of positions away in the alphabet.

For example, using a shift of `3`:

```text
A → D
B → E
C → F
...
X → A
Y → B
Z → C
```

Example:

```text
Plaintext:  HELLO
Shift:     3
Ciphertext: KHOOR
```

Decryption reverses the operation:

```text
Ciphertext: KHOOR
Shift:      3
Plaintext:  HELLO
```

## Requirements

* Python 3.x

No external libraries are required.

## Installation

Clone the repository:

```bash
git clone <https://github.com/Mohamed-MKM/CS_1_CaesarCipher_byte.git>
cd CS_1_CaesarCipher_byte
```

## Usage

Run the program:

```bash
python caesar_cipher.py
```

The program will request:

1. The operation: encryption or decryption
2. The text
3. The shift value

### Example — Encryption

```text
Enter operation (encrypt/decrypt): encrypt
Enter text: Hello World!
Enter shift: 3

Output: Khoor Zruog!
```

### Example — Decryption

```text
Enter operation (encrypt/decrypt): decrypt
Enter text: Khoor Zruog!
Enter shift: 3

Output: Hello World!
```

## Non-Alphabet Characters

Non-alphabetic characters are preserved.

Example:

```text
Input:  Hello, World! 123
Shift:  3
Output: Khoor, Zruog! 123
```

The comma, spaces, exclamation mark, and numbers are not modified.

## Project Structure

```text
CS_1_CaesarCipher_byte/
│
├── caesar_cipher.py
├── test_cases.txt
├── sample_input.txt
├── sample_output.txt
├── screenshot/
│   └── demo.png
└── README.md
```

## Testing

Example test cases:

| Input          | Shift | Operation | Expected Output |
| -------------- | ----: | --------- | --------------- |
| `HELLO`        |     3 | Encrypt   | `KHOOR`         |
| `KHOOR`        |     3 | Decrypt   | `HELLO`         |
| `Hello World!` |     5 | Encrypt   | `Mjqqt Btwqi!`  |
| `123 ABC!`     |     2 | Encrypt   | `123 CDE!`      |
| `XYZ`          |     3 | Encrypt   | `ABC`           |

## Sample Execution

```text
================================
       CAESAR CIPHER
================================

Enter operation (encrypt/decrypt): encrypt
Enter text: CyberSecurity
Enter shift: 4

Original : CyberSecurity
Shift    : 4
Result   : GcfivWigxvmx}
```

> Note: The exact output depends on the implementation and selected shift. The included test cases should be used as the authoritative verification examples.

## Security Note

The Caesar Cipher is a **classical educational cipher** and should not be used to protect sensitive information in real-world applications. It is included in this project for educational purposes to demonstrate basic cryptographic concepts.

## Deliverables

* Public GitHub repository
* Source code
* README documentation
* Sample input/output files
* Test cases
* Demonstration screenshot or terminal recording

## Author

**Mohamed MK**

CyberSecurity Internship — B.Y.T.E by Arithmatrix
