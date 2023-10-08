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
  cleanItems = list(dict.fromkeys(stringItems))

  # Add to the dictionary
  for string in cleanItems:
    value = stringItems.count(string)
    frequencies[string] = value

  return frequencies