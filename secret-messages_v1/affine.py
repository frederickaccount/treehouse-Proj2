import string

from ciphers import Cipher
# gcd to find coprimes
from math import gcd


class Affine(Cipher):
    """
        Asks user for a multiplier (which has a multiplicative inverse) for
        the length of the English alphabet, as well as an offset which is
        be modulated to that same length.  If encrypting provides the user
        with the multiplicative inverse that they need to decrypt.
        Encrypts and decrypts letters using their index values
        (0 - 26) and the following formulas:
        Encrypt:multiplier * index) + offset) % alphabet length
        Decrypt: Multiplicative Inverse * (index - offset) % alphabet length
    """

    def __init__(self):
        """
        Initializes by creating a list of uppercase letters, an integer with
        its length, and a list of the coprimes less than that integer for
        that integer.
        """
        self.ALPHABET = string.ascii_uppercase
        self.LEN = len(self.ALPHABET)
# Finds the given coprimes for the given alphabet length
        self.coprimes = []
        for coprime in range(self.LEN):
            if (gcd(coprime, self.LEN) == 1):
                self.coprimes.append(coprime)

    def input_multipier_and_offset(self, multiplier, offset, encrypt):
        """
        Takes input from user for the multiplier and offset.
        Has an encrypt variable passed in to properly show required information
        for encryption (multiplicative inverse of selected multiplier)
        Leaves default values which will work if user doesnt want to choose
        their own values.
        """
# Shows viable multipliers and asks user if they want to select one
        while True:
            if encrypt is True:
                print(self.coprimes)
                multiplier_selection = input("Select a multiplier from"
                                             " the above list, or"
                                             " leave blank to default"
                                             " to 5:   ")
            else:
                multiplier_selection = input("Enter multiplicative_inverse"
                                             " to decrypt, or leave blank"
                                             " to default to 21:   ")
            if multiplier_selection:
                try:
                    multiplier_selection = int(multiplier_selection)
                except ValueError:
                    print("Input must be an integer")
# If user is encrypting they must select
                if multiplier_selection in self.coprimes:
                    multiplier = multiplier_selection
                    break
                elif encrypt is False and isinstance(
                                    multiplier_selection, int):
                    multiplier = multiplier_selection
                    break
                else:
                    print("Invalid Selection")
            else:
                break
# Let user input an offset and if so modulate within alphabet length
        while True:
            offset_selection = input("Input an offset,"
                                     " or leave blank to default to 8:   ")
            if offset_selection:
                try:
                    offset_selection = int(offset_selection) % self.LEN

                except ValueError:
                    print("Input must be an integer")

                if isinstance(offset_selection, int):
                    offset = offset_selection % self.LEN
                    break
            else:
                break
        return (multiplier, offset)

    def multiplicative_inverse_info(self, multiplier, offset):
        """
        Determines the multiplicative inverse of the multiplier
        selected by the user, and returns a message for the user
        containing the multiplier and offset they will need to
        decrypt their message.
        """
# A formula for determining what multiplicative inverse applies to the given
# multiplier and alphabet length.
        remainder = multiplier % self.LEN

        for multiplicative_inverse_check in range(self.LEN):
            if ((remainder * multiplicative_inverse_check) % self.LEN == 1):
                multiplicative_inverse = multiplicative_inverse_check

        info_for_user = ("To Decrypt this message please note"
                         "that the multiplicative inverse needed"
                         "will be {} \n".format(multiplicative_inverse) +
                         "and the offset needed"
                         "will be {} \n".format(offset))
        return (info_for_user)

    def encrypt(self, text, multiplier=5, offset=8):
        """
        Asks the user which of the 12 possible aphine cipher
        multipliers which are available for the 26 uppercase
        English letters that they would like to use.  The user may
        input any offset they wish since it will be modulated to the
        correct length. Returns the encrypted message.
        """
# Set a variable to indicate we are decrypting
        encrypt = True
# Ask the user if they wish to change the multiplier and offset
        multiplier, offset = self.input_multipier_and_offset(
                                multiplier, offset, encrypt)
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.ALPHABET.index(char)
            except ValueError:
                output.append(char)
# This step uses the encryption formula
            else:
                output.append(self.ALPHABET[(((
                        multiplier * index) + offset) % self.LEN)])

        encrypted_message = (''.join(output))
# Tell the user the multiplicative inverse they need to decrypt
        print(self.multiplicative_inverse_info(multiplier, offset))
        return (encrypted_message)

    def decrypt(self, text, multiplier=21, offset=8):
        """
        Uses the multiplicative inverse of the alphabet length and
        multiplier used in encryption along with the same offset to
        decrypt. Returns the decrypted message with the multiplier
        and offset as provided by the user.
        """
# Set a variable to indicate we are decrypting
        encrypt = False
# Ask the user if they wish to change the multiplier and offset
        multiplier, offset = self.input_multipier_and_offset(
                                multiplier, offset, encrypt)
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.ALPHABET.index(char)

            except ValueError:
                output.append(char)
# The decrypted index is found using the formula in this command
            else:
                try:
                    output.append(self.ALPHABET[(
                        multiplier * (index - offset) % self.LEN)])
                except TypeError:
                    print("Invalid Multiplicative Inverse")
        return ''.join(output)
