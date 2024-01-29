import pandas as pd

root = "https://www.football-data.co.uk/mmz4281/"
leagues = ['E0', 'E1', 'E2', 'E3', 'EC']

dict_countries = {
    'Spanish La Liga': 'SP1',
    'English Premier League': 'E0'
}

dic_historical_data = {}

for league in dict_countries:
    frames = []
    for season in range(15, 23):
        df = pd.read_csv(root + str(season) + str(season + 1) + '/' + dict_countries[league] + '.csv', encoding='unicode_escape')
        df.insert(1, 'season', season)
        frames.append(df)
    df_concat = pd.concat(frames)
    dic_historical_data[league] = df_concat
print(dic_historical_data.keys())
print(dic_historical_data)