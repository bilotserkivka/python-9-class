password = ''  # Ініціюємо змінну password пустим рядком (змінну не можна використати в порівннянні доки її не існує)

while password != '123':  # Перевірка умови циклу (змінна password не рівна '123')
    password = input('Ведіть пароль: ')  # Тіло циклу яке буде повторюватись доки умова циклу не стане хибною

print('Вітаю, вам відкрито доступ')  # Те, що виконається після того, як цикл завершиться
