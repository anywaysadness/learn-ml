import pandas as pd
# Загружаем датасет Titanic
df = pd.read_csv('train.csv')
# Метод read_csv() читает CSV-файл в DataFrame — таблицу pandas.
# 'train.csv' — путь к файлу, который вы скачали с Kaggle.

# Смотрим первые 5 строк
print(df.head())
# Метод head() показывает первые n строк (по умолчанию 5).
# Вывод: таблица с PassengerId, Survived, Pclass, Name, Sex, Age и др.

# Проверяем пропуски
print(df.isna().sum())
# Метод isna() создает таблицу True/False (True, если NaN).
# sum() подсчитывает True (NaN) по каждому столбцу.
# Вывод: Age: 177, Cabin: 687, Embarked: 2.

# Заполняем пропуски в Age медианой
median_age = df['Age'].median()
# median() вычисляет медиану — значение, делящее данные пополам.
# Для Age это ~30 (половина пассажиров младше, половина старше).
df['Age'] = df['Age'].fillna(median_age)
# fillna(x) заменяет NaN на x. Здесь NaN в Age становятся 30.

# Кодируем Sex
df['Sex'] = df['Sex'].map({'male': 1, 'female': 0})
# map() применяет словарь к столбцу: male → 1, female → 0.

# Удаляем строки, где пропущен Embarked
df = df.dropna(subset=['Embarked'])
# dropna() удаляет строки/столбцы с NaN.
# subset=['Embarked'] указывает, что проверяем только этот столбец.
print(df.shape)  # Вывод: (889, 12) — 2 строки удалены.