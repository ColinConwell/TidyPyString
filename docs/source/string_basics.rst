String Basics
=============

This section covers basic string operations such as getting the length of strings, padding strings, 
and creating duplicated strings.

str_length
----------

Get the length of a string.

.. code-block:: python

    import pandas as pd
    from tidystring import str_length

    # Basic usage with a string
    str_length("hello")  # 5

    # With a list of strings
    str_length(["hello", "world", "tidystring"])  # [5, 5, 10]

    # With a pandas Series
    series = pd.Series(["apple", "banana", "cherry"])
    str_length(series)
    # 0    5
    # 1    6
    # 2    6
    # dtype: int64

str_pad
-------

Pad a string to a specified width.

.. code-block:: python

    from tidystring import str_pad

    # Center padding (default)
    str_pad("hello", 10)  # "  hello   "

    # Right padding
    str_pad("hello", 10, side="right")  # "hello     "

    # Left padding
    str_pad("hello", 10, side="left")  # "     hello"

    # Custom padding character
    str_pad("hello", 10, pad="*")  # "**hello***"

    # Works with collections
    str_pad(["a", "bb", "ccc"], 5, side="right")  # ["a    ", "bb   ", "ccc  "]

str_dup
-------

Duplicate strings multiple times.

.. code-block:: python

    from tidystring import str_dup

    # Basic usage
    str_dup("abc", 3)  # "abcabcabc"

    # With a list
    str_dup(["a", "b"], 3)  # ["aaa", "bbb"]

    # With a Series
    s = pd.Series(["x", "y", "z"])
    str_dup(s, 2)
    # 0    xx
    # 1    yy
    # 2    zz
    # dtype: object

str_squish
----------

Trim whitespace from start and end, and replace all internal whitespace with a single space.

.. code-block:: python

    from tidystring import str_squish

    # Basic usage
    str_squish("  hello  world  ")  # "hello world"

    # With multiple whitespace characters
    str_squish("hello    world")  # "hello world"

    # Works with collections
    texts = ["  a  b  ", " c   d "]
    str_squish(texts)  # ["a b", "c d"]

str_wrap
--------

Wrap text to a specified width.

.. code-block:: python

    from tidystring import str_wrap

    # Basic usage
    long_text = "This is a long string that needs to be wrapped."
    str_wrap(long_text, width=20)
    # "This is a long\nstring that needs to\nbe wrapped."

    # With indentation of first line
    str_wrap("A paragraph of text.", width=20, indent=2)
    # "  A paragraph of text."

    # With indentation of subsequent lines
    str_wrap("A longer paragraph that wraps to multiple lines.", width=20, exdent=2)
    # "A longer paragraph
    #   that wraps to
    #   multiple lines."