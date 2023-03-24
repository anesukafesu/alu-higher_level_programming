#!/usr/bin/python3
"""
Implements append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends a specified string after every search_string
    in the specified filename

    Args:
        - filename (str)
        - search_string (str)
        - new_string (str)
    Returns:
        - None
    """
    with open(filename, "w+") as f:
        lines = f.readlines()
        append_after = []
        offset = 0

        for i in range(len(lines)):
            if lines[i] == search_string:
                append_after.append(i)


        for appendage_point in append_after:
            lines.insert(appendage_point + offset, new_string)
            offset += 1

        f.writelines(lines)
