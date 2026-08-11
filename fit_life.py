def get_name():  # узнаём имя
    u_name = input('Укажите Ваше имя: ')
    return u_name


def get_age():  # узнаём возраст
    age_string = input('Укажите сколько Вам лет: ')
    age_raw = int(age_string)
    return age_raw


def get_height():  # узнаём рост
    height_string = input('Ваш рост: ')
    height_raw = float(height_string)
    return height_raw


def get_weight():  # узнаём вес
    weight_string = input('укажите Ваш вес в килограммах: ')
    weight_raw = float(weight_string)
    return weight_raw


# -------- знакомство --------
print('='*70)
print('Здравствуйте! Вас приветствует программа Fit Life')
print('Наш девиз: "Мы рады Вам, Вы благодарны нам"')
print('-'*70)

user_name = get_name()

print('-'*70)
print(user_name, end=', ')
print('добро пожаловать!')


user_age = get_age()

print('-'*70)
print(f'Ваш возраст {user_age}. Приятно познакомиться, {user_name}!')

# ----------- полезная информация --------------
print('Наша фитнес-программа поможет Вам укрепить и поддержать здоровье.')
print('Нам потребуются некоторые данные о Вашем физическом состоянии.')
print('-'*70)
print('Укажите рост в метрах. Используйте точку (например, 1.65).')

user_height = get_height()

print(user_name, end=', ')

user_weight = get_weight()

# ------------- рассчёты по формулам --------------------


def index_bmi(weight_kg, height_m):  # рассчитываем индекс ИМТ
    bmi_output = weight_kg / (height_m ** 2)
    bmi_round = round(bmi_output, 1)
    return bmi_round


bmi = index_bmi(user_weight, user_height)


def volume_water(weight_kg):  # рассчитываем требуемый объём воды
    water_ml = weight_kg * 30
    water_l = water_ml / 1000
    water_l_round = round(water_l)
    return water_l_round


water = volume_water(user_weight)

# ------------------ красивый отчёт ---------------------
print('='*70)
print(f'Отчёт для пользователя {user_name} (возраст: {user_age})')
print(f'Ваш Индекс Массы Тела (ИМТ): {bmi}')
print(f'Рекомендуемая норма воды: {water} л. в день')
print()
print('Расчёт окончен. Будьте здоровы!')
print('-'*70)
