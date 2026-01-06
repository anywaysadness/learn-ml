import pandas as pd

df = pd.read_csv("train.csv")
rows, _ = df.shape
print(f"Строк до: {rows}")

# Что нужно сделать:
# Удалите строки с пропусками в Embarked
df = df.dropna(subset=["Embarked"])

# Заполните Age медианой
df = df.fillna(df["Age"].median())

# Закодируйте Sex (male=1, female=0).
df["Sex"] = df["Sex"].map({"male": 1, "female": 0})

# Выведите строки до/после, пропуски после
rows, _ = df.shape
print(f"Строк после: {rows}")
print(f"Пропуски после:\n{df.isna().sum()}")
