"""
Tests for the unified cheatsheet functionality.
"""

import pandas as pd
import pytest
from tidystring import (
    get_tidystring_cheatsheet,
    get_regex_cheatsheet,
    get_input_types_cheatsheet
)

def test_get_all_functions():
    """Test getting all functions in the cheatsheet."""
    df_all = get_tidystring_cheatsheet()
    assert isinstance(df_all, pd.DataFrame)
    assert len(df_all) > 0
    assert 'Function' in df_all.columns
    assert 'Description' in df_all.columns
    assert 'Example' in df_all.columns
    assert 'Group' in df_all.columns

def test_filter_by_case_group():
    """Test filtering by 'case' group."""
    df_case = get_tidystring_cheatsheet(group='case')
    assert isinstance(df_case, pd.DataFrame)
    assert len(df_case) > 0
    assert all(df_case['Group'] == 'case')

def test_filter_by_modification_group():
    """Test filtering by 'modification' group."""
    df_mod = get_tidystring_cheatsheet(group='modification')
    assert isinstance(df_mod, pd.DataFrame)
    assert len(df_mod) > 0
    assert all(df_mod['Group'] == 'modification')

def test_regex_group_special_handling():
    """Test special handling for 'regex' group."""
    df_regex = get_tidystring_cheatsheet(group='regex')
    assert isinstance(df_regex, pd.DataFrame)
    assert len(df_regex) > 0
    assert 'Pattern' in df_regex.columns
    assert 'Description' in df_regex.columns
    assert 'Example' in df_regex.columns

def test_input_types_group_special_handling():
    """Test special handling for 'input_types' group."""
    df_input = get_tidystring_cheatsheet(group='input_types')
    assert isinstance(df_input, pd.DataFrame)
    assert len(df_input) > 0
    assert 'Input Type' in df_input.columns
    assert 'Example Input' in df_input.columns
    assert 'Example Function' in df_input.columns
    assert 'Example Output' in df_input.columns
    assert 'Notes' in df_input.columns

def test_regex_cheatsheet():
    """Test the regex cheatsheet function."""
    df_regex = get_regex_cheatsheet()
    assert isinstance(df_regex, pd.DataFrame)
    assert len(df_regex) > 0
    assert 'Pattern' in df_regex.columns
    assert 'Description' in df_regex.columns
    assert 'Example' in df_regex.columns

def test_input_types_cheatsheet():
    """Test the input types cheatsheet function."""
    df_input = get_input_types_cheatsheet()
    assert isinstance(df_input, pd.DataFrame)
    assert len(df_input) > 0
    assert 'Input Type' in df_input.columns
    assert 'Example Input' in df_input.columns
    assert 'Example Function' in df_input.columns
    assert 'Example Output' in df_input.columns
    assert 'Notes' in df_input.columns

def test_invalid_group_raises_error():
    """Test that an invalid group name raises a ValueError with helpful message."""
    with pytest.raises(ValueError) as excinfo:
        get_tidystring_cheatsheet(group='invalid_group')
    
    # Check the error message contains useful information
    error_msg = str(excinfo.value)
    assert 'Invalid group' in error_msg
    assert 'invalid_group' in error_msg
    assert 'Valid options are:' in error_msg
    assert 'basic' in error_msg
    assert 'case' in error_msg
    assert 'regex' in error_msg
    assert 'input_types' in error_msg