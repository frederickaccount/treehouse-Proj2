from affine import Affine
from atbash import Atbash
from keyword_cipher import KeywordCipher
from otp import OneTimePad


class CipherSelection:
    """
    Collects information required by all available ciphers, allows user to
    select a cipher, and returns the requested encrypted or decrypted message
    utilizing a one time pad. Output ciphertext is in capital letters and
    output plain text is in lowercase letters.  The ciphers only allow for
    for case insensitive english letters.
    """

    def __init__(self, crypt, cipher_choice, otp, message):
        """
        Initializes by creating the values requred by all ciphers which are
        available.  These values are given by using a classmethod.
        """
        self.crypt = crypt
        self.cipher_choice = cipher_choice
        self.otp = otp
        self.message = message

    @classmethod
    def choose_cipher(cls):
        """
        classmethod decorator is used to allow this method to be called
        before providing values required for initialization. This method
        asks the user to encrypt or decrypt, which cipher they want,
        their message to encrypt, and their one time pad.
        The one time pad must be as long as the closest greater than
        or equal to multiple of 5 compared to the length of the
        message.
        """
        while True:

            crypt = input("Would you like to encrypt or decrypt?").lower()
            print(crypt)
            if (crypt != "encrypt") and (crypt != "decrypt"):
                crypt = 0
                print("Invalid Selection")
            else:
                break

        while True:

            cipher_choice = input("Select Cipher: \n"
                                  "A) Affine\n"
                                  "B) Atbash\n"
                                  "C) Keyword\n"
                                  ).lower()

            if cipher_choice == ("a" or "a)" or "affine"):
                cipher_choice = "affine"
                break
            elif cipher_choice == ("b" or "b)" or "atbash"):
                cipher_choice = "atbash"
                break
            elif cipher_choice == ("c" or "c)" or "keyword"):
                cipher_choice = "keyword"
                break

            else:
                print("Invalid Selection")
        while True:
            message = input("Input your message: ")
            if (len(message) >= 1):
                break
            else:
                print("Invalid Message")
        while True:
            otp = input("Enter one time pad: ")
            if crypt == "encrypt" or crypt == "e":
                if (len(message) % 5):
                    otp_length = (len(message) + (5 - (len(message) % 5)))
                else:
                    otp_length = (len(message))
                if len(otp) >= otp_length:
                    break
                else:
                    print("otp for this message must be "
                          "{} characters long".format(otp_length))
            else:
                break
        return cls(crypt, cipher_choice, otp, message)

    def call_cipher(self):
        """
        Calls the cipher selected by the user.
        Encrypts using the selected cipher
        then encrypts that cipher text with a one time pad.  Decrypts the otp
        first then passes the result to the selected cipher for decryption.
        Cipher text is output in uppercase, decrypted plain text is output
        in lowercase.
        """
        if self.cipher_choice == "affine":

            if self.crypt == "encrypt":
                encrypted_message = Affine().encrypt(self.message.upper())
                otp_encrypted = OneTimePad().encrypt(
                                encrypted_message, self.otp.upper())
                return (otp_encrypted)

            elif self.crypt == "decrypt":
                otp_decrypted = OneTimePad().decrypt(
                                    self.message.upper(), self.otp.upper())
                decrypted_message = Affine().decrypt(otp_decrypted)
                return (decrypted_message.lower())

        elif self.cipher_choice == "atbash":

            if self.crypt == "encrypt":
                encrypted_message = Atbash().encrypt(self.message.upper())
                otp_encrypted = OneTimePad().encrypt(
                                encrypted_message, self.otp.upper())
                return (otp_encrypted)

            elif self.crypt == "decrypt":
                otp_decrypted = OneTimePad().decrypt(
                                    self.message.upper(), self.otp.upper())
                decrypted_message = Atbash().decrypt(otp_decrypted)
                return (decrypted_message.lower())

        elif self.cipher_choice == "keyword":

            if self.crypt == "encrypt":
                encrypted_message = KeywordCipher().encrypt(self.message.upper())
                otp_encrypted = OneTimePad().encrypt(
                                encrypted_message, self.otp.upper())
                return (otp_encrypted)

            elif self.crypt == "decrypt":
                otp_decrypted = OneTimePad().decrypt(
                                    self.message.upper(), self.otp.upper())
                decrypted_message = KeywordCipher().decrypt(otp_decrypted)
                return (decrypted_message.lower())


# Call the cipher program and output the result
cipher = CipherSelection.choose_cipher()
print(cipher.call_cipher())
