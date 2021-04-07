import pytest

from utils.preprocessing_helpers import convert_to_int

def convert_to_int_ch2(integer_string_with_commas):
    if len(integer_string_with_commas) > 3 and "," not in integer_string_with_commas:
      return None
    comma_separated_parts = integer_string_with_commas.split(",")
    if not all([len(part) == 3 for part in comma_separated_parts]):
      return None
    integer_string_without_commas = "".join(comma_separated_parts)
    try:
      return integer_string_without_commas
    except ValueError:
      return None


def test_on_string_with_one_comma():
    test_argument = "2,081"
    expected = 2081
    actual = convert_to_int(test_argument)
    message = "convert_to_int('2,081') should return the int 2081, but it actually returned {0}".format(actual)
    assert actual == expected, message


def test_on_string_with_one_comma_ch2():
  test_argument = "2,081"
  expected = 2081
  actual = convert_to_int_ch2(test_argument)
  message = "convert_to_int('2,081') should return the int 2081, but it actually returned {0}".format(actual)
  assert actual == expected, message
