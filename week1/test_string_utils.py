import pytest
from string_utils import (
    count_vowels, reverse_string, is_palindrome,
    word_count, capitalise_words, remove_duplicates
)

# ========== count_vowels tests ==========
def test_count_vowels_normal():
    assert count_vowels("Hello") == 2

def test_count_vowels_empty_string():
    assert count_vowels("") == 0

def test_count_vowels_no_vowels():
    assert count_vowels("xyz") == 0

def test_count_vowels_case_insensitive():
    assert count_vowels("AeIoU") == 5

def test_count_vowels_only_consonants():
    assert count_vowels("bcdfg") == 0

# ========== reverse_string tests ==========
def test_reverse_string_normal():
    assert reverse_string("abc") == "cba"

def test_reverse_string_empty():
    assert reverse_string("") == ""

def test_reverse_string_single_char():
    assert reverse_string("a") == "a"

def test_reverse_string_with_spaces():
    assert reverse_string("hello world") == "dlrow olleh"

# ========== is_palindrome tests ==========
def test_is_palindrome_true():
    assert is_palindrome("racecar") is True

def test_is_palindrome_false():
    assert is_palindrome("hello") is False

def test_is_palindrome_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") is True

def test_is_palindrome_empty():
    assert is_palindrome("") is True

def test_is_palindrome_single_char():
    assert is_palindrome("a") is True

# ========== word_count tests ==========
def test_word_count_normal():
    assert word_count("Hello World") == 2

def test_word_count_single_word():
    assert word_count("Hello") == 1

def test_word_count_empty():
    assert word_count("") == 0

def test_word_count_multiple_spaces():
    assert word_count("  Hello   World  ") == 2

def test_word_count_three_words():
    assert word_count("one two three") == 3

# ========== capitalise_words tests ==========
def test_capitalise_words_normal():
    assert capitalise_words("hello world") == "Hello World"

def test_capitalise_words_single():
    assert capitalise_words("hello") == "Hello"

def test_capitalise_words_empty():
    assert capitalise_words("") == ""

def test_capitalise_words_already_capitalised():
    assert capitalise_words("Hello World") == "Hello World"

# ========== remove_duplicates tests ==========
def test_remove_duplicates_normal():
    assert remove_duplicates("aaabbbcc") == "abc"

def test_remove_duplicates_empty():
    assert remove_duplicates("") == ""

def test_remove_duplicates_no_duplicates():
    assert remove_duplicates("abc") == "abc"

def test_remove_duplicates_long_run():
    assert remove_duplicates("aaaaabbbbbcccc") == "abc"

def test_remove_duplicates_mixed():
    assert remove_duplicates("aabbccddeeff") == "abcdef"

# ========== Exception handling tests ==========
def test_count_vowels_none_raises_typeerror():
    with pytest.raises(TypeError):
        count_vowels(None)

def test_reverse_string_none_raises_typeerror():
    with pytest.raises(TypeError):
        reverse_string(None)

def test_is_palindrome_none_raises_typeerror():
    with pytest.raises(TypeError):
        is_palindrome(None)

def test_word_count_none_raises_typeerror():
    with pytest.raises(TypeError):
        word_count(None)

def test_capitalise_words_none_raises_typeerror():
    with pytest.raises(TypeError):
        capitalise_words(None)

def test_remove_duplicates_none_raises_typeerror():
    with pytest.raises(TypeError):
        remove_duplicates(None)