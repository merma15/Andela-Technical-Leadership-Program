import json


def main():
    # Список словарей содержит данные о каждом МППР, который определяется
    # состояниями, действиями, вероятностями перехода и вознаграждениями.
    with open('mdps.json', "r") as f:
        mdps = json.load(f)
    print(mdps[0])
    # {'0': {'0': [{'probability': 1.0, 'next_state': '1', 'reward': -0.46}], ...

    # Словарь определяющий полезность каждого действия, жадная стратегия на его основе
    # используется для управления системой. Формат состояние -> действие -> полезность.
    with open('q_tables.json', "r") as f:
        q_tables = json.load(f)
    print(q_tables[0])
    # {'0': {'0': 1.5069852597037479, '1': 0.9969852597037479},
    # '1': {'0': 2.186286733733373, '1': 1.816286733733373}}

    # Список изменений для одной пары состояния-действия каждого МППР,
    # которые необходимо произвести.
    with open('submit.json', "r") as f:
        submit = json.load(f)
    print(submit[0])

    # {'state': '0', 'action': '0', 'value': -5}

    def create_dummy_answer(q_table_):
        # Выбираем первое состояние словаря и
        # присваиваем -1 его самому полезному действию.
        state, actions = next(iter(q_table_.items()))
        max_action = max(actions, key=actions.get)
        return {'state': state, 'action': max_action, 'value': -1}

    answers = []
    for q_table in q_tables:
        answers.append(create_dummy_answer(q_table))

    # Записываем ответы в файл.
    with open("submit.json", "w") as f:
        json.dump(answers, f)


if __name__ == '__main__':
    main()
