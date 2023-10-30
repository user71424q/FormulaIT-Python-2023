def find_common_participants(first_group, second_group, sep=','):
    set1 = set(first_group.split(sep))
    set2 = set(second_group.split(sep))
    common = list(set1.intersection(set2))
    common.sort()
    return common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
