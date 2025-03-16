"""
Cheatsheet module for tidystring.

This module provides functions to generate reference tables and help information
for various aspects of the tidystring package.
"""

import pandas as pd


def get_tidystring_cheatsheet(group=None):
    """
    Returns a comprehensive DataFrame containing tidystring functions.

    Args:
        group (str, optional): Filter by function group. Options:
            'basic', 'case', 'detection', 'extraction', 'modification', 'regex', 'input_types'.
            If None, returns all tidystring functions. Defaults to None.

    Returns:
        pd.DataFrame: A DataFrame with function names, descriptions, examples, and groups
    """
    # Define all cheatsheet data with group info
    data = {
        # Basic functions
        "str_length": {
            "Description": "Get the length of a string",
            "Example": "str_length('hello') -> 5",
            "Group": "basic",
        },
        "str_detect": {
            "Description": "Detect if a pattern exists in a string",
            "Example": "str_detect('hello world', 'o') -> True",
            "Group": "detection",
        },
        "str_extract": {
            "Description": "Extract the first match of a pattern",
            "Example": "str_extract('hello world', 'h(\\w+)') -> 'ello'",
            "Group": "extraction",
        },
        "str_replace": {
            "Description": "Replace all matches of a pattern",
            "Example": "str_replace('hello', 'l', 'X') -> 'heXXo'",
            "Group": "modification",
        },
        "str_remove": {
            "Description": "Remove all matches of a pattern",
            "Example": "str_remove('hello', 'l') -> 'heo'",
            "Group": "modification",
        },
        "str_trim": {
            "Description": "Remove whitespace from start and end",
            "Example": "str_trim('  hello  ') -> 'hello'",
            "Group": "modification",
        },
        "str_to_upper": {
            "Description": "Convert to uppercase",
            "Example": "str_to_upper('hello') -> 'HELLO'",
            "Group": "case",
        },
        "str_to_lower": {
            "Description": "Convert to lowercase",
            "Example": "str_to_lower('HELLO') -> 'hello'",
            "Group": "case",
        },
        "str_to_title": {
            "Description": "Convert to title case",
            "Example": "str_to_title('hello world') -> 'Hello World'",
            "Group": "case",
        },
        "str_split": {
            "Description": "Split string by pattern",
            "Example": "str_split('a,b,c', ',') -> ['a', 'b', 'c']",
            "Group": "extraction",
        },
        "str_sub": {
            "Description": "Extract substring from start/end positions",
            "Example": "str_sub('hello', 1, 3) -> 'el'",
            "Group": "extraction",
        },
        "str_count": {
            "Description": "Count occurrences of a pattern",
            "Example": "str_count('hello', 'l') -> 2",
            "Group": "detection",
        },
        "str_upper_cut": {
            "Description": "Capitalize first n characters",
            "Example": "str_upper_cut('hello', n=2) -> 'HEllo'",
            "Group": "case",
        },
        "camel_to_snake": {
            "Description": "Convert camelCase to snake_case",
            "Example": "camel_to_snake('helloWorld') -> 'hello_world'",
            "Group": "case",
        },
        "snake_to_camel": {
            "Description": "Convert snake_case to CamelCase",
            "Example": "snake_to_camel('hello_world') -> 'HelloWorld'",
            "Group": "case",
        },
        "str_search_recase": {
            "Description": "Change case of matched pattern",
            "Example": "str_search_recase('helloWorld', '\\w+', 'snakecase') -> 'hello_world'",
            "Group": "case",
        },
        "str_startswith": {
            "Description": "Check if string starts with a pattern",
            "Example": "str_startswith('hello', 'he') -> True",
            "Group": "detection",
        },
        "str_endswith": {
            "Description": "Check if string ends with a pattern",
            "Example": "str_endswith('hello', 'lo') -> True",
            "Group": "detection",
        },
        "str_locate": {
            "Description": "Find position of first match",
            "Example": "str_locate('hello', 'l') -> 2",
            "Group": "detection",
        },
        "str_locate_all": {
            "Description": "Find positions of all matches",
            "Example": "str_locate_all('hello', 'l') -> [[2, 3], [3, 4]]",
            "Group": "detection",
        },
        "str_pad": {
            "Description": "Pad a string to a specified width",
            "Example": "str_pad('hello', 10, side='both') -> '  hello   '",
            "Group": "modification",
        },
        "str_squish": {
            "Description": "Trim and replace internal whitespace",
            "Example": "str_squish('  hello    world  ') -> 'hello world'",
            "Group": "modification",
        },
        "str_dup": {
            "Description": "Duplicate a string n times",
            "Example": "str_dup('abc', 2) -> 'abcabc'",
            "Group": "modification",
        },
        "str_wrap": {
            "Description": "Wrap text to specified width",
            "Example": "str_wrap('long text...', width=20)",
            "Group": "modification",
        },
        "str_concat": {
            "Description": "Concatenate strings with separator",
            "Example": "str_concat('hello', 'world', sep='-') -> 'hello-world'",
            "Group": "modification",
        },
        "str_dash_to_space": {
            "Description": "Replace dashes with spaces",
            "Example": "str_dash_to_space('hello-world') -> 'hello world'",
            "Group": "modification",
        },
        "str_search_apply": {
            "Description": "Apply a function to each regex match",
            "Example": "str_search_apply('ab12', '\\d+', lambda x: str(int(x)*2)) -> 'ab24'",
            "Group": "modification",
        },
    }

    # Create DataFrame from the data
    functions = []
    descriptions = []
    examples = []
    groups = []

    for func, details in data.items():
        functions.append(func)
        descriptions.append(details["Description"])
        examples.append(details["Example"])
        groups.append(details["Group"])

    df = pd.DataFrame({"Function": functions, "Description": descriptions, "Example": examples, "Group": groups})

    # Filter by group if specified
    if group is not None:
        # Special handling for 'regex' and 'input_types' groups
        if group.lower() == "regex":
            return get_regex_cheatsheet()
        elif group.lower() == "input_types":
            return get_input_types_cheatsheet()

        if group.lower() not in set(df["Group"]):
            valid_groups = ", ".join(sorted(set(df["Group"])) + ["regex", "input_types"])
            raise ValueError(f"Invalid group: '{group}'. Valid options are: {valid_groups}")
        df = df[df["Group"] == group.lower()]

    # Sort alphabetically by function name
    df = df.sort_values("Function").reset_index(drop=True)

    return df


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


def get_all_functions():
    """
    Returns a list of all string manipulation functions in tidystring.

    Returns:
        list: A list of all function names
    """
    # Get all functions from the main cheatsheet
    df = get_tidystring_cheatsheet()
    return df["Function"].tolist()


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
