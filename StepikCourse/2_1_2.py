import pandas as pd

df = pd.read_csv("train.csv")

# Что нужно сделать:
# Выведите первые 5 строк
print(f"Первые 5 строк:\n{df.head(5)}\n")

# Выведите число строк/столбцов
rows, cols = df.shape
print(f"Размер: {rows} x {cols}\n")

# Выведите типы данных
dtypes = df.dtypes
print(f"Типы данных:\n{dtypes}\n")

# Выведите пропуски
nan = df.isna().sum()
print(f"Пропуски:\n{nan}\n")

# Найдите средний Age и медиану Fare
age_average = df["Age"].mean()
fare_mediana = df["Fare"].median()
print(f"Средний возвраст: {age_average:.2f} \nМедиана Fare: {fare_mediana:.2f}")
