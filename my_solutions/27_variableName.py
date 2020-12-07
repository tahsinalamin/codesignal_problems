"""
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

Example

For name = "var_1__Int", the output should be
variableName(name) = true;
For name = "qq-q", the output should be
variableName(name) = false;
"""


def variableName(name):
    s="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm_"
    d="0123456789"
    s=list(s)
    d=list(d)
    
    for i in range(len(list(name))):
        if i==0 and name[i] in d:
            return False
        if name[i] not in s and name[i] not in d:
            return False
    return True

