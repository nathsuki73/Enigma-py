import string

ALPHABET = string.ascii_uppercase

class Rotor:
    def __init__(self, wiring, notch, position='A'):
        self.wiring = wiring
        self.notch = notch
        self.position = position

    def _pos_index(self, ch):
        return ALPHABET.index(ch)

    def step(self):
        self.position = ALPHABET[(ALPHABET.index(self.position) + 1) % 26]

    def encode_forward(self, ch):
        offset_in = (ALPHABET.index(ch) + ALPHABET.index(self.position)) % 26
        wired = self.wiring[offset_in]
        offset_out = (ALPHABET.index(wired) - ALPHABET.index(self.position)) % 26
        return ALPHABET[offset_out]

    def encode_backward(self, ch):
        offset_in = (ALPHABET.index(ch) + ALPHABET.index(self.position)) % 26
        wired_index = self.wiring.index(ALPHABET[offset_in])
        offset_out = (wired_index - ALPHABET.index(self.position)) % 26
        return ALPHABET[offset_out]

    def at_notch(self):
        return self.position in self.notch


class Reflector:
    def __init__(self, wiring):
        self.wiring = wiring

    def reflect(self, ch):
        return self.wiring[ALPHABET.index(ch)]


class SimpleEnigma:
    def __init__(self, rotors, reflector, plugboard_pairs=None):
        self.left, self.middle, self.right = rotors
        self.reflector = reflector
        self.plugboard = {c: c for c in ALPHABET}
        if plugboard_pairs:
            for a, b in plugboard_pairs:
                a, b = a.upper(), b.upper()
                self.plugboard[a] = b
                self.plugboard[b] = a

    def _plug(self, ch):
        return self.plugboard.get(ch, ch)

    def step_rotors(self):
        if self.middle.at_notch():
            self.middle.step()
            self.left.step()
        elif self.right.at_notch():
            self.middle.step()
        self.right.step()

    def encrypt_char(self, ch):
        if ch not in ALPHABET:
            return ch

        self.step_rotors()

        #Plugboard
        c = self._plug(ch)
        # right to left
        c = self.right.encode_forward(c)
        c = self.middle.encode_forward(c)
        c = self.left.encode_forward(c)
        # reflector
        c = self.reflector.reflect(c)
        # left to right
        c = self.left.encode_backward(c)
        c = self.middle.encode_backward(c)
        c = self.right.encode_backward(c)
        # plugboard
        c = self._plug(c)
        return c

    def encrypt(self, text):
        text = text.upper()
        out = []
        for ch in text:
            out.append(self.encrypt_char(ch))
        return ''.join(out)



rotor_I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", notch='Q', position='A')  # Rotor I
rotor_II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", notch='E', position='A')  # Rotor II
rotor_III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", notch='V', position='A')  # Rotor III
reflector_B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")

machine = SimpleEnigma(rotors=[rotor_I, rotor_II, rotor_III],
                       reflector=reflector_B,
                       plugboard_pairs=[('A', 'B'), ('C', 'D')])

rotor_I.position = 'P'
rotor_II.position = 'A'
rotor_III.position = 'T'
while True:
    print(f"Initial rotor position: {rotor_I.position} {rotor_II.position} {rotor_III.position}")
    plaintext = input("Enter  a plaintext: ")
    cipher = machine.encrypt(plaintext)
    print("Ciphertext:", cipher)
