import string

class Rotor:
    def __init__(self, tyre, tNotch):
        self.tyre = list(tyre.upper())
        self.tNotch = tNotch
        self.pos = 0

    def rotate(self):
        self.tyre = self.tyre[-1:] + self.tyre[:-1]

class Scrambler:
    def __init__(self):
        self.rotors = []
        self.rotorscp = self.rotors
        self.alphabet = list(string.ascii_uppercase)
        self.nRotors = 0
    
    def add_rotor(self, rotor):
        rotor.pos = self.nRotors
        self.nRotors += 1
        self.rotors.append(rotor)

    def encrypt(self, plaintext):
        ciphertext = ""
        plaintext = plaintext.upper()
        for char in plaintext:
            for rotor in self.rotors:
                if char == rotor.tNotch:
                    rotor.rotate()
                if rotor.pos == 0:
                    rotor.rotate()
                index = self.alphabet.index(char)
                tempcipher = rotor.tyre[index]
                char = tempcipher
            ciphertext += tempcipher
        return(ciphertext)
    
    def reset(self):
        self.rotors = self.rotorscp

    def decrypt(self, ciphertext):
        plaintext = ""
        for char in ciphertext:
            for rotor in self.rotors:
                if char == rotor.tNotch:
                    rotor.rotate()
                if rotor.pos == 0:
                    rotor.rotate()
                index = rotor.tyre.index(char)
                temptext = self.alphabet[index]
                char = temptext
            plaintext += temptext
        return(plaintext)

class EnigmaMachine:
    def __init__(self, scrambler):
        self.scrambler = scrambler
    
    def rotate(self):
        self.scrambler.rotate()

    def encrypt(self, plaintext):
        return(self.scrambler.encrypt(plaintext))
    
    def decrypt(self, ciphertext):
        return(self.scrambler.decrypt(ciphertext))