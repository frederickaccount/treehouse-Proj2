import string

from ciphers import Cipher


class KeywordCipher(Cipher):
    """Provides encryption and decryption of Keyword Ciphers.
    An alphabet is formed replacing the first letters of the English
    alphabet with the order of first appearance of the keyword's letters,
    followed by the remaining letters of the alphabet in typical orderself.
    Encryption takes the index values of text in the English alphabet and
    returns the characters with those values in the keyword alphabet,
    decryption takes the index values of the letters
    in the keyword alphabet and returns the characters with those
    values in the English alphabet.
    """

    def __init__(self):
        """On init creates a list of the uppercase letters of the alphabet,
        takes in the keyword, and creates the encrypted alphabet
        """
        self.ALPHABET = string.ascii_uppercase
        self.keyword = self.input_keyword()
        self.keyword_alphabet = self.create_encrypted_alphabet()

    def input_keyword(self):
        """Gets keyword input from user"""
        keyword = input("\nPlease enter the Keyword:  ")
        return keyword

    def create_encrypted_alphabet(self):
        """Reorganizes the alphabet so that the letters of the keyword
        in the order of first appearance are the start of the
        alphabet followed by the rest of the letters in
        their regular order. This alphabet is returned.
        """
        keyword_alphabet = []

        for char in self.keyword.upper():
            if char in keyword_alphabet:
                pass
            else:
                keyword_alphabet.append(char)
        for char in self.ALPHABET:
            if char in keyword_alphabet:
                pass
            else:
                keyword_alphabet.append(char)
        return keyword_alphabet

    def encrypt(self, text):
        """Uses the alphabet created with the keyword to encrypt
        the text into uppercase letters. The letters are
        interpreted as numeric values and translated to
        the same vaues in the keyword alphabet
        which is returned.
        """
        output = []
        print(len(self.keyword_alphabet))
        text = text.upper()
# Goes through each char in the text and encrypts it if it's found in ALPHABET,
# or just drops it in if it is not in the list.
        for char in text:
            try:
                index = self.ALPHABET.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.keyword_alphabet[index])
        return ''.join(output)

    def decrypt(self, text):
        """Uses the alphabet created with the keyword to
        decrypt the text.  Interpretting it as a series
        of numeric values and translating it from the
        keyword alphabet to the English alphabet which
        is returned.
        """
        output = []
        self.create_encrypted_alphabet()
        text = text.upper()
# Goes through each char in the text and decrypts it if it's found in ALPHABET,
# or just drops it in if it is not in the list.
        for char in text:
            try:
                index = self.keyword_alphabet.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.ALPHABET[index])
        return ''.join(output)
