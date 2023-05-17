"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def zadacha(messages):

    from collections import Counter
    ab = Counter(i['sent_by'] for i in messages).most_common(1)
    print(f'Больше всего сообщений написал пользователь ID - {ab[0][0]}') # ответ на первый вопрос

    ac = Counter(i['reply_for'] for i in messages).most_common(2)
    print(f'Больше всего ответов - {ac[1][0]}')
    for i in messages:
        if i['id'] == ac[1][0]:
            print(f"{i['sent_by']} айди пользователя, на сообщения которого больше всего отвечали") # ответ на второй вопрос
    az = {}
    for i in messages:
        # print(i['id'], i['reply_for'])
        # print(i['sent_by'], i['seen_by'])
        if i['sent_by'] not in az:
            az[i['sent_by']] = i['seen_by']
        else:
            az[i['sent_by']] = az[i['sent_by']] + i['seen_by']
    print(az)
    for k, value in az.items():
        print(k, len(set(value))) # решение на 3 задачу


if __name__ == "__main__":
    print(generate_chat_history())
    zadacha(generate_chat_history())
