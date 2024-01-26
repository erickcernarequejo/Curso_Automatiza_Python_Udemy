import pandas as pd

# Read CSV
df_number_phone = pd.read_csv('numbers_phone.csv', names=['number_phone'])
print(df_number_phone)

df_number_phone['cod_country'] = df_number_phone['number_phone'].apply(lambda number: f'+1{number}')
print(df_number_phone)

# Read Multiple CSV
files_names = ['numbers_phone', 'number_phone-updated']

for file in files_names:
    df = pd.read_csv(f'{file}.csv', names=['number_phone'])
    df['cod_country'] = df['number_phone'].apply(lambda number: f'+1{number}')
    df.to_csv(f'code-{file}.csv', index=False)