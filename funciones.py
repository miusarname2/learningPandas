import pandas as pd
import xlrd

# Leer excel
ruta="C:\\Users\\Oscar Alvarez\\Downloads\\sandbox\\dataLake\\"
contenidoExcel = pd.read_excel(ruta+'titanic.xlsx')
print(contenidoExcel)
