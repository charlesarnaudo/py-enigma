import machine

if __name__ == '__main__':
    print("\n")
    enigma = machine.EnigmaMachine()
    # enigma.print_current_state()
    print("\n")
    plaintext = input("Enter text to encrypt\n")
    ciphertext = enigma.encrypt(plaintext)
    print("\nCipher: " + ciphertext)
    decrypt = enigma.decrypt(ciphertext)
    print("Decrypted: " + decrypt + "\n")
