############ CHECK FUNCTIONS ############

def lenCheck(length: str) -> tuple:
    """
    Checks whether provided length for password is in range 8-20.

    Args:
        length: Length of password requested by user.

    Returns:
        Tuple consisting of:
         - True if length in range, False otherwise.
         - None if True, error message string if False.
    """

    length = int(length)
    if length in range(8,21):
        return (True, None)
    elif length < 8:
        message = f"Minimum length of password must be 8. You entered {length}. Please try again!"
    else:
        message = f"Maximum length of password can be 20. You entered {length}. Please try again!"
    return (False, message)


def symbCheck(exclude: str) -> tuple:
    """
    Check whether provided string of symbols to exclude is acceptable.

    Args:
        exclude: String of symbols that the user doesn't wanat to include in password.

    Returns:
        Tuple consisting of :
         - True if acceptable, False otherwise.
         - None if True, error message string otherwise.
    """


    symbols = '!@#$%^&~'
    for char in exclude:
        if char not in symbols:
            return (False, f"Entered 'exclude' string has characters other than those used for generating passwords ({symbols}). Please try again.")
    return (True, None)

#########################################
