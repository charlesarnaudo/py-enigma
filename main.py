import machine

if __name__ == '__main__':
    enigma = machine.EnigmaMachine()
    plaintext = input("Enter text to encode\n")
    enigma.encode(plaintext)