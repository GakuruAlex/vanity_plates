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