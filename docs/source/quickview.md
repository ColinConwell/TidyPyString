# Package Overview

`tidystring` is a toolbox for performing ready-to-use string operations on python strings -- whether they be single strings, lists of strings, or pandas Series typed as strings. Inspired by R's `stringr` package from the tidyverse, it provides consistent, intuitive string manipulation functions.

## Installation

To get started, simply install the package (currently on GitHub):

```shell
pip install tidystring
```

Or, the latest version from GitHub:

```shell
pip install git+https://github.com/ColinConwell/TidyPyString.git
```

## Quick Start Examples

### Basic Usage

```python
from tidystring import str_detect, str_extract, str_split

# Works with single strings
str_detect("hello world", "world")  # True
str_extract("hello world", "h(\\w+)")  # 'ello'
str_split("a.b.c", "\\.")  # ['a', 'b', 'c']

# Works with pandas Series
import pandas as pd
series = pd.Series(["hello world", "python code"])
str_to_title(series)
# 0    Hello World
# 1    Python Code
# dtype: object
```

### String Transformation

```python
from tidystring import str_to_upper, str_to_lower, str_trim

# Case conversion
str_to_upper("hello")  # 'HELLO'
str_to_lower("WORLD")  # 'world'

# Whitespace removal
str_trim("  hello  ")  # 'hello'
```

### Pattern Matching

```python
from tidystring import str_detect, str_startswith, str_endswith

# Check if string contains pattern
str_detect(pd.Series(["apple", "banana"]), "a")
# 0    True
# 1    True
# dtype: bool

# Check start/end patterns
str_startswith("hello world", "hello")  # True
str_endswith("hello world", "world")  # True
```

### Advanced Features

```python
from tidystring import str_concat, str_search_apply, str_search_recase

# Concatenate strings with separator
str_concat("hello", "world", sep="-")  # 'hello-world'

# Apply function to matching patterns
str_search_apply("ab12cd34", "\\d+", lambda x: str(int(x) * 2))  # 'ab24cd68'

# Change case of matching patterns
str_search_recase("helloWorld", "\\w+", "snakecase")  # 'hello_world'
```

## Working with Different Data Types

TidyPyString works seamlessly with:

1. **Single strings** (`str`): Perfect for simple operations
2. **Pandas Series**: Vectorized operations for data analysis
3. **Lists of strings**: Through pandas Series conversion

Every function consistently handles these input types and returns the same type as the input:

```python
# Input: string, Output: string
result1 = str_to_upper("hello")  # 'HELLO'

# Input: Series, Output: Series
series = pd.Series(["hello", "world"])
result2 = str_to_upper(series)
# 0    HELLO
# 1    WORLD
# dtype: object
```

## Common Use Cases

### Text Cleaning

```python
# Remove unwanted characters and trim whitespace
from tidystring import str_remove, str_trim

text = "  Hello, World!  "
clean_text = str_trim(str_remove(text, ","))  # 'Hello World!'
```

### Pattern Extraction

```python
# Extract email addresses from text
from tidystring import str_extract

text = "Contact us at info@example.com or support@example.com"
email = str_extract(text, "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}")  # 'info@example.com'
```

### Text Standardization

```python
# Standardize case for database entries
from tidystring import str_to_lower

names = pd.Series(["John", "JANE", "Bob"])
standardized = str_to_lower(names)
# 0    john
# 1    jane
# 2     bob
# dtype: object
```