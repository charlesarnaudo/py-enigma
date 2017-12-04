import enigma_machine

if __name__ == '__main__':
    # Make Rotors
    rot0 = enigma_machine.Rotor('CABD', 'W')
    rot1 = enigma_machine.Rotor('BACD', 'X')
    rot2 = enigma_machine.Rotor('DBAC', 'X')

    # Make scrambler
    scrambler = enigma_machine.Scrambler()
    scrambler.add_rotor(rot0)
    scrambler.add_rotor(rot1)
    scrambler.add_rotor(rot2)

    # Put machine together
    machine = enigma_machine.EnigmaMachine(scrambler)

    plaintext = input("Text to encrypt\n")
    cipher = machine.encrypt(plaintext)
    print(cipher + "\n")
    uncipher = machine.decrypt(cipher)
    print(uncipher)