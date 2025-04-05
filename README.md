# INS- Cipher Implementation and Comparative Analysis

## Overview
This repository contains implementations of classical encryption techniques, including the **Playfair Cipher, Hill Cipher, Vigenère Cipher**, and a **Hybrid Cipher** combining AES substitution and transposition techniques. Additionally, a comparative analysis of these ciphers is provided, including cryptanalysis and performance evaluation.

## Ciphers Implemented

### 1. Playfair Cipher
- **Type**: Digraph Substitution Cipher
- **Key**: 5x5 Matrix constructed from a keyword
- **Encryption Process**:
  - Organizes letters into digraphs
  - Applies substitution based on position in matrix
  - Handles duplicate letters and odd-length messages
- **Implementation**: `playfair_cipher.py`
- **Complexity**: **O(n)** for encryption and decryption

### 2. Hill Cipher
- **Type**: Matrix-Based Block Cipher
- **Key**: n x n Matrix (must have an inverse mod 26)
- **Encryption Process**:
  - Converts text into numerical vectors
  - Applies matrix multiplication mod 26
  - Uses modular inverse for decryption
- **Implementation**: `hill_cipher.py`
- **Complexity**: **O(n³)** for decryption (due to matrix inversion)

### 3. Vigenère Cipher
- **Type**: Polyalphabetic Substitution Cipher
- **Key**: Repeated keyword of arbitrary length
- **Encryption Process**:
  - Shifts letters based on the repeating key
  - Implements character-wise modulo arithmetic
- **Implementation**: `vigenere_cipher.py`
- **Complexity**: **O(n)** for encryption and decryption

### 4. Hybrid Cipher (AES + Transposition)
- **Type**: Combination of Substitution and Transposition
- **Key**: 128-bit AES key
- **Encryption Process**:
  - Encrypts with AES (Electronic Codebook Mode)
  - Applies transposition based on a fixed seed
- **Implementation**: `hybrid_cipher.py`
- **Complexity**:
  - **AES Encryption**: **O(n)**
  - **Transposition**: **O(n log n)** (sorting-based shuffling)
  - 
 ### 5. Fiestel Structure 
## Overview
This script implements a **Feistel network-based encryption** algorithm. It takes an input string and a key, performs bitwise operations, and produces an encrypted binary output. The Feistel structure is widely used in cryptographic algorithms like DES (Data Encryption Standard).

## How It Works
1. The input string is converted to **binary**.
2. The binary string is split into **two halves** (Left and Right).
3. A **key** is taken as input and converted to binary.
4. The Feistel encryption **rounds** are performed:
   - The **right half** is processed using the key and XOR’d with the left half.
   - The halves are **swapped**.
   - A second round of processing is done.
5. The final encrypted binary is converted back into text.

## How to Run the Code

### Prerequisites
Before running the scripts, ensure you have the following installed:
- **Python 3.x**
- **NumPy** (for matrix operations in Hill Cipher)
- **PyCryptodome** (for AES encryption in Hybrid Cipher)

Install dependencies using:
```sh
pip install numpy pycryptodome
```

### Using GitHub Codespaces
If using **GitHub Codespaces**, follow these steps:

**Cipher_Codes Codespace**

Use this codespace to run the files

OR 

1. **Open the Repository in Codespaces**
   - Navigate to your repository on GitHub
   - Click on `<> Code` → `Codespaces` → `New Codespace`

2. **Run the Scripts**
   - Open the terminal in Codespaces
   - Run any of the Python scripts using:
     ```sh
     python3 <script_name>.py
     ```
   Example:
     ```sh
     python3 vigenere_cipher.py
     ```

3. **Provide Input When Prompted**
   - Each script may ask for input (key, plaintext, etc.)

## Example Usage

### Playfair Cipher
```sh
python3 playfair_cipher.py
```
**Input:**
```
Enter the key: SECRET
Enter the message: HELLO WORLD
```
**Output:**
```
Encrypted Message: KFMTHZBQKD
```

### Hill Cipher
```sh
python3 hill_cipher.py
```
**Input:**
```
Plaintext: SHORT
Key Matrix: [[7, 8], [11, 11]]
```
**Output:**
```
Encrypted: WFJTG
```

### Vigenère Cipher
```sh
python3 vigenere_cipher.py
```
**Input:**
```
Plaintext: HELLO
Key: KEY
```
**Output:**
```
Ciphertext: RIJVS
Decrypted: HELLO
```

### Hybrid Cipher (AES + Transposition)
```sh
python3 hybrid_cipher.py
```
**Input:**
```
Plaintext: HELLO WORLD
Key: thisis128bitkey
```
**Output:**
```
Encrypted: [Hexadecimal String]
Decrypted: HELLO WORLD
```
### Fiestel Structure

```sh
python3 fiestel_structure.py
```
**Input:**
```
enter the string:hello world
Result :  0110100001100101011011000110110001101111001000000111011101101111011100100110110001100100
**Output:**
```
enter the key :hello
0110100001100101011011000110110001101111001000000111011101101111011100100110110001100100
h
he
hel
hell
hello
hello 
hello w
hello wo
hello wor
hello worl
hello world



# INS- MINI PROJECT README FILE

# 🔐 Secure Data Handling GUI with AES and RSA

This Python application demonstrates secure data handling through **AES encryption**, **RSA digital signatures**, and a simple **graphical user interface (GUI)** built using Tkinter. It enables users to encrypt and decrypt text, sign data digitally, and verify digital signatures—all within an easy-to-use desktop interface.

---

## 📌 Features

- **AES-256 Encryption & Decryption (CBC Mode)**  
  Encrypts and decrypts plaintext with a randomly generated key and initialization vector (IV).

- **RSA Digital Signature & Verification**  
  Signs the text using RSA and SHA-256 hash. Verifies the authenticity and integrity of the signed message.

- **User-Friendly GUI (Tkinter)**  
  Clean interface for secure operations—no command-line knowledge needed.

- **Base64 Encoding for Output**  
  All encrypted and signed outputs are encoded for readability and ease of copying.

---

## 🛠 Technologies Used

- Python 3
- Tkinter (for GUI)
- PyCryptodome (for cryptography: AES, RSA, SHA-256)

---

## 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/secure-data-handler.git
cd secure-data-handler
```

### 2. Install dependencies
```bash
pip install pycryptodome
```

### 3. How to Run
```bash
python "mini project.py"
```
## A window will open allowing you to enter text, encrypt/decrypt, sign/verify easily through buttons.
## Testing & Evaluation
✅ AES encryption/decryption tested with ASCII, Unicode, and edge cases (e.g., empty strings).

✅ Digital signature verification accurately detects any tampering with the original message.

⚠️ Note: RSA keys are regenerated on every run; long-term use would require secure key storage.

⚠️ Padding is implemented manually; consider using Crypto.Util.Padding for standardized methods.


