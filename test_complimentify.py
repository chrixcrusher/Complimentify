import pytest  # Importing the pytest module for testing
from unittest import mock  # Importing mock from unittest to create mock objects
from complimentify import (  # Importing the functions to be tested from the complimentify module
    get_random_greeting, get_random_no_response, get_random_compliment, prompt_user
)

def test_get_random_greeting(mocker):
    mock_conn = mocker.patch('sqlite3.connect')  # Mocking the sqlite3.connect function
    mock_cursor = mocker.Mock()  # Creating a mock cursor object
    mock_conn.return_value.cursor.return_value = mock_cursor  # Setting the cursor method to return the mock cursor
    mock_cursor.fetchone.return_value = ["Hello"]  # Setting the fetchone method of the cursor to return a mock value

    assert get_random_greeting() == "Hello"  # Asserting that get_random_greeting returns the expected value

def test_get_random_no_response(mocker):
    mock_conn = mocker.patch('sqlite3.connect')  # Mocking the sqlite3.connect function
    mock_cursor = mocker.Mock()  # Creating a mock cursor object
    mock_conn.return_value.cursor.return_value = mock_cursor  # Setting the cursor method to return the mock cursor
    mock_cursor.fetchone.return_value = ["No worries!"]  # Setting the fetchone method of the cursor to return a mock value

    assert get_random_no_response() == "No worries!"  # Asserting that get_random_no_response returns the expected value

def test_get_random_compliment(mocker):
    mock_conn = mocker.patch('sqlite3.connect')  # Mocking the sqlite3.connect function
    mock_cursor = mocker.Mock()  # Creating a mock cursor object
    mock_conn.return_value.cursor.return_value = mock_cursor  # Setting the cursor method to return the mock cursor
    mock_cursor.fetchone.return_value = ["You are amazing!"]  # Setting the fetchone method of the cursor to return a mock value

    assert get_random_compliment() == "you are amazing!"  # Asserting that get_random_compliment returns the expected value in lowercase

def test_prompt_user(mocker):
    # Test case where the first response is valid
    mocker.patch('builtins.input', side_effect=["yes"])  # Mocking the input function to return "yes"
    assert prompt_user("Are you okay? (yes/no): ", ["yes", "no"]) == "yes"  # Asserting that prompt_user returns "yes" for valid input

    # Test case where the first response is invalid, followed by a valid response
    mocker.patch('builtins.input', side_effect=["maybe", "no"])  # Mocking the input function to return "maybe" then "no"
    assert prompt_user("Are you okay? (yes/no): ", ["yes", "no"]) == "no"  # Asserting that prompt_user returns "no" after an invalid response

    # Test case where multiple invalid responses are given before a valid response
    mocker.patch('builtins.input', side_effect=["maybe", "not sure", "yes"])  # Mocking the input function to return "maybe", "not sure", then "yes"
    assert prompt_user("Are you okay? (yes/no): ", ["yes", "no"]) == "yes"  # Asserting that prompt_user returns "yes" after multiple invalid responses

    # Test case where multiple invalid responses are given before a valid response
    mocker.patch('builtins.input', side_effect=["maybe", "not sure", "no"])  # Mocking the input function to return "maybe", "not sure", then "no"
    assert prompt_user("Are you okay? (yes/no): ", ["yes", "no"]) == "no"  # Asserting that prompt_user returns "no" after multiple invalid responses
