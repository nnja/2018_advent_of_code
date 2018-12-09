"""
AoC helper method and utilities
"""

import os
import re
from collections import Counter, defaultdict, namedtuple
from datetime import datetime
from itertools import combinations
from math import floor
from operator import itemgetter
from pathlib import Path
from pprint import pprint as pp

import requests

DEBUG = True


def log(*s):
    """
    Silly little shorthand logger, to avoid
    cluttering up output.

    Don't use anything like this in real code.
    Use the logging module instead.
    """
    if DEBUG:
        print(*s)


def local_cache(func):
    """
    Decorator to cache the input files for each day 
    to the local file system,
    to avoid hitting the server multiple times.
    """
    def function_wrapper(*args, **kwargs):
        day = args[0]
        should_split = kwargs.get('split', True)

        filename = Path(f"inputs/{day}.txt")

        content = ""

        if filename.is_file():
            with filename.open() as f:
                content = f.read()
        else:
            content = func(day)
            filename.write_text(content)

        return content.split("\n")[:-1] if should_split else content
    return function_wrapper


@local_cache
def get_data(day, split=True):
    """
    Grab the input for each day from the AoC server.
    Session cookie needs to be set with a valid key,
    available after logging in.
    """
    session_id = os.environ['AOC_SESSION_KEY']
    cookie = {'session': session_id}

    url = f"https://adventofcode.com/2018/day/{day}/input"
    r = requests.get(url, cookies=cookie)

    r.raise_for_status()

    return r.text


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def run_tests(func, test_inputs, delim="\n"):
    """
    Helper function to quickly run small test scenarios
    """
    for test in test_inputs:
        test_input, expected_result = test

        log("Testing...", test)

        if type(test_input) == str and delim:
            test_input = list(filter(lambda x: x != '', test_input.split(delim)))

        result = func(test_input)

        log("expected ", expected_result, " result was: ", result)

        assert result == expected_result
