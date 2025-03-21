# Tidy(Py)String: Wrangle those Strings

Easier string operations in Python, inspired by the tidyverse (especially [`stringr`](https://stringr.tidyverse.org/reference/index.html)).

All functions can be run both on single strings and vectors of strings, with direct support for base python's string type (`str`), lists or arrays of strings (`[str, str, ...]`), and Pandas columns / series (`pd.Series`), and indirect support other string-like or string-typed variables.

## Quick Start

Install the package from PyPI:

```shell
pip install tidystring
```

Then, wrangle those strings:

```python
import pandas as pd
import tidystring as ts

strings = ["text_alpha", "text_beta", "text_gamma"]

## detect if strings contain "alpha"
ts.str_detect(strings, "alpha")

## remove "alpha" from all strings
ts.str_remove(strings, "alpha")

## convert all strings to title case, removing dashes
ts.str_to_title(strings, remove_dashes=True)

# convert strings to pd.Series
strings = pd.Series(strings)

# replace "text" with "enum" in all strings
ts.str_replace(strings, "text", "enum")
```

## Development

This project uses [Hatch](https://hatch.pypa.io/) for project management. To get started with development:

1. Install Hatch:
```shell
pip install hatch
```

2. Create a development environment:
```shell
hatch env create
```

3. Activate the environment:
```shell
hatch shell
```

4. Run tests:
```shell
hatch run test
```

5. Build documentation:
```shell
hatch run docs:build
```
   Or use the provided script:
```shell
python scripts/build_docs.py
```

## Inspired by [`StringR`](https://stringr.tidyverse.org/reference/index.html)

... which offers the following functions:

- `str_length()`
- `str_sub()`
- `str_dup()`
- `str_trim()`
- `str_pad()`
- `str_wrap()`
- `str_to_upper()`
- `str_to_lower()`
- `str_to_title()`
- `str_detect()`
- `str_count()`
- `str_locate()`
- `str_locate_all()`
- `str_extract()`
- `str_extract_all()`
- `str_match()`
- `str_match_all()`
- `str_replace()`
- `str_replace_all()`
- `str_split()`
- `str_split_fixed()`
- `str_glue()`
- `str_order()`
- `str_sort()`
- `str_subset()`
- `str_which()`
- `str_squish()`
- `str_flatten()`

(All of these are on my to-do list, but for now...)

`tidystring`'s currently available `stringr` ports:

- `str_detect()`
- `str_remove()`
- `str_extract()`
- `str_split()`
- `str_trim()`
- `str_count()`
- `str_locate()`
- `str_locate_all()`
- `str_sub()`
- `str_pad()`
- `str_dup()`
- `str_squish()`
- `str_wrap()`
- `str_to_title()`
- `str_to_upper()`
- `str_to_lower()`
- `str_length()`

Additional `tidystring` functions not in `stringr`:

- `str_concat`
- `str_startswith`
- `str_endswith`
- `str_upper_cut`
- `str_search_apply`
- `str_search_recase`
- `str_dash_to_space`
- `camel_to_snake`
- `snake_to_camel`


Check out the [documentation]() for more information.

## Cheatsheets and Regex Utilities

`tidystring` also includes cheatsheets and regex helper functions to make string manipulation even easier:

### Interactive Cheatsheets

Get instant reference guides for all `tidystring` functions with built-in cheatsheets:

```python
from tidystring import get_basic_cheatsheet, get_combined_cheatsheet, print_cheatsheet

# View all basic functions
basic_df = get_basic_cheatsheet()
print_cheatsheet(basic_df)

# View all functions in one comprehensive table
all_df = get_combined_cheatsheet()
print_cheatsheet(all_df)
```

Available cheatsheets include: basic operations, case conversion, pattern detection, extraction, modification, regex patterns, input type handling, and a combined reference.

### Regex Pattern Builders

Build complex regular expressions with simple, readable functions:

```python
from tidystring import re_digit, re_capture, re_repeat, re_or, re_email

# Create a pattern for US phone numbers
phone_pattern = re_or(
    re_capture(f"{re_digit()}{re_repeat(3)}-{re_digit()}{re_repeat(3)}-{re_digit()}{re_repeat(4)}"),
    re_capture(f"\\({re_digit()}{re_repeat(3)}\\) {re_digit()}{re_repeat(3)}-{re_digit()}{re_repeat(4)}")
)

# Use pre-built patterns for common formats
url_pattern = re_url()

# Use patterns with string functions
from tidystring import str_extract
urls = ["https://www.example.com", "No url here"]
str_extract(urls, url_pattern)  # ['https://www.example.com', None]
```

## Tidyverse-Inspired Python

There are increasingly a number of other Python packages that are helping to bring the beautiful tidyverse to Python. Here's a couple to consider:

Here's a short-list of some stand-outs:

- [`siuba`](https://siuba.org/)
- [`pyjanitor`](https://pyjanitor-devs.github.io/pyjanitor/)

## Development Notes

### Installation Options

Install the stable version from PyPI:

```bash
pip install tidystring
```

Or, the latest version from GitHub:

```bash
pip install git+https://github.com/ColinConwell/TidyPyString.git
```

### Code Formatting

If you're contributing to the project, you can use the provided formatting scripts:

```bash
# Format the code (modifies files)
./devops/run_format.sh

# Check code formatting (doesn't modify files)
./devops/run_linter.sh
```

### Use of Generative AI

All code in this package has been tested by me (a human), but much of the documentation comes from a custom generative AI auto-documentation pipeline, powered by Claude-Sonnet-3.7. Documentation may thus be subject to some error. Please feel free to file an issue if this appears to be the case.
