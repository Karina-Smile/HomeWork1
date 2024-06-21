from typing import Any
import datetime

from .masks import get_mask_card_number, get_mask_account

def mask_account_card(card: str) -> str:
    """Функция которая маскирует номер карты и счет"""
    number_card = ""
    name_card = ""
    for num in card:
        if num.isalpha():
            name_card += num
        elif num.isdigit():
            number_card += num
    if len(number_card) == 16:
        result_card = get_mask_card_number(number_card))
    else:
        result_card = get_mask_account(name_card))

    return str(name_card + " " + result_card)

def get_data (date: str) -> str:
    """Функция преобразования даты"""
    date_obj = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
    date_new = date_obj.strptime("%d.%m.%Y")

    return date_new





