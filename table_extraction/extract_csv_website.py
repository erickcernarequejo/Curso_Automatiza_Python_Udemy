import pandas as pd

# df_premier = pd.read_csv('https://www.football-data.co.uk/mmz4281/2324/E0.csv')
# df_premier.rename(columns={
#     'Date': 'date',
#     'HomeTeam': 'home_team',
#     'AwayTeam': 'away_team',
#     'FTHG': 'home_goals',
#     'FTAG': 'away_goals'
# }, inplace=True)
# print(df_premier)

# Read multiples leagues
# root = "https://www.football-data.co.uk/mmz4281/"
# leagues = ['E0', 'E1', 'E2', 'E3', 'EC']
# frames = []
#
# for league in leagues:
#     df = pd.read_csv(root + '2324/' + league + '.csv', encoding='unicode_escape')
#     frames.append(df)
#
# print(len(frames))

# Read multiples season
root = "https://www.football-data.co.uk/mmz4281/"
leagues = ['E0', 'E1', 'E2', 'E3', 'EC']
frames = []

for league in leagues:
    for season in range(15, 23):
        df = pd.read_csv(root + str(season) + str(season + 1) + '/' + league + '.csv', encoding='unicode_escape')
        df.insert(1, 'season', season)
        frames.append(df)

print(frames)