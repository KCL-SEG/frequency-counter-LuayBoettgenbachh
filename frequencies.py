"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    stringItems = []

    # Convert items in the array to strings
    for item in items:
        itemToAppend = str(item)
        stringItems.append(itemToAppend)
    
    # Remove duplicates from the stringItems array
    stringItems = list(dict.fromkeys(stringItems))




    return frequencies
