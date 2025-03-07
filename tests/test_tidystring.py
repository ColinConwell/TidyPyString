import pytest
import pandas as pd
import numpy as np
import tidystring as ts

# Test data
SINGLE_STR = "hello world"
LIST_STR = ["hello world", "python test", "string operations"]
SERIES_STR = pd.Series(LIST_STR)

# Utility functions for testing
def check_return_type(func, input_val, *args, **kwargs):
    """Test that the function returns the same type it was given."""
    result = func(input_val, *args, **kwargs)
    
    if isinstance(input_val, str):
        assert isinstance(result, str), f"Expected str, got {type(result)}"
    elif isinstance(input_val, list):
        assert isinstance(result, list), f"Expected list, got {type(result)}"
    elif isinstance(input_val, pd.Series):
        assert isinstance(result, pd.Series), f"Expected pd.Series, got {type(result)}"

def _test_all_input_types(func, args_dict, expected_results):
    """Utility function to test a function with all input types and verify expected results.
    
    Not a test itself, but used by other tests.
    """
    # Test with string input
    result = func(SINGLE_STR, **args_dict.get('str', {}))
    assert result == expected_results['str'], f"Failed with str input. Got {result}"
    assert isinstance(result, type(expected_results['str'])), f"Wrong return type. Got {type(result)}"
    
    # Test with list input
    result = func(LIST_STR, **args_dict.get('list', {}))
    assert result == expected_results['list'], f"Failed with list input. Got {result}"
    assert isinstance(result, list), f"Wrong return type. Got {type(result)}"
    
    # Test with pandas Series input
    result = func(SERIES_STR, **args_dict.get('series', {}))
    assert all(result == expected_results['series']), f"Failed with series input. Got {result}"
    assert isinstance(result, pd.Series), f"Wrong return type. Got {type(result)}"

# ---- Tests for individual functions ----

class TestCaseConversions:
    """Tests for case conversion functions."""
    
    def test_camel_to_snake(self):
        single_input = "helloWorld"
        list_input = ["helloWorld", "pythonTest", "stringOps"]
        series_input = pd.Series(list_input)
        
        # Check single string
        assert ts.camel_to_snake(single_input) == "hello_world"
        assert isinstance(ts.camel_to_snake(single_input), str)
        
        # Check list
        result = ts.camel_to_snake(list_input)
        assert result == ["hello_world", "python_test", "string_ops"]
        assert isinstance(result, list)
        
        # Check Series
        result = ts.camel_to_snake(series_input)
        assert all(result == pd.Series(["hello_world", "python_test", "string_ops"]))
        assert isinstance(result, pd.Series)
    
    def test_snake_to_camel(self):
        single_input = "hello_world"
        list_input = ["hello_world", "python_test", "string_ops"]
        series_input = pd.Series(list_input)
        
        # Check single string
        assert ts.snake_to_camel(single_input) == "HelloWorld"
        assert isinstance(ts.snake_to_camel(single_input), str)
        
        # Check list
        result = ts.snake_to_camel(list_input)
        assert result == ["HelloWorld", "PythonTest", "StringOps"]
        assert isinstance(result, list)
        
        # Check Series
        result = ts.snake_to_camel(series_input)
        assert all(result == pd.Series(["HelloWorld", "PythonTest", "StringOps"]))
        assert isinstance(result, pd.Series)

class TestStringDetection:
    """Tests for string detection functions."""
    
    def test_str_detect(self):
        args = {'pattern': 'o'}
        
        # Check single string
        assert ts.str_detect(SINGLE_STR, **args) == True
        assert isinstance(ts.str_detect(SINGLE_STR, **args), bool)
        
        # Check list
        result = ts.str_detect(LIST_STR, **args)
        assert result == [True, True, True]
        assert isinstance(result, list)
        
        # Check Series
        result = ts.str_detect(SERIES_STR, **args)
        assert all(result == pd.Series([True, True, True]))
        assert isinstance(result, pd.Series)
    
    def test_str_startswith(self):
        args = {'pattern': 'hello'}
        
        # Check single string
        assert ts.str_startswith(SINGLE_STR, **args) == True
        assert isinstance(ts.str_startswith(SINGLE_STR, **args), bool)
        
        # Check list
        result = ts.str_startswith(LIST_STR, **args)
        assert result == [True, False, False]
        assert isinstance(result, list)
        
        # Check Series
        result = ts.str_startswith(SERIES_STR, **args)
        assert all(result == pd.Series([True, False, False]))
        assert isinstance(result, pd.Series)
    
    def test_str_endswith(self):
        args = {'pattern': 'world'}
        
        # Check single string
        assert ts.str_endswith(SINGLE_STR, **args) == True
        assert isinstance(ts.str_endswith(SINGLE_STR, **args), bool)
        
        # Check list
        result = ts.str_endswith(LIST_STR, **args)
        assert result == [True, False, False]
        assert isinstance(result, list)
        
        # Check Series
        result = ts.str_endswith(SERIES_STR, **args)
        assert all(result == pd.Series([True, False, False]))
        assert isinstance(result, pd.Series)

class TestStringModification:
    """Tests for string modification functions."""
    
    def test_str_replace(self):
        args = {'pattern': 'o', 'replacement': 'X'}
        
        # Check single string
        result = ts.str_replace(SINGLE_STR, **args)
        assert result == "hellX wXrld"
        assert isinstance(result, str)
        
        # Check list
        result = ts.str_replace(LIST_STR, **args)
        expected = ["hellX wXrld", "pythXn test", "string XperatiXns"]
        assert result == expected
        assert isinstance(result, list)
        
        # Check Series
        result = ts.str_replace(SERIES_STR, **args)
        assert all(result == pd.Series(expected))
        assert isinstance(result, pd.Series)
        
        # Test with count (n) parameter
        result = ts.str_replace(SINGLE_STR, 'o', 'X', n=1)
        assert result == "hellX world"
    
    def test_str_remove(self):
        args = {'pattern': 'o'}
        
        # Check single string
        result = ts.str_remove(SINGLE_STR, **args)
        assert result == "hell wrld"
        assert isinstance(result, str)
        
        # Check list
        result = ts.str_remove(LIST_STR, **args)
        expected = ["hell wrld", "pythn test", "string peratins"]
        assert result == expected
        assert isinstance(result, list)
        
        # Check Series
        result = ts.str_remove(SERIES_STR, **args)
        assert all(result == pd.Series(expected))
        assert isinstance(result, pd.Series)
    
    def test_str_trim(self):
        padded_str = "  hello world  "
        padded_list = ["  hello world  ", " python test ", "  string operations"]
        padded_series = pd.Series(padded_list)
        
        # Check single string
        result = ts.str_trim(padded_str)
        assert result == "hello world"
        assert isinstance(result, str)
        
        # Check list
        result = ts.str_trim(padded_list)
        expected = ["hello world", "python test", "string operations"]
        assert result == expected
        assert isinstance(result, list)
        
        # Check Series
        result = ts.str_trim(padded_series)
        assert all(result == pd.Series(expected))
        assert isinstance(result, pd.Series)

class TestStringExtraction:
    """Tests for string extraction functions."""
    
    def test_str_extract(self):
        args = {'pattern': 'h(\\w+)'}
        
        # Check single string
        result = ts.str_extract(SINGLE_STR, **args)
        assert result == "ello"
        assert isinstance(result, str)
        
        # Check list
        result = ts.str_extract(LIST_STR, **args)
        expected = ["ello", None, None]  # No match returns None
        assert result == expected
        assert isinstance(result, list)
        
        # Check Series
        result = ts.str_extract(SERIES_STR, **args)
        # Pandas will return NaN for no match
        expected_series = pd.Series(["ello", np.nan, np.nan])
        pd.testing.assert_series_equal(result, expected_series, check_dtype=False)
        assert isinstance(result, pd.Series)
    
    def test_str_sub(self):
        # Check single string
        result = ts.str_sub(SINGLE_STR, 0, 5)
        assert result == "hello"
        assert isinstance(result, str)
        
        # Check with only start parameter
        result = ts.str_sub(SINGLE_STR, 6)
        assert result == "world"
        assert isinstance(result, str)
        
        # Check list
        result = ts.str_sub(LIST_STR, 0, 5)
        expected = ["hello", "pytho", "strin"]
        assert result == expected
        assert isinstance(result, list)
        
        # Check Series
        result = ts.str_sub(SERIES_STR, 0, 5)
        assert all(result == pd.Series(expected))
        assert isinstance(result, pd.Series)
    
    def test_str_split(self):
        # Check single string
        result = ts.str_split(SINGLE_STR, " ")
        assert result == ["hello", "world"]
        assert isinstance(result, list)  # Note: split always returns a list
        
        # Check list
        result = ts.str_split(LIST_STR, " ")
        expected = [["hello", "world"], ["python", "test"], ["string", "operations"]]
        assert result == expected
        assert isinstance(result, list)
        
        # Check Series
        result = ts.str_split(SERIES_STR, " ")
        for i, split_list in enumerate(expected):
            assert result[i] == split_list
        assert isinstance(result, pd.Series)
    
        # Check with maxsplit parameter
        result = ts.str_split("a b c d", " ", 2)
        assert result == ["a", "b", "c d"]

class TestStringCaseConversion:
    """Tests for string case conversion functions."""
    
    def test_str_to_upper(self):
        # Check single string
        result = ts.str_to_upper(SINGLE_STR)
        assert result == "HELLO WORLD"
        assert isinstance(result, str)
        
        # Check list
        result = ts.str_to_upper(LIST_STR)
        expected = ["HELLO WORLD", "PYTHON TEST", "STRING OPERATIONS"]
        assert result == expected
        assert isinstance(result, list)
        
        # Check Series
        result = ts.str_to_upper(SERIES_STR)
        assert all(result == pd.Series(expected))
        assert isinstance(result, pd.Series)
    
    def test_str_to_lower(self):
        mixed_case = "HELLO World"
        mixed_list = ["HELLO World", "Python TEST", "StRiNg OpeRaTiOns"]
        mixed_series = pd.Series(mixed_list)
        
        # Check single string
        result = ts.str_to_lower(mixed_case)
        assert result == "hello world"
        assert isinstance(result, str)
        
        # Check list
        result = ts.str_to_lower(mixed_list)
        expected = ["hello world", "python test", "string operations"]
        assert result == expected
        assert isinstance(result, list)
        
        # Check Series
        result = ts.str_to_lower(mixed_series)
        assert all(result == pd.Series(expected))
        assert isinstance(result, pd.Series)
    
    def test_str_to_title(self):
        # Check single string
        result = ts.str_to_title(SINGLE_STR)
        assert result == "Hello World"
        assert isinstance(result, str)
        
        # Check list
        result = ts.str_to_title(LIST_STR)
        expected = ["Hello World", "Python Test", "String Operations"]
        assert result == expected
        assert isinstance(result, list)
        
        # Check Series
        result = ts.str_to_title(SERIES_STR)
        assert all(result == pd.Series(expected))
        assert isinstance(result, pd.Series)
        
        # Check with remove_dashes parameter
        result = ts.str_to_title("hello-world", remove_dashes=True)
        assert result == "Hello World"

class TestNewStringrFunctions:
    """Tests for new stringr functions."""
    
    def test_str_length(self):
        # Check single string
        result = ts.str_length(SINGLE_STR)
        assert result == 11
        assert isinstance(result, int)
        
        # Check list
        result = ts.str_length(LIST_STR)
        expected = [11, 11, 17]
        assert result == expected
        assert isinstance(result, list)
        
        # Check Series
        result = ts.str_length(SERIES_STR)
        assert all(result == pd.Series(expected))
        assert isinstance(result, pd.Series)
    
    def test_str_count(self):
        args = {'pattern': 'o'}
        
        # Check single string
        result = ts.str_count(SINGLE_STR, **args)
        assert result == 2
        assert isinstance(result, int)
        
        # Check list
        result = ts.str_count(LIST_STR, **args)
        expected = [2, 1, 2]
        assert result == expected
        assert isinstance(result, list)
        
        # Check Series
        result = ts.str_count(SERIES_STR, **args)
        assert all(result == pd.Series(expected))
        assert isinstance(result, pd.Series)
    
    def test_str_locate(self):
        args = {'pattern': 'o'}
        
        # Check single string
        result = ts.str_locate(SINGLE_STR, **args)
        assert result == 4  # 0-indexed position
        assert isinstance(result, int)
        
        # Check list
        result = ts.str_locate(LIST_STR, **args)
        expected = [4, 4, 12]
        assert result == expected
        assert isinstance(result, list)
        
        # Check Series
        result = ts.str_locate(SERIES_STR, **args)
        assert all(result == pd.Series(expected))
        assert isinstance(result, pd.Series)
    
    def test_str_locate_all(self):
        args = {'pattern': 'o'}
        
        # Check single string
        result = ts.str_locate_all(SINGLE_STR, **args)
        assert result == [[4, 5], [7, 8]]
        assert isinstance(result, list)
        
        # Check list
        result = ts.str_locate_all(LIST_STR, **args)
        expected = [[[4, 5], [7, 8]], [[4, 5]], [[12, 13], [14, 15]]]
        assert result == expected
        assert isinstance(result, list)
        
        # Check Series
        result = ts.str_locate_all(SERIES_STR, **args)
        for i, positions in enumerate(expected):
            assert result[i] == positions
        assert isinstance(result, pd.Series)
    
    def test_str_pad(self):
        # Check single string
        result = ts.str_pad("hello", 10)
        assert result == "  hello   "
        assert len(result) == 10
        assert isinstance(result, str)
        
        # With left side
        result = ts.str_pad("hello", 10, side="left")
        assert result == "     hello"
        assert len(result) == 10
        assert isinstance(result, str)
        
        # With right side
        result = ts.str_pad("hello", 10, side="right")
        assert result == "hello     "
        assert len(result) == 10
        assert isinstance(result, str)
        
        # With custom pad character
        result = ts.str_pad("hello", 10, pad="*")
        assert result == "**hello***"
        assert len(result) == 10
        assert isinstance(result, str)
        
        # Check list
        result = ts.str_pad(["a", "bb"], 3)
        expected = [" a ", "bb "]
        assert result == expected
        assert isinstance(result, list)
        
        # Check Series
        result = ts.str_pad(pd.Series(["a", "bb"]), 3)
        assert all(result == pd.Series(expected))
        assert isinstance(result, pd.Series)
    
    def test_str_dup(self):
        # Check single string
        result = ts.str_dup("abc", 3)
        assert result == "abcabcabc"
        assert isinstance(result, str)
        
        # Check list
        result = ts.str_dup(["a", "b"], 3)
        expected = ["aaa", "bbb"]
        assert result == expected
        assert isinstance(result, list)
        
        # Check Series
        result = ts.str_dup(pd.Series(["a", "b"]), 3)
        assert all(result == pd.Series(expected))
        assert isinstance(result, pd.Series)
    
    def test_str_squish(self):
        # Check single string
        result = ts.str_squish("  hello    world  ")
        assert result == "hello world"
        assert isinstance(result, str)
        
        # Check list
        result = ts.str_squish(["  a  b  ", " c   d "])
        expected = ["a b", "c d"]
        assert result == expected
        assert isinstance(result, list)
        
        # Check Series
        result = ts.str_squish(pd.Series(["  a  b  ", " c   d "]))
        assert all(result == pd.Series(expected))
        assert isinstance(result, pd.Series)
    
    def test_str_wrap(self):
        # Check single string
        result = ts.str_wrap("This is a long string that needs to be wrapped.", width=20)
        expected = "This is a long\nstring that needs to\nbe wrapped."
        assert result == expected
        assert isinstance(result, str)
        
        # With indent
        result = ts.str_wrap("This is a test.", width=20, indent=2)
        expected = "  This is a test."
        assert result == expected
        assert isinstance(result, str)
        
        # With exdent
        long_text = "This is a longer test that will need to be wrapped to multiple lines."
        result = ts.str_wrap(long_text, width=20, exdent=2)
        lines = result.split("\n")
        assert lines[0].startswith("This is a longer")
        assert lines[1].startswith("  test that will")
        assert isinstance(result, str)
        
        # Check list and Series
        # Just verify return types as textwrap behavior testing is complex
        result = ts.str_wrap(["Short text", "This is longer text that should wrap"], width=10)
        assert isinstance(result, list)
        
        result = ts.str_wrap(pd.Series(["Short text", "This is longer text that should wrap"]), width=10)
        assert isinstance(result, pd.Series)

class TestUtilityFunctions:
    """Tests for utility functions."""
    
    def test_str_concat(self):
        # Single strings
        result = ts.str_concat("hello", "world")
        assert result == "hello_world"
        assert isinstance(result, str)
        
        # With custom separator
        result = ts.str_concat("hello", "world", sep="-")
        assert result == "hello-world"
        assert isinstance(result, str)
        
        # Series concatenation
        s1 = pd.Series(["a", "b"])
        s2 = pd.Series(["c", "d"])
        result = ts.str_concat(s1, s2)
        expected = pd.Series(["a_c", "b_d"])
        assert all(result == expected)
        assert isinstance(result, pd.Series)
        
        # DataFrame column concatenation
        df = pd.DataFrame({"col1": ["a", "b"], "col2": ["c", "d"]})
        result = ts.str_concat(df, "col1", "col2")
        expected = pd.Series(["a_c", "b_d"])
        assert all(result == expected)
        assert isinstance(result, pd.Series)
    
    def test_str_dash_to_space(self):
        # Check single string
        result = ts.str_dash_to_space("hello-world")
        assert result == "hello world"
        assert isinstance(result, str)
        
        # With underscore
        result = ts.str_dash_to_space("hello_world")
        assert result == "hello world"
        assert isinstance(result, str)
        
        # With custom dashes
        result = ts.str_dash_to_space("hello.world", dashes=["."])
        assert result == "hello world"
        assert isinstance(result, str)
        
        # Check list
        result = ts.str_dash_to_space(["hello-world", "python_test"])
        expected = ["hello world", "python test"]
        assert result == expected
        assert isinstance(result, list)
        
        # Check Series
        result = ts.str_dash_to_space(pd.Series(["hello-world", "python_test"]))
        assert all(result == pd.Series(expected))
        assert isinstance(result, pd.Series)
    
    def test_str_upper_cut(self):
        # Check single string
        result = ts.str_upper_cut("hello")
        assert result == "Hello"
        assert isinstance(result, str)
        
        # With n parameter
        result = ts.str_upper_cut("hello", n=2)
        assert result == "HEllo"
        assert isinstance(result, str)
        
        # Check list
        result = ts.str_upper_cut(["hello", "world"], n=2)
        expected = ["HEllo", "WOrld"]
        assert result == expected
        assert isinstance(result, list)
        
        # Check Series
        result = ts.str_upper_cut(pd.Series(["hello", "world"]), n=2)
        assert all(result == pd.Series(expected))
        assert isinstance(result, pd.Series)
    
    def test_str_search_apply(self):
        # Check single string
        result = ts.str_search_apply("hello world", r"\w+", lambda x: x.upper())
        assert result == "HELLO WORLD"
        assert isinstance(result, str)
        
        # Check list
        result = ts.str_search_apply(["hello", "world"], r"\w+", lambda x: x.upper())
        expected = ["HELLO", "WORLD"]
        assert result == expected
        assert isinstance(result, list)
        
        # Check Series
        result = ts.str_search_apply(pd.Series(["hello", "world"]), r"\w+", lambda x: x.upper())
        assert all(result == pd.Series(expected))
        assert isinstance(result, pd.Series)
    
    def test_str_search_recase(self):
        # Check single string with upper case
        result = ts.str_search_recase("hello world", r"\w+", "upper")
        assert result == "HELLO WORLD"
        assert isinstance(result, str)
        
        # With camelcase
        result = ts.str_search_recase("hello_world", r"\w+", "camelcase")
        assert result == "HelloWorld"
        assert isinstance(result, str)
        
        # With snakecase
        result = ts.str_search_recase("helloWorld", r"\w+", "snakecase")
        assert result == "hello_world"
        assert isinstance(result, str)
        
        # Check list
        result = ts.str_search_recase(["hello", "world"], r"\w+", "upper")
        expected = ["HELLO", "WORLD"]
        assert result == expected
        assert isinstance(result, list)
        
        # Check Series
        result = ts.str_search_recase(pd.Series(["hello", "world"]), r"\w+", "upper")
        assert all(result == pd.Series(expected))
        assert isinstance(result, pd.Series)

# Additional test cases can be added for edge cases, error handling, etc.