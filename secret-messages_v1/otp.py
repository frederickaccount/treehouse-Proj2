import string

from ciphers import Cipher


class OneTimePad(Cipher):

    """Provides an extra layer of encryption of decryption on top of whatever
    cipher is selected.  Encrypts the encrypted output of whatever cipher
    was called, and then is decryted before being passed to the relevant
    decryption cipher.
    For encryption:
    Takes in a one time pad message which is at
    least as long as the nearest multiple of 5 greater than or equal
    to the length of the message. Uses the index values of the
    letters in the pad as modular offsets for each character
    of the message and returns 5 letter blocks with the encrypted message.
    For decryption:
    Uses the provided pad to modularly offset the encrypted message
    provided.
    """

    def __init__(self):
        """OneTimePad is initialzied with two alphabets containing
        all characters that can be encrypted or decrypted.
        This pad contains uppercase letters, symbols,  and digits although
        the 3 ciphers  don't otherwise use digits or symbols.
        In order to disguise spaces one alphabet is used containing a space
        and another has an arbitrary + symbol.
        """
        self.CHARS = string.ascii_uppercase
        self.CHARS += "0123456789"
        self.CHARS += "!@#$%^&*()/"
        self.NO_SPACE_CHARS = self.CHARS
# NO_SPACE_CHARS and CHARS differ only in their last element
# NO_SPACE_CHARS has a + and CHARS has a space
        self.NO_SPACE_CHARS += "+"
        self.CHARS += " "

    def encrypt(self, text, pad):
        """Sets the block size of the text blocks to be returned
        at 5.  Adds padding spaces which will be encrypted
        if the message length is not divisible by 5.
        Modularly offsets the message values using the pad.
        Spaces in the character list are replaced with +
        symbols so that they will not appear in encrypted messages.
        """
# BLOCK_SIZE will be the length of text blocks that are output.
        BLOCK_SIZE = 5
        blocked_encrypted_list = []
        msg_as_nums = []
        pad_as_nums = []
        encrypted_as_nums = []
        encrypted_chars = []
        whole_encrypted_msg = []
        text = text.upper()
# Check if padding is required, if so pad with spaces
        if (len(text) % BLOCK_SIZE != 0):
            padding = (BLOCK_SIZE - (len(text) % BLOCK_SIZE))
            text += (" " * padding)
# Get indexes of message
        for char in text:
            msg_as_nums.append(self.CHARS.index(char))
# Get alphabetical indexes of pad
        for char in pad:
            pad_as_nums.append(self.CHARS.index(char))

# Modularly offset message index by pad index
        for msg_num, pad_num in zip(msg_as_nums, pad_as_nums):
            encrypted_as_nums.append(
                            (((msg_num + pad_num)) % (len(self.CHARS))))
# add to list with space replaced by +
        for encrypted_num in encrypted_as_nums:
            encrypted_chars.append(self.NO_SPACE_CHARS[encrypted_num])

        whole_encrypted_msg = (''.join(encrypted_chars))
# Calculate number of 5 block words needed to display encrypted message
        num_words = ((len(whole_encrypted_msg) // BLOCK_SIZE) + 1)
# Place 5 letter blocks of encrypted message into  list
        for block in range(num_words):
            blocked_encrypted_list.append(
                            (whole_encrypted_msg[(block*5):((block*5) + 5)]))

        blocked_encrypted_msg = (' '.join(blocked_encrypted_list))

        return (blocked_encrypted_msg)

    def decrypt(self, text, pad):
        """Decrypts messages using provided pad to reverse the modular
        that occured during encryption. Restores the spaces that
        had been replaced with + symbols during encryption.
        """
        text_as_words = []
        msg_as_nums = []
        pad_as_nums = []
        decrypted_as_nums = []
        decrypted_chars = []
        text_as_words = (text.split())
        text_block = ("".join(text_as_words))
# Get indexes of message, spaces are replaced with +
        for char in text_block:
            msg_as_nums.append(self.NO_SPACE_CHARS.index(char))
# Get indexes of pad
        for char in pad:
            pad_as_nums.append(self.CHARS.index(char))

# Modularly offset message index by pad index
        for msg_num, pad_num in zip(msg_as_nums, pad_as_nums):
            decrypted_as_nums.append(
                                (((msg_num - pad_num)) % (len(self.CHARS))))
# Prepare the output using the list which contains spaces
        for decrypted_num in decrypted_as_nums:
            decrypted_chars.append(self.CHARS[decrypted_num])

        decrypted_message = (''.join(decrypted_chars))

        return (decrypted_message)
