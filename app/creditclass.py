import re


class CreditCard:
    def __init__(self, card_number):
        self.card_number = card_number

    def is_valid_input(self):
        pattern = re.compile(r"^\d{13}(\d{2}(\d{1})?)?$")
        return bool(pattern.match(self.card_number))

    def determine_card(self):
        service = ""
        if self.card_number[0] == "4":
            service = "VISA"
        elif self.card_number[0] == "5" and (self.card_number[1]) in [
            "1",
            "2",
            "3",
            "4",
            "5",
        ]:
            service = "MASTERCARD"
        elif self.card_number[0] == "3" and (self.card_number[1]) in ["4", "7"]:
            service = "AMEX"
        return service

    def is_valid_card(self):
        first_part_of_sum = [
            int(c)
            for c in list(
                "".join([str((int(c) * 2)) for c in list(self.card_number[-2::-2])])
            )
        ]
        second_part_of_sum = [
            int(c) for c in [str(int(c)) for c in list(self.card_number[-1::-2])]
        ]
        total_sum = sum(first_part_of_sum + second_part_of_sum)
        if total_sum % 10 == 0:
            return True
        else:
            return False

    def check_card(self):
        valid = self.is_valid_input()
        if valid and self.is_valid_card():
            service = self.determine_card()
            print(service if service else "INVALID")
        else:
            print("INVALID")


if __name__ == "__main__":
    card_number = input("Type card number: ")
    card = CreditCard(card_number)
    card.check_card()
