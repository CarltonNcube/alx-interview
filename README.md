# Project 0x04: UTF-8 Validation

In this project, we will utilize bitwise operations, understanding of the UTF-8 encoding scheme, 
and Python programming skills to validate whether a given dataset represents a valid UTF-8 encoding. 
Here’s a breakdown of the concepts and resources that will be helpful for this project:

    Bitwise operations: We'll use bitwise operations to extract and manipulate individual bits from bytes in the dataset.
    UTF-8 encoding scheme: Understanding the UTF-8 encoding scheme is crucial for decoding and validating UTF-8 encoded data.
    Python programming skills: We'll leverage Python's capabilities to implement the validation logic efficiently.

## Concepts Needed:

### Bitwise Operations in Python:

Understanding how to manipulate bits in Python, including operations like AND (&), OR (|), XOR (^), NOT (~), shifts (<<, >>).
[Python Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators)
  
### UTF-8 Encoding Scheme:

Familiarity with the UTF-8 encoding rules, including how characters are encoded into one or more bytes.
Understanding the patterns that represent a valid UTF-8 encoded character.
[UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
[Characters, Symbols, and the Unicode Miracle](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)

### Data Representation:

Understanding how to represent and work with data at the byte level.
Handling the least significant bits (LSB) of integers to simulate byte data.

### List Manipulation in Python:

Iterating through lists, accessing list elements, and understanding list comprehensions.
[Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

### Boolean Logic:

Applying logical operations to make decisions within the program.

By studying these concepts and utilizing the resources provided, you will be equipped to tackle the UTF-8 validation project, 
effectively applying bitwise operations and logical reasoning to determine the validity of UTF-8 encoded data.

## Additional Resource

### Mock Technical Interview


## Tasks

### 0. UTF-8 Validation

#### Description

Write a method that determines if a given data set represents a valid UTF-8 encoding.

#### Prototype

```python
def validUTF8(data):
    pass

Return

    True if data is a valid UTF-8 encoding, else return False

Details

    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
