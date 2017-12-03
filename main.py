import machine

if __name__ == '__main__':
    enigma = machine.EnigmaMachine()
    print("\n")
    enigma.print_current_state()
    plaintext = input("Enter text to encode\n")
    ciphertext = enigma.encrypt(plaintext)
    print("Cipher: " + ciphertext + "\n")
   
    enigma.print_current_state()
    enigma.reset()
   
    decrypt = enigma.encrypt(ciphertext)
    print("Decrypted: " + decrypt)
