#!/usr/bin/env python3

def validate_user(username, minlen):
    assert type(username) == str, "username must be a string"  #
    if minlen <1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        return False  #could be misleading if minlen is not proper.  So 
    if not username.isalnum():
        return False  #invalid
    return True

