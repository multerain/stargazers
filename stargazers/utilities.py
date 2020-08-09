"""Stargazer CLI Utilities."""


def input_to_list(str_input):  # pylint: disable=inconsistent-return-statements
    """Convert input comma or space separated string to a list.

    :param str str_input: Input string from CLI
    """
    comma_split = str_input.split(',')
    space_split = str_input.split()

    # If we have empty splits, return None
    if comma_split == [''] and space_split == []:  # pylint: disable=no-else-return
        return None
    # If both are len 1 we were likely given only a single entry
    elif len(comma_split) == 1 and len(space_split) == 1:
        return space_split
    # If one is len 1 and the other is not, choose that one
    # Except that len(''.split(',')) = [''] has len 1 so make sure to check
    elif (len(comma_split) == 1 or comma_split == ['']) and len(space_split) != 1:
        return space_split
    elif len(comma_split) != 1 and len(space_split) == 1:
        return comma_split
