import pandas as pd

# Concat multiples files
df_phone_number = pd.read_csv('numbers_phone.csv', names=['phone_number'])
df_phone_number2 = pd.read_csv('number_phone-updated.csv', names=['phone_number'])

df_concat = pd.concat([df_phone_number, df_phone_number2], axis=0, ignore_index=True)
print(df_concat)
df_concat.to_csv('number-concat.csv', index=False, header=False)