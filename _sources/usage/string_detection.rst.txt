Detection
=========

This section covers functions that detect patterns in strings and return boolean values.


---------

Detect the presence of a pattern in a string.

.. code-block:: python

    import pandas as pd
    from tidystring import str_detect

    # Basic usage
    str_detect("hello world", "world")  # True
    str_detect("hello world", "python")  # False

    # With regular expressions
    str_detect("hello123", "\\d+")  # True (contains digits)
    str_detect("abc", "[0-9]")  # False (no digits)

    # With a list of strings
    texts = ["apple", "banana", "cherry"]
    str_detect(texts, "a")  # [True, True, False]

    # With a pandas Series
    series = pd.Series(["dog", "cat", "mouse"])
    str_detect(series, "o")
    # 0     True
    # 1    False
    # 2     True
    # dtype: bool


-------------

Check if a string starts with a specific pattern.

.. code-block:: python

    from tidystring import str_startswith

    # Basic usage
    str_startswith("hello world", "hello")  # True
    str_startswith("hello world", "world")  # False

    # With multiple strings
    words = ["apple", "banana", "pear"]
    str_startswith(words, "a")  # [True, False, False]

    # With a Series
    fruits = pd.Series(["apple", "banana", "orange"])
    str_startswith(fruits, "b")
    # 0    False
    # 1     True
    # 2    False
    # dtype: bool


-----------

Check if a string ends with a specific pattern.

.. code-block:: python

    from tidystring import str_endswith

    # Basic usage
    str_endswith("hello world", "world")  # True
    str_endswith("hello world", "hello")  # False

    # With multiple strings
    files = ["document.txt", "image.jpg", "data.csv"]
    str_endswith(files, ".txt")  # [True, False, False]

    # With a Series
    extensions = pd.Series(["file.txt", "image.png", "data.csv"])
    str_endswith(extensions, ".csv")
    # 0    False
    # 1    False
    # 2     True
    # dtype: bool


--------

Count occurrences of a pattern in a string.

.. code-block:: python

    from tidystring import str_count

    # Basic usage
    str_count("hello world", "l")  # 3
    str_count("mississippi", "i")  # 4

    # With regular expressions
    str_count("a1b2c3", "\\d")  # 3 (three digits)

    # With a list
    words = ["apple", "banana", "papaya"]
    str_count(words, "a")  # [1, 3, 3]

    # With a Series
    fruits = pd.Series(["apple", "banana", "pineapple"])
    str_count(fruits, "p")
    # 0    1
    # 1    0
    # 2    3
