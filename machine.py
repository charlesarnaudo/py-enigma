import sys
import math
from collections import deque


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
        # Group rotors together]
        self.rotors = []
        self.rotors += self.rotor0, self.rotor1, self.rotor2
        # Copy of initial rotor config
        self.rotors_copy = self.rotors
    
    def rotate(self, l, n):
        return l[-n:] + l[:-n]
    
    def encode(self, plaintext):
        plaintext = plaintext.upper()
        """Run input through rotors"""
        print(plaintext)
        self.rotor0 = self.rotate(self.rotor0, 1)
        print(self.rotor0)
            
   

    def print_current_config(self):
        """Print current configuration of machine"""
        print(self.rotors)
        print(self.rotors[0].index('K'))
