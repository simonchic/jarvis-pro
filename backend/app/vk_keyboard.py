import json


def get_main_keyboard():
    keyboard = {
        "one_time": False,
        "buttons": [
            [
                {
                    "action": {
                        "type": "text",
                        "label": "📥 Подать заявку"
                    },
                    "color": "primary"
                }
            ],
            [
                {
                    "action": {
                        "type": "text",
                        "label": "💰 Рассчитать стоимость"
                    },
                    "color": "positive"
                }
            ],
            [
                {
                    "action": {
                        "type": "text",
                        "label": "📞 Связаться"
                    },
                    "color": "secondary"
                }
            ]
        ]
    }

    return json.dumps(keyboard, ensure_ascii=False)