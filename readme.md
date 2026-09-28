# Caesar Cipher — Text Encryption & Decryption

A simple Python implementation of the **Caesar Cipher** that supports both encryption and decryption using a configurable shift key.

This project was completed as part of the **B.Y.T.E by Arithmatrix CyberSecurity Internship — Task 1**.

## Features

* Encrypts plaintext using a configurable shift key.
* Decrypts ciphertext using a configurable shift key.
* Supports uppercase and lowercase letters.
* Preserves the original letter capitalization.
* Preserves spaces, numbers, punctuation, and other non-alphabet characters.
* Supports shift values from 1 to 25.
* Validates the entered shift value.
* Handles invalid operation choices.
* Includes test cases and sample input/output.

## How It Works

The Caesar Cipher shifts each alphabetic character by a fixed number of positions in the alphabet.

For example, with a key of `3`:

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
Plaintext:  Hello
Key:       3
Ciphertext: Khoor
```

Decryption reverses the same operation:

```text
Ciphertext: Khoor
Key:        3
Plaintext:  Hello
```

## Requirements

* Python 3.x

No external Python packages are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/CS_1_CaesarCipher_byte.git
```

Move into the project directory:

```bash
cd CS_1_CaesarCipher_byte
```

## Running the Program

Run:

```bash
python caesar_cipher.py
```

The program asks whether you want to encrypt or decrypt a message.

### Encryption Example

```text
Welcome to the Caesar Cipher Program!

Do you want to encrypt or decrypt a message?

Type "e" to encrypt, type "d" to decrypt:
e

Enter the key (a number between 1 and 25):
3

Enter the message:
Hello, World!

Encrypted message: Khoor, Zruog!
```

### Decryption Example

```text
Welcome to the Caesar Cipher Program!

Do you want to encrypt or decrypt a message?

Type "e" to encrypt, type "d" to decrypt:
d

Enter the key (a number between 1 and 25):
3

Enter the message:
Khoor, Zruog!

Decrypted message: Hello, World!
```

## Character Handling

Alphabetic characters are shifted while non-alphabetic characters remain unchanged.

Example:

```text
Input:
Hello, World! 123

Key:
3

Output:
Khoor, Zruog! 123
```

The following characters are preserved:

* Spaces
* Numbers
* Commas
* Periods
* Exclamation marks
* Other non-alphabetic characters

Uppercase letters also remain uppercase.

Example:

```text
Input:  HELLO World
Key:    3
Output: KHOOR Zruog
```

## Key Validation

The program accepts keys from `1` to `25`.

If an invalid key is entered, the program displays an error message.

Example:

```text
Enter the key (a number between 1 and 25):
26

Invalid key. Please enter a number between 1 and 25.
```

## Test Cases

The repository contains `test_cases.txt` with test cases covering:

* Basic encryption
* Basic decryption
* Uppercase and lowercase characters
* Spaces and punctuation
* Numbers
* Alphabet wraparound
* Decryption wraparound
* Maximum supported key
* Invalid key
* Invalid operation

Example:

| Test | Input           | Key | Operation | Expected Output |
| ---- | --------------- | --: | --------- | --------------- |
| 1    | `Hello`         |   3 | Encrypt   | `Khoor`         |
| 2    | `Khoor`         |   3 | Decrypt   | `Hello`         |
| 3    | `Hello World`   |   3 | Encrypt   | `Khoor Zruog`   |
| 4    | `Hello, World!` |   3 | Encrypt   | `Khoor, Zruog!` |
| 5    | `XYZ`           |   3 | Encrypt   | `ABC`           |
| 6    | `ABC`           |   3 | Decrypt   | `XYZ`           |

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

## Demonstration

A terminal screenshot or screen recording should demonstrate at least:

1. Starting the program.
2. Encrypting a message.
3. Decrypting the resulting ciphertext.
4. Showing that punctuation and numbers remain unchanged.

Recommended demonstration:

```text
Original:
Hello, World! 123

Encrypted with key 3:
Khoor, Zruog! 123

Decrypted with key 3:
Hello, World! 123
```

## Security Note

The Caesar Cipher is a classical educational cipher and is **not suitable for protecting sensitive information in real-world applications**.

It is included in this project for educational purposes to demonstrate basic encryption and decryption concepts.

## Deliverables

This repository contains the required internship deliverables:

* [x] Public GitHub repository
* [x] Source code
* [x] README with usage examples
* [x] Sample input file
* [x] Sample output file
* [x] Test-case file
* [ ] Demonstration screenshot or terminal recording

The demonstration screenshot/recording should be added before final submission.

## Repository

Repository naming convention:

```text
CS_1_CaesarCipher_byte
```

This follows the internship requirement:

```text
DomainShortHand_TaskNumber_TaskTitle_byte
```

## Author

**Mohamed MK**

CyberSecurity Internship — B.Y.T.E by Arithmatrix
