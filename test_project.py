import pytest
from unittest.mock import patch
import project


def test_clear():
    assert project.clear() is None


def test_colorized_message_white():
    assert project.colorized_message("Hello", color="white") is None


def test_colorized_message_colored():
    assert project.colorized_message("Hello", color="cyan") is None


@pytest.mark.parametrize(
    "user_input,original_text,expected_text",
    [
        ("n", "TeSt", "test"),   # should be all lowercase
        ("y", "TeSt", "TeSt")    # should retain original case
    ]
)
@patch("builtins.input")
@patch("project.root")
def test_includ_upper(mock_root, mock_input, user_input, original_text, expected_text):
    mock_input.return_value = user_input
    project.includ_upper(original_text, 24, 80)
    mock_root.assert_called_once_with(expected_text, 24, 80)

    if user_input == "n":
        assert expected_text.islower()
    elif user_input == "y":
        assert any(c.isupper() for c in expected_text)


@patch("builtins.input", side_effect=["40", "5"])
@patch("project.sample_words")
def test_get_valid_input(mock_sample_words, mock_input):
    assert project.get_valid_input() is None
    assert mock_sample_words.called
