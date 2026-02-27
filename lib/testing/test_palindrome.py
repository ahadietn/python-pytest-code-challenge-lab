import pytest
from lib.palindrome import longest_palindromic_substring


@pytest.mark.parametrize("input_str,expected", [
    ("babad", ["bab", "aba"]),
    ("cbbd", ["bb"]),
    ("a", ["a"]),
    ("ac", ["a", "c"]),
    ("racecar", ["racecar"])
])
def test_basic_cases(input_str, expected):
    result = longest_palindromic_substring(input_str)
    assert result in expected


@pytest.mark.parametrize("input_str,expected", [
    ("", [""]),
    ("abcde", ["a","b","c","d","e"]),
    ("aaaaa", ["aaaaa"]),
    ("xyzzy", ["yzzy"]),
    ("abba", ["abba"]),
    ("a"*1000, ["a"*1000])
])
def test_edge_cases(input_str, expected):
    result = longest_palindromic_substring(input_str)
    assert result in expected

@pytest.mark.parametrize("input_str,expected", [
    ("abaac", ["aba"]),
    ("civiccar", ["civic"]),
    ("raceecar", ["ee"]),
    ("madamimadam", ["madamimadam"])
])
def test_ambiguous_cases(input_str, expected):
    result = longest_palindromic_substring(input_str)
    assert result in expected