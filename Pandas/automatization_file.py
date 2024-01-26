import pandas as pd
import numpy as np

# Create list number phone random (TXT/CSV)
numbers = np.random.randint(100000000, 999999999, size=100)
numbers.tofile('numbers_phone.txt', sep='\n')
numbers.tofile('numbers_phone.csv', sep='\n')

df_number_phone = pd.DataFrame(numbers, columns=['number_phone'])
print(df_number_phone)
df_number_phone.to_csv('number_phone-updated.csv', index=False, header=False)
