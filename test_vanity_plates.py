from vanity_plates import Plates
import pytest

# Test for the function checking for both digits and letters in plate
@pytest.mark.parametrize("plate, result", [
    ("Hello1234", True),
    ("1234", False),
    ("1234Hello", True),
    ("hello12", True)
])
class TestIsAlphaNum:
    plates = Plates()
    def test_is_alpha_num(self,plate, result)->None:
        assert self.plates.is_alpha_num(plate) == result

# Test for the begins_with_two_letters function
@pytest.mark.parametrize("plate, result", [
    ("Hello", True),
    ("123Hel", False),
    ("1234", False),
    ("Hello23", True)
])
class TestBeginsWithTwoLetters:
    plates = Plates()

    def test_begins_with_two_letters(self,plate, result)->None:
        assert self.plates.begins_with_two_letters(plate) == result

#Test for whether the length is valid
@pytest.mark.parametrize("plate, result",[
    ("Hello", True),
    ("HELLO", True),
    ("HELLOWORLD", False),
    ("helloworld", False),
    ("Hello1", True),
    ("Goodbye", False)
])
class TestIsLengthValid:
    plates = Plates()
    def test_is_length_valid(self,plate, result)->None:
        assert self.plates.is_length_valid(plate) == result

#Test for the contains digits function
@pytest.mark.parametrize("plate, result",[
    ("AAA222", True),
    ("22222", True),
    ("AAAAA", False),
    ("Hello World", False),
    ("Hel222A", True)
])
class TestContainsDigits:
    plates = Plates()
    def test_contains_digits(self, plate, result):
        assert self.plates.contains_digits(plate) == result
#Test for the is number in the middle of the plate function
@pytest.mark.parametrize("plate, result",[
    ("CS50", False),
    ("CS50P", True),
    ("AAA222", False),
    ("AAA22A", True),
])
class TestIsIntInMiddle:
    plates = Plates()
    def test_is_int_middle(self, plate, result):
        assert self.plates.is_int_in_middle(plate) == result