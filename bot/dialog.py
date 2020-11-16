def dialog():
    yes_need = yield from ask_yes_or_no("Добрый день, вечер, ночь или утро.\n"
                                        "Нужна вам незамерзайка?(незамерзающая стеклоомывающая жидкость).\n"
                                        "Я ваш персональный менеджер и готов принять Ваш заказ.")
    if yes_need:
        answer = yield from order()


def ask_yes_or_no(question):
    answer = yield question
    while not ("да" in answer.text.lower() or "нет" in answer.text.lower()):
        answer = yield "Так да или нет?"
    return "да" in answer.text.lower()


def order():
    return "Давайте познакомимся и определим Ваши пожелания."
