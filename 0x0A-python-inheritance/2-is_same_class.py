#!/usr/bin/bash
"""checks for instance"""


def is_same_class(obj, a_class):
    """checks for obj inctance
    Retrun:
        true
        false
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
