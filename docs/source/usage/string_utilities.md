# Key Utilities

This section covers utility functions for working with strings.

---

Concatenate strings with a separator.

```python
import pandas as pd
from tidystring import str_concat

# Basic usage with strings
str_concat("hello", "world")  # "hello_world"

# With custom separator
str_concat("hello", "world", sep="-")  # "hello-world"

# With multiple strings
str_concat("a", "b", "c", sep=".")  # "a.b.c"

# With Series
s1 = pd.Series(["a", "b"])
s2 = pd.Series(["c", "d"])
str_concat(s1, s2)
# 0    a_c
# 1    b_d
# dtype: object

# With DataFrame columns
df = pd.DataFrame({"first": ["John", "Jane"], "last": ["Doe", "Smith"]})
str_concat(df, "first", "last", sep=" ")
# 0     John Doe
# 1    Jane Smith
# dtype: object
```

---

Apply a function to each regex match in string.

```python
from tidystring import str_search_apply

# Apply uppercase to all words
str_search_apply("hello world", "\\w+", lambda x: x.upper())
# "HELLO WORLD"

# Double all numbers in a string
str_search_apply("a1b2c3", "\\d", lambda x: str(int(x) * 2))
# "a2b4c6"

# With a list
texts = ["apple pie", "banana bread"]
str_search_apply(texts, "\\b[a-z]", lambda x: x.upper())
# ["Apple Pie", "Banana Bread"]

# With a Series
s = pd.Series(["hello world", "python 3.9"])
str_search_apply(s, "\\d", lambda x: f"[{x}]")
# 0       hello world
# 1    python [3].[9]
# dtype: object
```

---

Change the case of text matching a pattern in string.

```python
from tidystring import str_search_recase

# Change words to uppercase
str_search_recase("hello world", "\\w+", "upper")
# "HELLO WORLD"

# Change words to lowercase
str_search_recase("Hello World", "\\w+", "lower")
# "hello world"

# Change words to title case
str_search_recase("hello world", "\\w+", "title")
# "Hello World"

# Change words to snake case
str_search_recase("helloWorld pythonCode", "\\w+", "snakecase")
# "hello_world python_code"

# Change words to camel case
str_search_recase("hello_world python_code", "\\w+", "camelcase")
# "HelloWorld PythonCode"

# With a list
words = ["helloWorld", "pythonScript"]
str_search_recase(words, "\\w+", "snakecase")
# ["hello_world", "python_script"]

# With a Series
s = pd.Series(["snake_case", "camelCase"])
str_search_recase(s, "\\w+", "title")
# 0    Snake_case
# 1     CamelCase
# dtype: object
```