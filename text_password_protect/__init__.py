"""Top-level package for Text Password Protect."""

__author__ = """Mason Egger"""
__email__ = "mason@masonegger.com"
__version__ = "0.1.0"

"""Main module."""
import base64, os, socket
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class TextPasswordProtect:
    """This class allows for the encryption and decryption of messages, each
    message being encrypted with a password.
    """

    def __init__(self, salt=None):
        """Constructor method"""
        if os.getenv("TPPSALT", None) is None:
            self.__salt__ = str.encode(socket.gethostname())
        else:
            self.__salt__ = str.encode(os.getenv("TPPSALT"))

    def set_salt(self, salt):
        """
        Set the salt of the class. Will encode to bytes.

        :param salt: The salt that will be used in the encryption/decryption process
        :type salt: str
        """
        self.__salt__ = str.encode(salt)

    def encrypt(
        self,
        plaintext: str,
        password: str,
        algorithm=hashes.SHA256,
        length: int = 32,
        iterations: int = 100000,
    ) -> bytes:
        """
        Encrypt a plaintext str with a password.

        :param plaintext: Plaintext representation of the message to encrypt
        :type plaintext: str
        :param password: The password to encrypt the string with
        :type password: str
        """
        password_provided = password.encode()
        kdf = PBKDF2HMAC(
            algorithm=algorithm(),
            length=length,
            salt=self.__salt__,
            iterations=iterations,
            backend=default_backend(),
        )
        key = base64.urlsafe_b64encode(
            kdf.derive(password_provided)
        )  # Can only use kdf once
        f = Fernet(key)

        # encrypt the message
        ciphertext = f.encrypt(plaintext.encode("utf-8"))

        return ciphertext

    def decrypt(
        self,
        ciphertext: bytes,
        password: str,
        algorithm=hashes.SHA256,
        length: int = 32,
        iterations: int = 100000,
    ) -> str:
        """
        Decrypt an encrypted ciphertext str with a password.

        :param ciphertext: Bytes representation of the ciphertext to decrypt
        :type ciphertext: bytes
        :param password: The password to deencrypt the string with
        :type password: str
        """
        password_provided = password.encode()  # Convert to type bytes
        kdf = PBKDF2HMAC(
            algorithm=algorithm(),
            length=length,
            salt=self.__salt__,
            iterations=iterations,
            backend=default_backend(),
        )
        key = base64.urlsafe_b64encode(
            kdf.derive(password_provided)
        )  # Can only use kdf once
        f = Fernet(key)
        decrypted_message = f.decrypt(ciphertext)

        return decrypted_message.decode("utf-8")
