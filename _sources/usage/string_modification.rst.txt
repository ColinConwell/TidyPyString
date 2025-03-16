Modification
============

This section covers functions for modifying and transforming string content.


----------

Replace all occurrences of a pattern in a string.

.. code-block:: python

    import pandas as pd
    from tidystring import str_replace

    # Basic replacement
    str_replace("hello world", "o", "X")  # "hellX wXrld"

    # With a limited number of replacements
    str_replace("hello world", "l", "L", n=1)  # "heLlo world"

    # With regular expressions
    str_replace("hello123world", "\\d+", "")  # "helloworld"

    # With a list
    texts = ["apple", "banana", "cherry"]
    str_replace(texts, "a", "A")  # ["Apple", "bAnAnA", "cherry"]

    # With a Series
    fruits = pd.Series(["apple", "banana", "cherry"])
    str_replace(fruits, "e", "E")
    # 0    applE
    # 1    banana
    # 2    chErry
    # dtype: object


---------

Remove all occurrences of a pattern from a string.

.. code-block:: python

    from tidystring import str_remove

    # Basic usage
    str_remove("hello world", "o")  # "hell wrld"

    # With regular expressions
    str_remove("hello123world", "\\d+")  # "helloworld"

    # With a list
    emails = ["user@example.com", "admin@example.com"]
    str_remove(emails, "@example.com")  # ["user", "admin"]

    # With a Series
    data = pd.Series(["Product: A123", "Product: B456", "Product: C789"])
    str_remove(data, "Product: ")
    # 0    A123
    # 1    B456
    # 2    C789
    # dtype: object


-------

Remove whitespace from the start and end of a string.

.. code-block:: python

    from tidystring import str_trim

    # Basic usage
    str_trim("  hello  ")  # "hello"

    # With trailing whitespace
    str_trim("hello world  ")  # "hello world"

    # With leading whitespace
    str_trim("  hello world")  # "hello world"

    # With a list
    spaces = ["  left", "right  ", "  both  "]
    str_trim(spaces)  # ["left", "right", "both"]

    # With a Series
    s = pd.Series(["  data  ", " analysis ", "  science  "])
    str_trim(s)
    # 0        data
    # 1    analysis
    # 2     science
    # dtype: object


----------------

Replace all occurrences of specified dashes with spaces.

.. code-block:: python

    from tidystring import str_dash_to_space

    # Basic usage
    str_dash_to_space("hello-world")  # "hello world"

    # With underscores
    str_dash_to_space("hello_world")  # "hello world"

    # With custom dashes
    str_dash_to_space("hello.world", dashes=["."])  # "hello world"

    # With a list
    texts = ["python-code", "data_analysis"]
    str_dash_to_space(texts)  # ["python code", "data analysis"]

    # With a Series
    s = pd.Series(["machine-learning", "deep_learning"])
    str_dash_to_space(s)
    # 0    machine learning
    # 1     deep learning
