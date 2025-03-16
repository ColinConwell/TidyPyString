# Cheatsheets

This page contains quick reference guides for all the functions available in the `tidystring` package.

## Basic Operations

| Function | Description | Example |
|----------|-------------|---------|
| `str_length` | Get the length of a string | `str_length('hello') -> 5` |
| `str_detect` | Detect if a pattern exists in a string | `str_detect('hello world', 'o') -> True` |
| `str_extract` | Extract the first match of a pattern | `str_extract('hello world', 'h(\w+)') -> 'ello'` |
| `str_replace` | Replace all matches of a pattern | `str_replace('hello', 'l', 'X') -> 'heXXo'` |
| `str_remove` | Remove all matches of a pattern | `str_remove('hello', 'l') -> 'heo'` |
| `str_trim` | Remove whitespace from start and end | `str_trim('  hello  ') -> 'hello'` |
| `str_to_upper` | Convert to uppercase | `str_to_upper('hello') -> 'HELLO'` |
| `str_to_lower` | Convert to lowercase | `str_to_lower('HELLO') -> 'hello'` |
| `str_to_title` | Convert to title case | `str_to_title('hello world') -> 'Hello World'` |
| `str_split` | Split string by pattern | `str_split('a,b,c', ',') -> ['a', 'b', 'c']` |
| `str_sub` | Extract substring from start/end positions | `str_sub('hello', 1, 3) -> 'el'` |
| `str_count` | Count occurrences of a pattern | `str_count('hello', 'l') -> 2` |

## Case Conversion

| Function | Description | Example |
|----------|-------------|---------|
| `str_to_upper` | Convert to uppercase | `str_to_upper('hello') -> 'HELLO'` |
| `str_to_lower` | Convert to lowercase | `str_to_lower('HELLO') -> 'hello'` |
| `str_to_title` | Convert to title case | `str_to_title('hello world') -> 'Hello World'` |
| `str_upper_cut` | Capitalize first n characters | `str_upper_cut('hello', n=2) -> 'HEllo'` |
| `camel_to_snake` | Convert camelCase to snake_case | `camel_to_snake('helloWorld') -> 'hello_world'` |
| `snake_to_camel` | Convert snake_case to CamelCase | `snake_to_camel('hello_world') -> 'HelloWorld'` |
| `str_search_recase` | Change case of matched pattern | `str_search_recase('helloWorld', '\w+', 'snakecase') -> 'hello_world'` |

## Pattern Detection

| Function | Description | Example |
|----------|-------------|---------|
| `str_detect` | Detect if a pattern exists in a string | `str_detect('hello world', 'o') -> True` |
| `str_startswith` | Check if string starts with a pattern | `str_startswith('hello', 'he') -> True` |
| `str_endswith` | Check if string ends with a pattern | `str_endswith('hello', 'lo') -> True` |
| `str_count` | Count occurrences of a pattern | `str_count('hello', 'l') -> 2` |
| `str_locate` | Find position of first match | `str_locate('hello', 'l') -> 2` |
| `str_locate_all` | Find positions of all matches | `str_locate_all('hello', 'l') -> [[2, 3], [3, 4]]` |

## Pattern Extraction

| Function | Description | Example |
|----------|-------------|---------|
| `str_extract` | Extract first match of a pattern | `str_extract('hello world', 'h(\w+)') -> 'ello'` |
| `str_sub` | Extract substring from start/end positions | `str_sub('hello', 1, 3) -> 'el'` |
| `str_split` | Split string by pattern into components | `str_split('a,b,c', ',') -> ['a', 'b', 'c']` |

## String Modification

| Function | Description | Example |
|----------|-------------|---------|
| `str_replace` | Replace all matches of a pattern | `str_replace('hello', 'l', 'X') -> 'heXXo'` |
| `str_remove` | Remove all matches of a pattern | `str_remove('hello', 'l') -> 'heo'` |
| `str_trim` | Remove whitespace from start and end | `str_trim('  hello  ') -> 'hello'` |
| `str_pad` | Pad a string to a specified width | `str_pad('hello', 10, side='both') -> '  hello   '` |
| `str_squish` | Trim and replace internal whitespace | `str_squish('  hello    world  ') -> 'hello world'` |
| `str_dup` | Duplicate a string n times | `str_dup('abc', 2) -> 'abcabc'` |
| `str_wrap` | Wrap text to specified width | `str_wrap('long text...', width=20)` |
| `str_concat` | Concatenate strings with separator | `str_concat('hello', 'world', sep='-') -> 'hello-world'` |
| `str_dash_to_space` | Replace dashes with spaces | `str_dash_to_space('hello-world') -> 'hello world'` |
| `str_search_apply` | Apply a function to each regex match | `str_search_apply('ab12', '\d+', lambda x: str(int(x)*2)) -> 'ab24'` |

## Input Type Handling

TidyPyString functions work with different input types while preserving the output type:

| Input Type | Example Input | Example Output from `str_to_upper` | Notes |
|------------|---------------|-----------------------------------|-------|
| Single string | `'hello world'` | `'HELLO WORLD'` | Returns a string |
| List of strings | `['hello', 'world']` | `['HELLO', 'WORLD']` | Returns a list |
| pandas Series | `pd.Series(['hello', 'world'])` | `pd.Series(['HELLO', 'WORLD'])` | Returns a Series |

## Regex Patterns

| Pattern | Description | Example |
|---------|-------------|---------|
| `.` | Any character except newline | `'h.t'` matches 'hat', 'hit', 'hot' |
| `\w` | Word character (letter, digit, underscore) | `'\w+'` matches 'hello123' |
| `\d` | Digit character | `'\d+'` matches '123' |
| `\s` | Whitespace character | `'\s+'` matches spaces, tabs, newlines |
| `\b` | Word boundary | `'\bword\b'` matches 'word' as whole word |
| `^` | Start of string | `'^start'` matches 'start' at beginning |
| `$` | End of string | `'end$'` matches 'end' at the end |
| `[abc]` | Any character in the set | `'[aeiou]'` matches any vowel |
| `[^abc]` | Any character not in the set | `'[^0-9]'` matches any non-digit |
| `a\|b` | a or b | `'cat\|dog'` matches 'cat' or 'dog' |
| `a*` | 0 or more a's | `'a*'` matches '', 'a', 'aa', 'aaa' |
| `a+` | 1 or more a's | `'a+'` matches 'a', 'aa', 'aaa' |
| `a?` | 0 or 1 a | `'colou?r'` matches 'color' or 'colour' |
| `a{3}` | Exactly 3 a's | `'a{3}'` matches 'aaa' |
| `a{2,4}` | 2 to 4 a's | `'a{2,4}'` matches 'aa', 'aaa', 'aaaa' |
| `(abc)` | Capturing group | `'(\w+)@(\w+)'` captures username and domain |
| `(?:abc)` | Non-capturing group | `'(?:\w+)'` groups without capturing |
| `(?=abc)` | Positive lookahead | `'(?=\d)\w+'` matches word followed by digit |
| `(?!abc)` | Negative lookahead | `'(?!\d)\w+'` matches word not followed by digit |

## Regex Utility Functions

TidyPyString provides helper functions to build regular expressions:

| Function | Description | Example |
|----------|-------------|---------|
| `re_literal()` | Escape special characters | `re_literal('a.b*c') -> 'a\\.b\\*c'` |
| `re_or()` | Combine patterns with OR | `re_or('cat', 'dog') -> 'cat\|dog'` |
| `re_chars()` | Match any char in set | `re_chars('aeiou') -> '[aeiou]'` |
| `re_not_chars()` | Match any char not in set | `re_not_chars('aeiou') -> '[^aeiou]'` |
| `re_digit()` | Match a digit | `re_digit() -> '\d'` |
| `re_word()` | Match a word character | `re_word() -> '\w'` |
| `re_space()` | Match whitespace | `re_space() -> '\s'` |
| `re_any()` | Match any character | `re_any() -> '.'` |
| `re_boundary()` | Match word boundary | `re_boundary() -> '\b'` |
| `re_start()` | Match start of string | `re_start() -> '^'` |
| `re_end()` | Match end of string | `re_end() -> '$'` |
| `re_capture()` | Create capturing group | `re_capture('\d+') -> '(\d+)'` |
| `re_group()` | Create non-capturing group | `re_group('\d+') -> '(?:\d+)'` |
| `re_whole_word()` | Match whole word | `re_whole_word('cat') -> '\bcat\b'` |
| `re_date()` | Match common date formats | `re_date() -> '\b(\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}/\d{4})\b'` |
| `re_email()` | Match email addresses | Returns pattern matching emails |
| `re_url()` | Match URLs | Returns pattern matching URLs |
| `re_phone_us()` | Match US phone numbers | Returns pattern matching US phone numbers |

## Programmatic Access

You can access all these cheatsheets programmatically in your code:

```python
from tidystring.cheatsheet import get_basic_cheatsheet, get_combined_cheatsheet, print_cheatsheet

# Get basic reference as DataFrame
df = get_basic_cheatsheet()

# Print nicely formatted
print_cheatsheet(df)

# Get comprehensive cheatsheet with all functions
all_df = get_combined_cheatsheet()
print_cheatsheet(all_df)
```

Available cheatsheet functions:

- `get_basic_cheatsheet()`: Common string operations
- `get_case_cheatsheet()`: Case conversion operations  
- `get_detection_cheatsheet()`: Pattern detection operations
- `get_extraction_cheatsheet()`: Pattern extraction operations
- `get_modification_cheatsheet()`: String modification operations
- `get_regex_cheatsheet()`: Regular expression patterns
- `get_input_types_cheatsheet()`: Input type handling
- `get_all_functions()`: List of all available functions
- `get_combined_cheatsheet()`: Comprehensive cheatsheet with all functions