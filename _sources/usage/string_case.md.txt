# (Re)Casing

This section covers functions for converting between different string cases.

---

Convert a string to uppercase.

```python
import pandas as pd
from tidystring import str_to_upper

# Basic usage
str_to_upper("hello")  # "HELLO"

# With mixed case
str_to_upper("Hello World")  # "HELLO WORLD"

# With a list
words = ["apple", "Banana", "CHERRY"]
str_to_upper(words)  # ["APPLE", "BANANA", "CHERRY"]

# With a Series
s = pd.Series(["python", "R", "Julia"])
str_to_upper(s)
# 0    PYTHON
# 1         R
# 2     JULIA
# dtype: object
```

---

Convert a string to lowercase.

```python
from tidystring import str_to_lower

# Basic usage
str_to_lower("HELLO")  # "hello"

# With mixed case
str_to_lower("Hello World")  # "hello world"

# With a list
words = ["APPLE", "Banana", "cherry"]
str_to_lower(words)  # ["apple", "banana", "cherry"]

# With a Series
s = pd.Series(["PYTHON", "R", "Julia"])
str_to_lower(s)
# 0    python
# 1         r
# 2     julia
# dtype: object
```

---

Convert a string to title case.

```python
from tidystring import str_to_title

# Basic usage
str_to_title("hello world")  # "Hello World"

# With already capitalized words
str_to_title("PYTHON programming")  # "Python Programming"

# With dashes (optional removal)
str_to_title("hello-world", remove_dashes=True)  # "Hello World"
str_to_title("hello-world", remove_dashes=False)  # "Hello-World"

# With a list
phrases = ["machine learning", "data science", "artificial intelligence"]
str_to_title(phrases)  # ["Machine Learning", "Data Science", "Artificial Intelligence"]

# With a Series
s = pd.Series(["natural language processing", "computer vision"])
str_to_title(s)
# 0    Natural Language Processing
# 1              Computer Vision
# dtype: object
```

---

Capitalize the first n characters of a string.

```python
from tidystring import str_upper_cut

# Basic usage (first character)
str_upper_cut("hello")  # "Hello"

# With n specified
str_upper_cut("hello", n=2)  # "HEllo"
str_upper_cut("python", n=3)  # "PYThon"

# With a list
words = ["apple", "banana", "cherry"]
str_upper_cut(words, n=2)  # ["APple", "BAnana", "CHerry"]

# With a Series
s = pd.Series(["python", "r", "julia"])
str_upper_cut(s, n=1)
# 0    Python
# 1         R
# 2     Julia
# dtype: object
```

---

Convert a camel case string to snake case.

```python
from tidystring import camel_to_snake

# Basic usage
camel_to_snake("helloWorld")  # "hello_world"
camel_to_snake("DataScience")  # "data_science"

# With multiple words
camel_to_snake("convertCamelCaseToSnakeCase")  # "convert_camel_case_to_snake_case"

# With a list
variables = ["firstName", "lastName", "emailAddress"]
camel_to_snake(variables)  # ["first_name", "last_name", "email_address"]

# With a Series
s = pd.Series(["userID", "orderCount", "totalPrice"])
camel_to_snake(s)
# 0       user_id
# 1    order_count
# 2    total_price
# dtype: object
```

---

Convert a snake case string to camel case.

```python
from tidystring import snake_to_camel

# Basic usage
snake_to_camel("hello_world")  # "HelloWorld"
snake_to_camel("data_science")  # "DataScience"

# With multiple underscores
snake_to_camel("convert_snake_case_to_camel_case")  # "ConvertSnakeCaseToCamelCase"

# With a list
variables = ["first_name", "last_name", "email_address"]
snake_to_camel(variables)  # ["FirstName", "LastName", "EmailAddress"]

# With a Series
s = pd.Series(["user_id", "order_count", "total_price"])
snake_to_camel(s)
# 0        UserId
# 1    OrderCount
# 2    TotalPrice
# dtype: object
```