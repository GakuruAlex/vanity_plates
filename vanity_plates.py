import string
class Plates:
    def is_alpha_num(self, plate):
        return any(plate.isalpha() for plate in plate) and any(plate.isdigit() for plate in plate)
    def contains_digits(self, plate):
        return any(plate.isdigit() for plate in plate)
    def is_first_digit_zero(self, plate):
        if not plate.isalpha():
            for char in plate:
                if char.isdigit():
                    return int(char) == 0
        return False
    def begins_with_two_letters(self, plate):
        return plate[:2].isalpha()
    def is_length_valid(self, plate):
        return len(plate) >  1 and len(plate) < 7
    def is_int_in_middle(self, plate):
        if self.is_alpha_num(plate):
            if plate[0].isalpha() and plate[-1].isalpha():
                return self.contains_digits(plate[1:-2])
            else:
                return False
        else:
            return False

    def no_period_punctuation(self, plate):
        return True not in [char in string.punctuation and char in string.whitespace for char in plate]
    def is_valid(self, plate):
        if self.is_length_valid(plate):
            if self.is_alpha_num(plate):
                return self.begins_with_two_letters(plate) and self.is_int_in_middle(plate) and self.no_period_punctuation(plate)
            else:
                return self.no_period_punctuation(plate)
        else:
            return False

    def main(self):
        plate = input("Plate: ")
        if self.is_valid(plate):
            print("Valid")
        else:
            print("Invalid")

if __name__ =="__main__":
    plates = Plates()
    plates.main()
