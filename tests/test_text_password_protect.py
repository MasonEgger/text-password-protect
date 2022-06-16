#!/usr/bin/env python

"""Tests for `text_password_protect` package."""

import pytest


from text_password_protect import TextPasswordProtect
from cryptography.fernet import InvalidToken

def test_encrypt_decrypt_success():

    test_text = "Hello There"
    test_password = "Mason"
    tpp = TextPasswordProtect(salt="xKD7prACS7MHfQU7")
    ciphertext = tpp.encrypt(test_text, test_password)
    plaintext = tpp.decrypt(ciphertext, test_password)
    assert test_text == plaintext

def test_encrypt_decrypt_different_password():

    test_text = "Hello There"
    test_password = "Mason"
    tpp = TextPasswordProtect(salt="xKD7prACS7MHfQU7")
    ciphertext = tpp.encrypt(test_text, test_password)
    with pytest.raises(InvalidToken):
        plaintext = tpp.decrypt(ciphertext, "stas")
    