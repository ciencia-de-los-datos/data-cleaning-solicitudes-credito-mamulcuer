"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from datetime import datetime

def clean_data():
    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df.drop(df.columns[0], axis=1, inplace=True)
    df['monto_del_credito'] = df['monto_del_credito'].str.replace('[\$,]', '', regex=True)
    df["monto_del_credito"] = df["monto_del_credito"].astype(str).str.split(".", expand=True)[0]
    df['idea_negocio'] = df['idea_negocio'].str.replace('-', ' ')
    df['línea_credito'] = df['línea_credito'].str.replace('-', ' ')
    df['barrio'] = df['barrio'].str.replace('-', ' ')
    #df['barrio'] = df['barrio'].str.replace('¿', 'e')
    df['idea_negocio'] = df['idea_negocio'].str.replace('_', ' ')
    df['línea_credito'] = df['línea_credito'].str.replace('_', ' ')
    df['barrio'] = df['barrio'].str.replace('_', ' ')
    def format_date(date_str):
        try:
            date_obj = datetime.strptime(date_str, '%Y/%m/%d')  # Intentar con formato Y/m/d
        except ValueError:
            date_obj = datetime.strptime(date_str, '%d/%m/%Y')  # Si falla, intentar con formato d/m/Y
            date_obj = datetime.strptime(date_obj.strftime('%Y/%m/%d'), '%Y/%m/%d')  # Convertir a formato Y/m/d y luego a objeto datetime
        return date_obj
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(format_date)
    df = df.applymap(lambda x: x.lower() if type(x) == str else x)
    df = df.apply(lambda x: x.str.strip() if x.name != 'barrio' and x.dtype == 'O' else x)
    df = df.dropna()
    df = df.drop_duplicates()
    return df