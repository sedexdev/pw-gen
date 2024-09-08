"""
Test suite
"""

from src.main import gen_password, get_pw_chars


class TestPWGen:
    """
    Test cases for the functionality in main.py
    """

    @classmethod
    def setup_method(cls):
        """
        Setup method: runs before every test method in the class
        """
        cls.l = 10
        cls.n = 4
        cls.s = 2
        cls.chars = "szalyZWFRU9558>*"

    @classmethod
    def teardown_method(cls):
        """
        Teardown method: runs after every test method in the class
        """
        cls.l = None
        cls.n = None
        cls.s = None
        cls.chars = None

    def test_correct_number_of_chars(self) -> None:
        """
        Tests the correct number of chars are returned
        """
        chars = get_pw_chars(self.l, self.n, self.s)
        assert len(chars) == (self.l + self.n + self.s)

    def test_gen_password_contains_all_chars(self) -> None:
        """
        Tests the final password contains the correct characters
        """
        password = gen_password(self.chars)
        correct_chars = True
        for char in password:
            if char not in self.chars:
                correct_chars = False
        assert correct_chars

    def test_gen_password_not_equal_to_chars_string(self) -> None:
        """
        Tests that the string returned by gen_password is different from the input
        """
        password = gen_password(self.chars)
        assert self.chars != password
