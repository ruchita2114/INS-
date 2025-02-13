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

## Comparative Analysis
| Cipher       | Type                         | Key Size        | Complexity (Enc/Dec) | Strengths                        | Weaknesses |
|-------------|------------------------------|-----------------|----------------------|---------------------------------|------------|
| Playfair    | Digraph Substitution         | 5x5 Key Matrix  | O(n)                 | More secure than simple monoalphabetic | Still vulnerable to digraph analysis |
| Hill        | Matrix-Based Block Cipher    | n x n Matrix    | O(n³)                 | Stronger encryption, uses algebra | Requires invertible key matrix |
| Vigenère    | Polyalphabetic Substitution  | Variable Length | O(n)                  | Resists simple frequency analysis | Still breakable with Kasiski method |
| Hybrid (AES+Transposition) | Block Cipher + Shuffling | 128-bit Key  | O(n) AES, O(n log n) Transposition | Strong cryptographic security | Computationally heavier |

## Future Improvements
- Implement **automated cryptanalysis tools** to break weak ciphers.
- Enhance **key management** for Hill and Playfair ciphers.
- Extend hybrid cipher with **CBC mode encryption** for AES security.

For any issues or contributions, feel free to submit a pull request or open an issue in the repository. 
