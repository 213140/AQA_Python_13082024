import unittest
from lesson_10.src.homework_10 import log_event

# Functions
def create_expected_message_for_test(username, status):
    return f"Login event - Username: {username}, Status: {status}"

def read_login_system_file():
    with open('login_system.log', 'r') as log_file:
        return log_file.read()

def clear_log_file():
    open('login_system.log', 'w').close()

class TestLogEventFunction(unittest.TestCase):

    def test_log_event_inputs(self, name, status):
        # Arrange
        clear_log_file() # Clear log file before start testing
        expected_logging_message = create_expected_message_for_test(name, status)
        # Act
        log_event(name, status)
        # Assert
        self.assertIn(expected_logging_message, read_login_system_file())


class TestLogEventFunctionInputCombinations(TestLogEventFunction):

    def test_log_event_status_success(self):
        # Use parent class for testing (with unique input data set
        self.test_log_event_inputs("user", "success")

    def test_log_event_status_expired(self):
        # Use parent class for testing (with unique input data set
        self.test_log_event_inputs("user", "expired")

    def test_log_event_status_failed(self):
        # Use parent class for testing (with unique input data set
        self.test_log_event_inputs("user", "failed")

    def test_log_event_alphabetic(self):
        # Use parent class for testing (with unique input data set
        self.test_log_event_inputs("CristianoRonaldo", "success")

    def test_log_event_name_with_special_character(self):
        # Use parent class for testing (with unique input data set
        self.test_log_event_inputs("user12:/,", "success")

if __name__ == "__main__":
    unittest.main(verbosity=3)