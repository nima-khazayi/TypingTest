import pytest
from unittest.mock import patch
from io import StringIO
import project


def test_clear():
    assert project.clear() is None


def test_colorized_message():
    assert project.colorized_message("Hello", color="white") is None
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
def test_include_upper(mock_root, mock_input, user_input, original_text, expected_text):
    mock_input.return_value = user_input
    # Include additional arguments height, width, num, and n as per project.py
    project.include_upper(original_text, 24, 80, 30, 5)
    mock_root.assert_called_once_with(expected_text, 24, 80, 30, 5, user_input)

    if user_input == "n":
        assert expected_text.islower()
    elif user_input == "y":
        assert any(c.isupper() for c in expected_text)


@patch("builtins.input", side_effect=["40", "5"])
@patch("project.sample_words")
def test_get_valid_input(mock_sample_words, mock_input):
    assert project.get_valid_input() is None
    assert mock_sample_words.called


def test_enterance():
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        project.enterance()
        output = mock_stdout.getvalue()

    # Print the output for debugging purposes
    print(output)  # This will help you see the exact output format

    # Split the output into lines for more granular checks
    output_lines = output.splitlines()

    # Check for specific characteristics of the ASCII art
    assert any("______" in line for line in output_lines)  # Check for the top line of ASCII art
    assert "________________________________________" in output  # Check for the line separator

    # Optional: Check if the output has leading whitespace (if needed)
    assert output[0].isspace()  # Check if the first character is a whitespace character