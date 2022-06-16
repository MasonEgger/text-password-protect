# Text Password Protect
_Protect any text with your own password._

Ever want a simple library to encrypt some text with a password? Well here it is.
This is a great library for building quick One Time Secret apps in Python

### Warning
   Use this package at your own discretion. There is no guarantee about the strength
   of the encryption.

## Usage

To install run
```bash
pip install text-password-protect
```

In code:

```python
    from text_password_protect import TextPasswordProtect
    
    test_text = "Hello There"
    test_password = "General Kenobi"

    # Create an instance of the class.
    # You can set a salt an initialization time, change the salt with the
    # set_salt method, or set TPPSALT as an environment variable, which will
    # be read at initialization time.
    tpp = TextPasswordProtect(salt="BAD_SALT_DO_NOT_USE!")

    # Encrypt your message
    ciphertext = tpp.encrypt(test_text, test_password)

    # Ciphertext is of type bytes
    print(ciphertext)

    # Decrypt ciphertext
    plaintext = tpp.decrypt(ciphertext, test_password)

    print(plaintext)
```


## License
* Free software: MIT license
* Documentation: https://text-password-protect.readthedocs.io.



