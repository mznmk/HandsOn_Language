import unittest
import script


class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_input(self):
        result = script.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = script.run_guess(5, 3)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = script.run_guess(3, 11)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = script.run_guess(3, "11")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
