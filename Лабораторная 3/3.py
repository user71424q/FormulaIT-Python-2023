# TODO  Напишите функцию count_letters
def count_letters(text):
    dict = {}
    for symbol in text.lower():
        if symbol.isalpha():
            if dict.get(symbol) is None:
                dict[symbol] = 1
            else:
                dict[symbol] += 1
    return dict


# TODO Напишите функцию calculate_frequency
def calculate_frequency(letter_dict, total_count):
    frequency_dict = {}
    for letter in letter_dict:
        frequency_dict[letter] = round(letter_dict[letter] / total_count, 2)
    return frequency_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
letter_count_dict = count_letters(main_str)
total_letter_count = 0
for char in main_str:
    if char.isalpha():
        total_letter_count += 1
frequency_dict = calculate_frequency(letter_count_dict, total_letter_count)
for letter in frequency_dict:
    print(f"{letter}: {frequency_dict[letter]:.2f}")