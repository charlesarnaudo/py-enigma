import string

class EnigmaMachine:
    """
    Enigma machine with standard functions
    Plugboard not implemented
    """
    def __init__(self):
        # Create three rotors
        self.rotor0 = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
        self.rotor0 = list(self.rotor0)
        self.rotor1 = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
        self.rotor1 = list(self.rotor1)
        self.rotor2 = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
        self.rotor2 = list(self.rotor2)
        # Group rotors together
        self.rotors = []
        self.rotors += self.rotor0, self.rotor1, self.rotor2
        # Copy of initial rotor config
        self.rotors_copy = []
        self.rotors_copy += self.rotor0, self.rotor1, self.rotor2

        # Create alphabet array, for index
        self.alphabet = list(string.ascii_uppercase)
        
    def rotate(self):
        """Rotate rotor right by one"""
        self.rotors[0] = self.rotors[0][-1:] + self.rotors[0][:-1]

    def reset(self):
        """Reset machine to inital config"""
        self.rotors = self.rotors_copy

    def encrypt(self, plaintext):
        """Encrypt text"""
        plaintext = plaintext.replace(" ", "x")
        plaintext = plaintext.upper()
        ciphertext = ""
        tempcipher = ""
        for char in plaintext:
            for rotor in self.rotors:
                index = self.alphabet.index(char)
                tempcipher = rotor[index]
                char = tempcipher
            ciphertext += tempcipher
            self.rotate()
        return(ciphertext)

    def decrypt(self, ciphertext):
        """Decrypt text"""
        self.reset()
        plaintext = ""
        temptext = ""
        for char in ciphertext:
            for rotor in reversed(self.rotors):
                index = rotor.index(char)
                temptext = self.alphabet[index]
                # print(temptext)
                # print(rotor)
                # print("\n")
                char = temptext
            plaintext += temptext
            self.rotate()
        return(plaintext)

    def print_current_state(self):
        """Print current configuration of machine"""
        print("Current configuration of rotors")
        print(self.rotors)
        print("\n")
