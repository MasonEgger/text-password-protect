=====
Usage
=====

To use Text Password Protect in a project::

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
