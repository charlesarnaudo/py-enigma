import string
import copy

class Rotor:
    def __init__(self, tyre, tNotch):
        self.tyre = list(tyre.upper())
        self.tNotch = tNotch
        self.pos = 0
    
    def __str__(self):
        return(str(self.tyre))
    
    def getchar(self, index):
        return(self.tyre[index])

    def getindex(self, char):
        return(self.tyre.index(char))

    def rotate(self):
        self.tyre = self.tyre[-1:] + self.tyre[:-1]
"""
"""
class Scrambler:
    def __init__(self):
        self.rotors = []
        self.rotorscp = []
        self.alphabet = list(string.ascii_uppercase)
        self.nRotors = 0
    
    def add_rotor(self, rotor):
        """Add rotor to scrambler"""
        rotor.pos = self.nRotors
        self.nRotors += 1
        self.rotors.append(rotor)
        self.rotorscp = copy.deepcopy(self.rotors)

    def encrypt(self, plaintext):
        """Passes text through rotors"""
        plaintext = plaintext.replace(" ", "x")
        plaintext = plaintext.upper() # Enigma only used upper case
        ciphertext = ""
        for char in plaintext:
            print(char + "\n")
            for rotor in self.rotors:
                index = self.alphabet.index(char)
                print(char + " = " + rotor.getchar(index))
                char = rotor.getchar(index) # char is changed to pass through to next rotor
                print(rotor)
                print("\n")
                if rotor.pos == 0:
                    rotor.rotate()
            ciphertext += char
            print("\n")
        return(ciphertext)

    def decrypt(self, ciphertext):
        """Passes text through rotors backwards to decrypt"""
        self.reset()
        plaintext = ""
        for char in ciphertext:
            print(char + "\n")
            for rotor in reversed(self.rotors):
                index = rotor.getindex(char)
                print(char + " = " + self.alphabet[index])
                char = self.alphabet[index]
                print(rotor)
                print("\n")
                if rotor.pos == 0:
                    rotor.rotate()
            plaintext += char
            print("\n")

        return(plaintext)

    def reset(self):
        """Reset scrambler to inital configuration"""
        self.rotors = self.rotorscp

    def print_config(self):
        """Print current position of rotors"""
        for rotor in self.rotors:
            print(rotor)

    # def decrypt(self, ciphertext):

class EnigmaMachine:
    def __init__(self, scrambler):
        self.scrambler = scrambler
    
    def rotate(self):
        self.scrambler.rotate()

    def encrypt(self, plaintext):
        return(self.scrambler.encrypt(plaintext))
    
    def decrypt(self, ciphertext):
        return(self.scrambler.decrypt(ciphertext))

    def print_config(self):
        self.scrambler.print_config()
