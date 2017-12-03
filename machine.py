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
    
    def rotate(self, l):
        """Rotate rotor right by one"""
        return l[-1:] + l[:-1]

    def reset(self):
        """Reset machine to inital config"""
        self.rotors = self.rotors_copy
        print("Reset")
        print(self.rotors)
        print("\n")
    
    def encrypt(self, plaintext):
        """Run input through rotors, and encode"""
        plaintext = plaintext.upper()
        ciphertext = ""
        tempcipher = ""
        for char in plaintext:
            index = self.alphabet.index(char)
            self.rotate(self.rotors[0])
            for rotor in self.rotors:
                tempcipher = rotor[index]
                index = self.alphabet.index(tempcipher)
            ciphertext += tempcipher
        return(ciphertext)

    def print_current_state(self):
        """Print current configuration of machine"""
        print("Current configuration of rotors")
        print(self.rotors)
        print("\n")
