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

strings = pd.Series(["text_alpha", "text_beta", "text_gamma"])

## detect if strings contain "alpha"
ts.str_detect(strings, "alpha")

## remove "alpha" from all strings
ts.str_remove(strings, "alpha")

## convert all strings to title case, removing dashes
ts.str_to_title(strings, remove_dashes=True)
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
- `str_to_title()`
- `str_to_upper()`
- `str_to_lower()`

Additional `tidystring` functions not in `stringr`:

- `str_concat`
- `str_startswith`
- `str_endswith`
- `str_upper_cut`
- `str_search_apply`
- `str_search_recase`
- `str_dash_to_space`


Check out the [documentation]() for more information.

## Tidyverse-Inspired Python

There are increasingly a number of other Python packages that are helping to bring the beautiful tidyverse to Python. Here's a couple to consider:

Here's a short-list of some stand-outs:

- [`siuba`](https://siuba.org/)
- [`pyjanitor`](https://pyjanitor-devs.github.io/pyjanitor/)

## Development Notes

### Install from GitHub

To install the latest version from GitHub, simply run:

```bash
pip install git+https://github.com/ColinConwell/TidyPyString.git
```

### Use of Generative AI

All code in this package has been tested by me (a human), but much of the documentation comes from a custom generative AI auto-documentation pipeline, powered by Claude-Sonnet-3.7. Documentation may thus be subject to some error. Please feel free to file an issue if this appears to be the case.
