#!/usr/bin/env python3
""" password encryption module
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Implement a hash_password function that expects
    one string argument name password and returns a salted,
    """
    encrypt = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return encrypt


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Implement an is_valid function
    """
    validity = bcrypt.checkpw(password.encode('utf-8'), hashed_password)
    return validity
