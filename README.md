# Simple Enigma Machine in Python

This Python program simulates a simplified version of the World War II Enigma machine. It allows you to encrypt and decrypt messages using rotor-based substitution, a reflector, and an optional plugboard.

---

## Features

* 3 rotors with configurable wiring, notch, and initial positions
* Reflector for bidirectional encryption
* Optional plugboard swaps for additional complexity
* Continuous rotor stepping, changing the encryption dynamically

---

## Requirements

* Python 3.x
* Standard library (`string` module is used)

---

## Installation

1. Clone or download this repository.
2. Make sure Python 3 is installed on your system.
3. Save the `enigma.py` file (or your script) in a folder.

---

## How to Run

1. Open a terminal or command prompt.
2. Navigate to the folder containing your `enigma.py` file.
3. Run the script:

```bash
python enigma.py
```

4. The program will display the initial rotor positions and prompt you for a plaintext message.
5. Enter your message and press Enter to see the encrypted ciphertext.
6. You can encrypt multiple messages; the rotor positions will continue to update with each key press.

---

## Example

```
Initial rotor position: P A T
Enter a plaintext: HELLO
Ciphertext: XZQMF
```

---

## How to Set Rotor Positions

You can set initial rotor positions by modifying the following lines in the script:

```python
rotor_I.position = 'P'
rotor_II.position = 'A'
rotor_III.position = 'T'
```

Change the letters to any uppercase A–Z to start with different rotor settings.

---

## Notes

* Only uppercase A–Z letters are encrypted; other characters are passed through unchanged.
* Using the same rotor settings and plugboard configuration allows decryption by running the ciphertext through the machine again.

---

This is a simplified educational version and **does not replicate all real Enigma features**, but it demonstrates the core encryption mechanics.
