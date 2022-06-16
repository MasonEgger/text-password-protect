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


def test_sha256hex():
    test_text = "Hello There"
    test_sha256hex = "abf5dacd019d2229174f1daa9e62852554ab1b955fe6ae6bbbb214bab611f6f5"
    tpp = TextPasswordProtect()
    hex = tpp.sha256hex(test_text)

    assert test_sha256hex == hex
