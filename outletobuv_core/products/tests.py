from django.test import TestCase

# Create your tests here.
import re

# Ваша строка
s = '"9142";"Обувь,БОСОНОЖКИ";72;5;"замш ";"БОСОНОЖКИ бордвые замш 9142 Пекин, Китай 35(р)";"Пекин, Китай";"35";"";50;"бордвые";3990'
s = s.split(';')
print(s)
# Регулярное выражение для извлечения текста в кавычках
pattern = '"(.+?)"'

# Находим все совпадения с помощью re.findall
matches = re.findall(pattern, s)

# Выводим совпадения
for match in matches:
    print(match)