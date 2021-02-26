"""
Knowing whether a person is young, beautiful and loved, find out if they contradict Mary's belief.

A person contradicts Mary's belief if one of the following statements is true:

they are young and beautiful but not loved;
they are loved but not young or not beautiful.
Example

For young = true, beautiful = true, and loved = true, the output should be
willYou(young, beautiful, loved) = false.
"""

def willYou(young, beautiful, loved):
    if young and beautiful and not loved:
        return True
    if loved and (not young or not beautiful):
        return True
    return False

