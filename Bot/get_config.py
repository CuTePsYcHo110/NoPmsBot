#!/usr/bin/env python3

""" wrapper for getting the credentials """

import os


def get_config(name: str, d_v=None, should_prompt=False):
    """ accepts one mandatory variable
    and prompts for the value, if not available """
    val = os.environ.get(name, d_v)
    if not val and should_prompt:
        try:
            val = input(f"enter {name}'s value: ")
        except EOFError:
            val = d_v
        print("\n")
    return val
