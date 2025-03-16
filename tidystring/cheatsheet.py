"""
Cheatsheet module for tidystring.

This module provides functions to generate reference tables and help information
for various aspects of the tidystring package.
"""

import pandas as pd


def get_basic_cheatsheet():
    """
    Returns a DataFrame containing common string operations.

    Returns:
        pd.DataFrame: A DataFrame with function names, descriptions, and examples
    """
    data = {
        "Function": [
            "str_length",
            "str_detect",
            "str_extract",
            "str_replace",
            "str_remove",
            "str_trim",
            "str_to_upper",
            "str_to_lower",
            "str_to_title",
            "str_split",
            "str_sub",
            "str_count",
        ],
        "Description": [
            "Get the length of a string",
            "Detect if a pattern exists in a string",
            "Extract the first match of a pattern",
            "Replace all matches of a pattern",
            "Remove all matches of a pattern",
            "Remove whitespace from start and end",
            "Convert to uppercase",
            "Convert to lowercase",
            "Convert to title case",
            "Split string by pattern",
            "Extract substring from start/end positions",
            "Count occurrences of a pattern",
        ],
        "Example": [
            "str_length('hello') -> 5",
            "str_detect('hello world', 'o') -> True",
            "str_extract('hello world', 'h(\\w+)') -> 'ello'",
            "str_replace('hello', 'l', 'X') -> 'heXXo'",
            "str_remove('hello', 'l') -> 'heo'",
            "str_trim('  hello  ') -> 'hello'",
            "str_to_upper('hello') -> 'HELLO'",
            "str_to_lower('HELLO') -> 'hello'",
            "str_to_title('hello world') -> 'Hello World'",
            "str_split('a,b,c', ',') -> ['a', 'b', 'c']",
            "str_sub('hello', 1, 3) -> 'el'",
            "str_count('hello', 'l') -> 2",
        ],
    }
    return pd.DataFrame(data)


def get_case_cheatsheet():
    """
    Returns a DataFrame containing case conversion operations.

    Returns:
        pd.DataFrame: A DataFrame with function names, descriptions, and examples
    """
    data = {
        "Function": [
            "str_to_upper",
            "str_to_lower",
            "str_to_title",
            "str_upper_cut",
            "camel_to_snake",
            "snake_to_camel",
            "str_search_recase",
        ],
        "Description": [
            "Convert to uppercase",
            "Convert to lowercase",
            "Convert to title case",
            "Capitalize first n characters",
            "Convert camelCase to snake_case",
            "Convert snake_case to CamelCase",
            "Change case of matched pattern",
        ],
        "Example": [
            "str_to_upper('hello') -> 'HELLO'",
            "str_to_lower('HELLO') -> 'hello'",
            "str_to_title('hello world') -> 'Hello World'",
            "str_upper_cut('hello', n=2) -> 'HEllo'",
            "camel_to_snake('helloWorld') -> 'hello_world'",
            "snake_to_camel('hello_world') -> 'HelloWorld'",
            "str_search_recase('helloWorld', '\\w+', 'snakecase') -> 'hello_world'",
        ],
    }
    return pd.DataFrame(data)


def get_detection_cheatsheet():
    """
    Returns a DataFrame containing pattern detection operations.

    Returns:
        pd.DataFrame: A DataFrame with function names, descriptions, and examples
    """
    data = {
        "Function": ["str_detect", "str_startswith", "str_endswith", "str_count", "str_locate", "str_locate_all"],
        "Description": [
            "Detect if a pattern exists in a string",
            "Check if string starts with a pattern",
            "Check if string ends with a pattern",
            "Count occurrences of a pattern",
            "Find position of first match",
            "Find positions of all matches",
        ],
        "Example": [
            "str_detect('hello world', 'o') -> True",
            "str_startswith('hello', 'he') -> True",
            "str_endswith('hello', 'lo') -> True",
            "str_count('hello', 'l') -> 2",
            "str_locate('hello', 'l') -> 2",
            "str_locate_all('hello', 'l') -> [[2, 3], [3, 4]]",
        ],
    }
    return pd.DataFrame(data)


def get_extraction_cheatsheet():
    """
    Returns a DataFrame containing pattern extraction operations.

    Returns:
        pd.DataFrame: A DataFrame with function names, descriptions, and examples
    """
    data = {
        "Function": ["str_extract", "str_sub", "str_split"],
        "Description": [
            "Extract first match of a pattern",
            "Extract substring from start/end positions",
            "Split string by pattern into components",
        ],
        "Example": [
            "str_extract('hello world', 'h(\\w+)') -> 'ello'",
            "str_sub('hello', 1, 3) -> 'el'",
            "str_split('a,b,c', ',') -> ['a', 'b', 'c']",
        ],
    }
    return pd.DataFrame(data)


def get_modification_cheatsheet():
    """
    Returns a DataFrame containing string modification operations.

    Returns:
        pd.DataFrame: A DataFrame with function names, descriptions, and examples
    """
    data = {
        "Function": [
            "str_replace",
            "str_remove",
            "str_trim",
            "str_pad",
            "str_squish",
            "str_dup",
            "str_wrap",
            "str_concat",
            "str_dash_to_space",
            "str_search_apply",
        ],
        "Description": [
            "Replace all matches of a pattern",
            "Remove all matches of a pattern",
            "Remove whitespace from start and end",
            "Pad a string to a specified width",
            "Trim and replace internal whitespace",
            "Duplicate a string n times",
            "Wrap text to specified width",
            "Concatenate strings with separator",
            "Replace dashes with spaces",
            "Apply a function to each regex match",
        ],
        "Example": [
            "str_replace('hello', 'l', 'X') -> 'heXXo'",
            "str_remove('hello', 'l') -> 'heo'",
            "str_trim('  hello  ') -> 'hello'",
            "str_pad('hello', 10, side='both') -> '  hello   '",
            "str_squish('  hello    world  ') -> 'hello world'",
            "str_dup('abc', 2) -> 'abcabc'",
            "str_wrap('long text...', width=20)",
            "str_concat('hello', 'world', sep='-') -> 'hello-world'",
            "str_dash_to_space('hello-world') -> 'hello world'",
            "str_search_apply('ab12', '\\d+', lambda x: str(int(x)*2)) -> 'ab24'",
        ],
    }
    return pd.DataFrame(data)


def get_regex_cheatsheet():
    """
    Returns a DataFrame containing regex pattern information.

    Returns:
        pd.DataFrame: A DataFrame with pattern symbols, descriptions, and examples
    """
    data = {
        "Pattern": [
            ".",
            "\\w",
            "\\d",
            "\\s",
            "\\b",
            "^",
            "$",
            "[abc]",
            "[^abc]",
            "a|b",
            "a*",
            "a+",
            "a?",
            "a{3}",
            "a{2,4}",
            "(abc)",
            "(?:abc)",
            "(?=abc)",
            "(?!abc)",
        ],
        "Description": [
            "Any character except newline",
            "Word character (letter, digit, underscore)",
            "Digit character",
            "Whitespace character",
            "Word boundary",
            "Start of string",
            "End of string",
            "Any character in the set",
            "Any character not in the set",
            "a or b",
            "0 or more a's",
            "1 or more a's",
            "0 or 1 a",
            "Exactly 3 a's",
            "2 to 4 a's",
            "Capturing group",
            "Non-capturing group",
            "Positive lookahead",
            "Negative lookahead",
        ],
        "Example": [
            "'h.t' matches 'hat', 'hit', 'hot'",
            "'\\w+' matches 'hello123'",
            "'\\d+' matches '123'",
            "'\\s+' matches spaces, tabs, newlines",
            "'\\bword\\b' matches 'word' as whole word",
            "'^start' matches 'start' at beginning",
            "'end$' matches 'end' at the end",
            "'[aeiou]' matches any vowel",
            "'[^0-9]' matches any non-digit",
            "'cat|dog' matches 'cat' or 'dog'",
            "'a*' matches '', 'a', 'aa', 'aaa'",
            "'a+' matches 'a', 'aa', 'aaa'",
            "'colou?r' matches 'color' or 'colour'",
            "'a{3}' matches 'aaa'",
            "'a{2,4}' matches 'aa', 'aaa', 'aaaa'",
            "'(\\w+)@(\\w+)' captures username and domain",
            "'(?:\\w+)' groups without capturing",
            "'(?=\\d)\\w+' matches word followed by digit",
            "'(?!\\d)\\w+' matches word not followed by digit",
        ],
    }
    return pd.DataFrame(data)


def get_input_types_cheatsheet():
    """
    Returns a DataFrame showing how tidystring handles different input types.

    Returns:
        pd.DataFrame: A DataFrame with examples for different input types
    """
    data = {
        "Input Type": ["Single string", "List of strings", "pandas Series"],
        "Example Input": ["'hello world'", "['hello', 'world']", "pd.Series(['hello', 'world'])"],
        "Example Function": ["str_to_upper", "str_to_upper", "str_to_upper"],
        "Example Output": ["'HELLO WORLD'", "['HELLO', 'WORLD']", "pd.Series(['HELLO', 'WORLD'])"],
        "Notes": ["Returns a string", "Returns a list", "Returns a Series"],
    }
    return pd.DataFrame(data)


def print_cheatsheet(df):
    """
    Pretty-print a cheatsheet DataFrame.

    Args:
        df (pd.DataFrame): The cheatsheet DataFrame to print
    """
    # Set display options for better readability
    with pd.option_context(
        "display.max_rows", None, "display.max_columns", None, "display.width", 1000, "display.expand_frame_repr", False
    ):
        print(df)

def get_all_functions():
    """
    Returns a list of all string manipulation functions in tidystring.

    Returns:
        list: A list of all function names
    """
    functions = [
        # Basic string functions
        "str_length",
        "str_detect",
        "str_extract",
        "str_replace",
        "str_remove",
        "str_trim",
        # Case conversion
        "str_to_upper",
        "str_to_lower",
        "str_to_title",
        "str_upper_cut",
        "camel_to_snake",
        "snake_to_camel",
        "str_search_recase",
        # Detection functions
        "str_startswith",
        "str_endswith",
        "str_count",
        "str_locate",
        "str_locate_all",
        # Extraction functions
        "str_sub",
        "str_split",
        # Modification functions
        "str_pad",
        "str_squish",
        "str_dup",
        "str_wrap",
        "str_concat",
        "str_dash_to_space",
        "str_search_apply",
    ]
    
    return functions


def get_tidystring_cheatsheet():
    """
    Returns a comprehensive DataFrame containing all tidystring functions.

    This combines all the individual cheatsheets into a single reference table.

    Returns:
        pd.DataFrame: A DataFrame with all function names, descriptions, and examples
    """
    # Get all individual cheatsheets
    basic = get_basic_cheatsheet()
    case = get_case_cheatsheet()
    detection = get_detection_cheatsheet()
    extraction = get_extraction_cheatsheet()
    modification = get_modification_cheatsheet()

    # Combine all dataframes
    combined = pd.concat([basic, case, detection, extraction, modification])

    # Remove duplicates (some functions appear in multiple cheatsheets)
    combined = combined.drop_duplicates(subset=["Function"])

    # Sort alphabetically by function name
    combined = combined.sort_values("Function").reset_index(drop=True)

    return combined
