import pandas as pd

# Delete duplicates and values NaN
df_concat = pd.read_csv('number-concat.csv', names=['number-phone'])

# Duplicate number elements
# print(df_concat[df_concat['number-phone'].duplicated()])

# Delete duplicate
# Option 1
# df_concat = df_concat.drop_duplicates(['number-phone'])
# df_concat.to_csv('no_duplicate.csv', index=False)

# Option 2
df_concat.drop_duplicates(['number-phone'], inplace=True)
print(df_concat)

# Delete values NaN
print(df_concat[df_concat['number-phone'].isnull()])
df_concat.dropna(subset=['number-phone'], inplace=True)
print(df_concat)

# Complete values Nan
df_concat['number-phone'] = df_concat['number-phone'].fillna('-1')