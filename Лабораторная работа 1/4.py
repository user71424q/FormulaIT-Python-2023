users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статистикой посещений
site_visit_logs = {"Общее количество": 0, "Уникальные посещения": 0}
site_visit_logs["Общее количество"] = len(users)
site_visit_logs["Уникальные посещения"] = len(set(users))
print(site_visit_logs)
