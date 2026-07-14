import pandas as pd

data = {
    "Nombre": ["Julio", "Bob", None, "David"],
    "Edad": [32, None, 22, 35],
    "Ciudad": ["New York", "London", "Paris", None],
}

df = pd.DataFrame(data)

print("DataFrame original:")
print(df)

print("\n")

print("Valores nulos:")
print(df.isnull())
