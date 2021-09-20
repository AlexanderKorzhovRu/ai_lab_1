import pandas

data = pandas.read_csv('https://raw.githubusercontent.com/tpo9hbi4/MachineDeepLearning/master'
                       '/introductory_laboratory_work%20('
                       '%E2%84%961)/Dataset/%D0%A2%D0%B8%D1%82%D0%B0%D0%BD%D0%B8%D0%BA.csv',
                       index_col='PassengerId')
import re


def males_count():
    # return np.count_nonzero(data.Sex == 'male')
    # return data[data.Sex == 'male'].count()
    return data.Sex.value_counts()['male']


def percent_survived_passengers():
    column_survived_count = data.Survived.count()
    survived_count = data.Survived \
        .where(data.Survived == 1) \
        .count()

    return round(survived_count * 100 / column_survived_count, 2)


def percent_passengers_in_second_class():
    column_pclass_count = data.Pclass.count()
    survived_count = data.Pclass \
        .where(data.Pclass == 2) \
        .count()

    return round(survived_count * 100 / column_pclass_count, 2)


def find_age_mean():
    return round(data.Age.mean(), 2)


def find_age_median():
    return round(data.Age.median(), 2)


def corr_between_two_columns(
        col_1: str = 'SibSp',
        col_2: str = 'Parch',
        method='pearson'):
    return round(data.corr(method=method).loc[col_1, col_2], 2)


def clean_name(name):
    # First word before comma is a surname
    s = re.search('^[^,]+, (.*)', name)
    if s:
        name = s.group(1)

    # get name from braces (if in braces)
    s = re.search('\(([^)]+)\)', name)
    if s:
        name = s.group(1)

    # Removing appeal
    name = re.sub('(Miss\. |Mrs\. |Ms\. |Dr\. )', '', name)

    # Get first left word and removing quotes
    name = name.split(' ')[0].replace('"', '')

    return name


def find_must_popular_name_by_gender(gender_key: str = 'female'):
    gender_column_name = data.Name \
        .loc[data.Sex == gender_key] \
        .apply(lambda full_name: clean_name(full_name)) \
        .value_counts()
    return gender_column_name.index[0]


print('\n1. Сколько мужчин было на корабле?')
print(males_count())

print('\n2. Какая доля пассажиров (в %) выжила?')
print(percent_survived_passengers())

print('\n3. Какая доля пассажиров (в %) от общего количества путешествовала во 2-ом классе? ')
print(percent_passengers_in_second_class())

print('\n4. Посчитайте среднее и медиану возраста всех людей на корабле.')
print(find_age_mean())
print(find_age_median())

print('\n 5. Коррелируют ли число братьев/сестер с числом родителей/детей? Посчитайте корреляцию по Пирсону между '
      'признаками SibSp и Parch датасета. ')
print(corr_between_two_columns())  # Пересечение двух областей

print('\n 6. Какое самое популярное женское имя было на корабле? Извлеките из полного имени пассажира (колонка Name) '
      'его личное имя (FirstName). ')
print(find_must_popular_name_by_gender())
