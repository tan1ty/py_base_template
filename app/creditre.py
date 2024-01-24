import re


def is_valid_input(card):
    pattern = re.compile(r"^\d{13}(\d{2}(\d{1})?)?$")
    return bool(pattern.match(card))


def determine_card(card):
    service = ""
    if card[0] == "4":
        service = "VISA"
    elif card[0] == "5" and (card[1]) in ["1", "2", "3", "4", "5"]:
        service = "MASTERCARD"
    elif card[0] == "3" and (card[1]) in ["4", "7"]:
        service = "AMEX"
    return service


def is_valid_card(card):
    first_part_of_sum = [
        int(c) for c in list("".join([str((int(c) * 2)) for c in list(card[-2::-2])]))
    ]
    second_part_of_sum = [int(c) for c in [str(int(c)) for c in list(card[-1::-2])]]
    total_sum = sum(first_part_of_sum + second_part_of_sum)
    if total_sum % 10 == 0:
        return True
    else:
        return False


def check_card():
    card = input("Type card number: ")
    valid = is_valid_input(card)
    if valid and is_valid_card(card):
        service = determine_card(card)
        print(service if service else "INVALID")
    else:
        print("INVALID")


check_card()
