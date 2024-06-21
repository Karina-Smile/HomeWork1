from typing import Any

def get_mask_card_number(card_number: str) -> Any:
    """Маскировка номера карты"""
    masked_card_list = []
    masked_card = card_number[:6] + "******" + card_number[-4:]

    for num in range(0, len(masked_card), 4):
        masked_card_list.append(masked_card[num: num + 4])

    return " ".join(masked_card_list)


def get_mask_account(account: str) -> Any:
    """Маскировка номера счета"""
    return "**" + account[-4:]
