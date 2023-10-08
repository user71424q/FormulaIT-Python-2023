# TODO Найдите количество книг, которое можно разместить на дискете
WEIGHT = 1.44 * 1024 * 1024
PAGES = 100
LINES = 50
SYMBOLS = 25
WEIGHT_PER_SYMBOL = 4
res = WEIGHT // (WEIGHT_PER_SYMBOL * SYMBOLS * LINES * PAGES)
print("Количество книг, помещающихся на дискету:", int(res))
