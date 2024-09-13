import pandas as pd

datos = {
    'nombres': ['Juan', 'Ana', 'Luis'],
    'apellidos': ['Perez', 'Gonzalez', 'Lopez'],
    'edades': [30, 25, 40],
    'pesos': [70, 80, 50],
    'generos': ['M', 'F', 'M']
}

# Aca muestro el dataframe, una vez creado
df = pd.DataFrame(datos)
print(df)

print("\n")

# Filtrar por columnas, y mostrar los tipos de datos
columnaEdades =df['edades']
print(columnaEdades)

print("\n")

# Obtener el minimo en una columna, y el maximo
maximoYMinimo =str(df['edades'].min())+ '-' + str(df['edades'].max())

print(maximoYMinimo)

# Obtener en base a los datos, la media,la cantidad de datos,la desviacion estandar, el minimo, el maximo y algunos porcentajes
multiplesDatos = df.describe()

print("\n")

print(multiplesDatos)

# Informacion 'tecnica'

infoTec = df.info()

print(infoTec)