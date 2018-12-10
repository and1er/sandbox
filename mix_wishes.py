"""
Скрипт, в шапке которого задаётся перечень желаний в формате

<№ п.п.>. <текст желания>

На выходе в файл 'mixed_wishes.txt' записывается результат.
"""

import os
import re
import random

input_wishes = """
1. wish example 1
2. wish example 2
"""

wishes = input_wishes.strip().splitlines()
random.shuffle(wishes)

wish_regex = re.compile(r'\d+\.\s*(?P<wish>.+)')

result_wishes = list()
for idx, wish in enumerate(wishes):
    match = wish_regex.match(wish)
    if match:
        wish_text = match.group('wish')
        result_wishes.append("{}. {}\n".format(idx+1, wish_text))

with open('mixed_wishes.txt', mode='w', encoding='utf-8') as fh:
    fh.writelines(result_wishes)
