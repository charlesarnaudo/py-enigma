import enigma_machine

if __name__ == '__main__':
    # Make Rotors
    # rot0 = enigma_machine.Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'W')
    # rot1 = enigma_machine.Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'X')
    # rot2 = enigma_machine.Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'X')

    rot0 = enigma_machine.Rotor('CABD', 'X')
    rot1 = enigma_machine.Rotor('BACD', 'X')
    rot2 = enigma_machine.Rotor('DBAC', 'X')

    # Make scrambler
    scrambler = enigma_machine.Scrambler()
    scrambler.add_rotor(rot0)
    scrambler.add_rotor(rot1)
    scrambler.add_rotor(rot2)

    # Put machine together
    machine = enigma_machine.EnigmaMachine(scrambler)

    print("Welcome to the Enigma Machine!\n")
    plaintext = input("Enter text to encrypt:\n")
    print("\n")
    
    ciphertext = machine.encrypt(plaintext)
    print("Cipher: " + ciphertext)
    decrypted = machine.decrypt(ciphertext)
    print("Decrypted Cipher: " + decrypted + "\n")
    
