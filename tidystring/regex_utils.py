"""
Regular expression utilities for tidystring.

This module provides helper functions to simplify the creation and use of
regular expressions with tidystring functions.
"""

import re


def re_literal(text):
    """
    Escape a string to be used as a literal in a regular expression.

    Args:
        text (str): The text to escape

    Returns:
        str: The escaped string

    Examples:
        >>> re_literal('hello.world')
        'hello\\.world'
        >>> re_literal('a+b*c?')
        'a\\+b\\*c\\?'
    """
    return re.escape(text)


def re_or(*patterns):
    """
    Combine multiple patterns with OR logic.

    Args:
        *patterns: Variable number of patterns to combine

    Returns:
        str: Pattern that matches any of the input patterns

    Examples:
        >>> re_or('cat', 'dog', 'bird')
        'cat|dog|bird'
        >>> re_or('\\d+', '[A-Z]+', '\\w{3}')
        '\\d+|[A-Z]+|\\w{3}'
    """
    return "|".join(patterns)


def re_either(left, right):
    """
    Create a pattern matching either the left or right pattern.

    Args:
        left (str): The left pattern
        right (str): The right pattern

    Returns:
        str: Pattern that matches either left or right

    Examples:
        >>> re_either('cat', 'dog')
        'cat|dog'
    """
    return f"{left}|{right}"


def re_not_chars(chars):
    """
    Create a pattern matching any character not in the given set.

    Args:
        chars (str): Characters to exclude

    Returns:
        str: Pattern matching any character not in chars

    Examples:
        >>> re_not_chars('aeiou')
        '[^aeiou]'
    """
    return f"[^{re_literal(chars)}]"


def re_chars(chars):
    """
    Create a pattern matching any character in the given set.

    Args:
        chars (str): Characters to include

    Returns:
        str: Pattern matching any character in chars

    Examples:
        >>> re_chars('aeiou')
        '[aeiou]'
    """
    return f"[{re_literal(chars)}]"


def re_digit():
    """
    Return a pattern matching any digit character.

    Returns:
        str: Pattern matching any digit

    Examples:
        >>> re_digit()
        '\\d'
    """
    return r"\d"


def re_word():
    """
    Return a pattern matching any word character (letter, digit, underscore).

    Returns:
        str: Pattern matching any word character

    Examples:
        >>> re_word()
        '\\w'
    """
    return r"\w"


def re_space():
    """
    Return a pattern matching any whitespace character.

    Returns:
        str: Pattern matching any whitespace character

    Examples:
        >>> re_space()
        '\\s'
    """
    return r"\s"


def re_any():
    """
    Return a pattern matching any character except newline.

    Returns:
        str: Pattern matching any character

    Examples:
        >>> re_any()
        '.'
    """
    return r"."


def re_start():
    """
    Return a pattern matching the start of a string.

    Returns:
        str: Pattern matching start of string

    Examples:
        >>> re_start()
        '^'
    """
    return r"^"


def re_end():
    """
    Return a pattern matching the end of a string.

    Returns:
        str: Pattern matching end of string

    Examples:
        >>> re_end()
        '$'
    """
    return r"$"


def re_boundary():
    """
    Return a pattern matching a word boundary.

    Returns:
        str: Pattern matching a word boundary

    Examples:
        >>> re_boundary()
        '\\b'
    """
    return r"\b"


def re_zero_or_more(pattern):
    """
    Create a pattern matching zero or more occurrences of the input pattern.

    Args:
        pattern (str): The pattern

    Returns:
        str: Pattern matching zero or more occurrences

    Examples:
        >>> re_zero_or_more('a')
        'a*'
        >>> re_zero_or_more('[abc]')
        '[abc]*'
    """
    return f"{pattern}*"


def re_one_or_more(pattern):
    """
    Create a pattern matching one or more occurrences of the input pattern.

    Args:
        pattern (str): The pattern

    Returns:
        str: Pattern matching one or more occurrences

    Examples:
        >>> re_one_or_more('a')
        'a+'
        >>> re_one_or_more('[abc]')
        '[abc]+'
    """
    return f"{pattern}+"


def re_optional(pattern):
    """
    Create a pattern matching zero or one occurrence of the input pattern.

    Args:
        pattern (str): The pattern

    Returns:
        str: Pattern matching zero or one occurrence

    Examples:
        >>> re_optional('a')
        'a?'
        >>> re_optional('[abc]')
        '[abc]?'
    """
    return f"{pattern}?"


def re_repeat(pattern, n):
    """
    Create a pattern matching exactly n occurrences of the input pattern.

    Args:
        pattern (str): The pattern
        n (int): Number of repetitions

    Returns:
        str: Pattern matching exactly n occurrences

    Examples:
        >>> re_repeat('a', 3)
        'a{3}'
        >>> re_repeat('[abc]', 5)
        '[abc]{5}'
    """
    return f"{pattern}{{{n}}}"


def re_repeat_range(pattern, min_count, max_count=None):
    """
    Create a pattern matching between min and max occurrences of the input pattern.

    Args:
        pattern (str): The pattern
        min_count (int): Minimum number of repetitions
        max_count (int, optional): Maximum number of repetitions. Defaults to None.

    Returns:
        str: Pattern matching specified range of occurrences

    Examples:
        >>> re_repeat_range('a', 2, 4)
        'a{2,4}'
        >>> re_repeat_range('[abc]', 3)
        '[abc]{3,}'
    """
    if max_count is None:
        return f"{pattern}{{{min_count},}}"
    return f"{pattern}{{{min_count},{max_count}}}"


def re_capture(pattern):
    """
    Create a capturing group containing the input pattern.

    Args:
        pattern (str): The pattern to capture

    Returns:
        str: Capturing group

    Examples:
        >>> re_capture('\\w+')
        '(\\w+)'
    """
    return f"({pattern})"


def re_group(pattern):
    """
    Create a non-capturing group containing the input pattern.

    Args:
        pattern (str): The pattern to group

    Returns:
        str: Non-capturing group

    Examples:
        >>> re_group('\\w+')
        '(?:\\w+)'
    """
    return f"(?:{pattern})"


def re_lookahead(pattern):
    """
    Create a positive lookahead assertion for the input pattern.

    Args:
        pattern (str): The pattern to look ahead for

    Returns:
        str: Positive lookahead assertion

    Examples:
        >>> re_lookahead('\\d+')
        '(?=\\d+)'
    """
    return f"(?={pattern})"


def re_negative_lookahead(pattern):
    """
    Create a negative lookahead assertion for the input pattern.

    Args:
        pattern (str): The pattern to not look ahead for

    Returns:
        str: Negative lookahead assertion

    Examples:
        >>> re_negative_lookahead('\\d+')
        '(?!\\d+)'
    """
    return f"(?!{pattern})"


def re_whole_word(word):
    """
    Create a pattern matching a whole word.

    Args:
        word (str): The word to match

    Returns:
        str: Pattern matching the whole word

    Examples:
        >>> re_whole_word('hello')
        '\\bhello\\b'
    """
    return f"\\b{re_literal(word)}\\b"


def re_starts_with(pattern):
    """
    Create a pattern matching a string starting with the input pattern.

    Args:
        pattern (str): The pattern that should start the string

    Returns:
        str: Pattern matching a string starting with pattern

    Examples:
        >>> re_starts_with('hello')
        '^hello'
    """
    return f"^{pattern}"


def re_ends_with(pattern):
    """
    Create a pattern matching a string ending with the input pattern.

    Args:
        pattern (str): The pattern that should end the string

    Returns:
        str: Pattern matching a string ending with pattern

    Examples:
        >>> re_ends_with('world')
        'world$'
    """
    return f"{pattern}$"


def re_word_list(words):
    """
    Create a pattern matching any word from a list of words.

    Args:
        words (list): List of words to match

    Returns:
        str: Pattern matching any of the provided words

    Examples:
        >>> re_word_list(['cat', 'dog', 'bird'])
        '\\b(cat|dog|bird)\\b'
    """
    escaped_words = [re_literal(word) for word in words]
    return f"\\b({re_or(*escaped_words)})\\b"


def re_date():
    """
    Return a pattern matching common date formats (YYYY-MM-DD or MM/DD/YYYY).

    Returns:
        str: Pattern matching common date formats

    Examples:
        >>> re_date()
        '\\b(\\d{4}-\\d{2}-\\d{2}|\\d{1,2}/\\d{1,2}/\\d{4})\\b'
    """
    return r"\b(\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}/\d{4})\b"


def re_time():
    """
    Return a pattern matching common time formats (HH:MM:SS or HH:MM).

    Returns:
        str: Pattern matching common time formats

    Examples:
        >>> re_time()
        '\\b([01]?\\d|2[0-3]):[0-5]\\d(:[0-5]\\d)?\\b'
    """
    return r"\b([01]?\d|2[0-3]):[0-5]\d(:[0-5]\d)?\b"


def re_email():
    """
    Return a pattern matching common email address formats.

    Returns:
        str: Pattern matching email addresses

    Examples:
        >>> re_email()
        '\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b'
    """
    return r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"


def re_url():
    """
    Return a pattern matching common URL formats.

    Returns:
        str: Pattern matching URLs

    Examples:
        >>> re_url()
        'https?://[\\w.-]+\\.\\w+(/[\\w./\\-?=&%]*)?'
    """
    return r"https?://[\w.-]+\.\w+(/[\w./\-?=&%]*)?"


def re_phone_us():
    """
    Return a pattern matching US phone number formats.

    Returns:
        str: Pattern matching US phone numbers

    Examples:
        >>> re_phone_us()
        '\\b(\\+?1[-.])?\\(?\\d{3}\\)?[-.]?\\d{3}[-.]?\\d{4}\\b'
    """
    return r"\b(\+?1[-.])?\\?\d{3}\\?[-.]?\d{3}[-.]?\d{4}\b"
