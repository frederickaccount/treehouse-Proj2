import string

from ciphers import Cipher


class Atbash(Cipher):
    """
    Takes index values of characters in text to encrypt and translates them
    into a reversed alphabet in encryption, works backwards in
    decryption.
    """

    def __init__(self):
        """
        Initializes by creating a regular and reversed alphabet.
        """
        self.ALPHABET = string.ascii_uppercase
# Creates list with a reversed alphabet
        self.REVERSED_ALPHABET = self.ALPHABET[::-1]

    def encrypt(self, text):
        """
        Returns upper case text encrypted by having the
        index values of the provided plaintext placed in a reversed
        alphabet position.
        """
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.ALPHABET.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.REVERSED_ALPHABET[index])
        return ''.join(output)

    def decrypt(self, text):
        """
        Takes in cipher text, and if that text has been encrypted using
        a reversed alphabet it will translate it to plaintext and return
        that.
        """
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.REVERSED_ALPHABET.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.ALPHABET[index])
        return ''.join(output)
