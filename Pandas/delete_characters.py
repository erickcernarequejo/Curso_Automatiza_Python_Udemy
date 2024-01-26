import pandas as pd

# Read file CSV 'code_number_phone'

df_numbers_phone = pd.read_csv('code-numbers_phone.csv', dtype={'number_phone': int, 'cod_country': str})
print(df_numbers_phone)

# Delete character
df_numbers_phone['number_phone_without_add'] = df_numbers_phone['cod_country'].str.extract(r'\+(\d+)')
print(df_numbers_phone)

# Export file
df_numbers_phone.to_csv('number_phone_without_add.csv', index=False)