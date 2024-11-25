from vanity_plates import Plates
import pytest
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