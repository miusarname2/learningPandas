import pandas as pd

datos = {
    'nombres': ['Juan', 'Ana', 'Luis'],
    'apellidos': ['Perez', 'Gonzalez', 'Lopez'],
    'edades': [30, 25, 40],
    'pesos': [70, 80, 50],
    'generos': ['M', 'F', 'M']
}

# Aca muestro el dataframe, una vez creado
df = pd.DataFrame(data=datos)
print(df)

print("\n")

# Filtrar por columnas, y mostrar los tipos de datos
print(df['edades'])
