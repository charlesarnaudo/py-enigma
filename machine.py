import sys
import math
import string
import pprint

class EnigmaMachine:
    """
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
        print("Reset")
        print(self.rotors)
        print("\n")
    
    def encrypt(self, plaintext):
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

    def print_current_state(self):
        """Print current configuration of machine"""
        print("Current configuration of rotors")
        print(self.rotors)
        print("\n")
