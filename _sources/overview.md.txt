# Package Overview

`tidystring` is a Python package for performing consistent, intuitive string operations. Inspired by R's `stringr` package from the tidyverse, it provides a collection of functions that work seamlessly with different string representations in Python.

## Key Features

- **Consistent Interface**: All functions follow a consistent naming and parameter pattern
- **Input Flexibility**: Works with single strings, lists of strings, and pandas Series
- **Type Preservation**: Returns the same type as the input
- **Intuitive Names**: Function names clearly indicate their purpose (e.g., `str_detect`, `str_extract`)
- **Comprehensive Toolkit**: Covers detection, extraction, modification, case conversion, and more

## Installation

You can install the package via pip:

```shell
pip install tidystring
```

For the latest development version:

```shell
pip install git+https://github.com/ColinConwell/TidyPyString.git
```

## Quick Start

Import the functions you need:

```python
from tidystring import str_detect, str_extract, str_replace
```

### Works with Multiple Input Types

```python
# With single strings
str_to_upper("hello")  # 'HELLO'

# With lists
str_to_upper(["hello", "world"])  # ['HELLO', 'WORLD']

# With pandas Series
import pandas as pd
series = pd.Series(["hello", "world"])
str_to_upper(series)
# 0    HELLO
# 1    WORLD
# dtype: object
```

### Function Overview

TidyPyString provides functions in several categories:

- **Detection**: `str_detect`, `str_startswith`, `str_endswith`, `str_count`
- **Extraction**: `str_extract`, `str_sub`, `str_split`, `str_locate`, `str_locate_all`
- **Modification**: `str_replace`, `str_remove`, `str_trim`, `str_dash_to_space`
- **Case Conversion**: `str_to_upper`, `str_to_lower`, `str_to_title`, `str_upper_cut`, `camel_to_snake`, `snake_to_camel`
- **String Basics**: `str_length`, `str_pad`, `str_dup`, `str_squish`, `str_wrap`
- **Utilities**: `str_concat`, `str_search_apply`, `str_search_recase`

### Usage Examples

```python
# Pattern detection
str_detect("hello world", "world")  # True

# Pattern extraction
str_extract("hello world", "h(\\w+)")  # 'ello'

# String replacement
str_replace("hello world", "o", "X")  # 'hellX wXrld'

# Case conversion
str_to_title("hello world")  # 'Hello World'

# String modification
str_trim("  hello  ")  # 'hello'

# String splitting
str_split("a,b,c", ",")  # ['a', 'b', 'c']

# String concatenation
str_concat("hello", "world", sep="-")  # 'hello-world'
```

## Why TidyPyString?

While Python's built-in string methods and pandas string accessor are powerful, TidyPyString offers:

1. A more consistent naming convention inspired by R's stringr
2. Seamless switching between different string representations
3. Consistently preserved return types
4. Additional utility functions not available in standard libraries

## Next Steps

Dive into the thematic documentation pages to explore the full range of functions and capabilities.