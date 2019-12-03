import pandas as pd

def horse_data():
    df = pd.read_csv('clean.csv')

    df_3_USA = df[df['origin'] == 'usa'][['name','horsepower']].sort_values(by='horsepower', ascending=False).head(3)
    df_3_JPN =df[df['origin'] == 'japan'][['name','horsepower']].sort_values(by='horsepower', ascending=False).head(3)
    df_3_EUR =df[df['origin'] == 'europe'][['name','horsepower']].sort_values(by='horsepower', ascending=False).head(3)

    rank_dataframe = pd.DataFrame({
        'Ranking' : ['Rank 1' , 'Rank 2' , 'Rank 3'],
        'Usa' : df_3_USA.name.values,
        'Japan' : df_3_JPN.name.values,
        'Europe' : df_3_EUR.name.values,
    } , index = ['Rank 1' , 'Rank 2' , 'Rank 3'])
    return rank_dataframe

def  irit_data():
    df = pd.read_csv('clean.csv')

    irit_USA = df[df['origin'] == 'usa' ][['name','mpg']].sort_values(by='mpg',ascending=False).head(3)
    irit_JPN = df[df['origin'] == 'japan' ][['name','mpg']].sort_values(by='mpg',ascending=False).head(3)
    irit_EUR = df[df['origin'] == 'europe' ][['name','mpg']].sort_values(by='mpg',ascending=False).head(3)

    rank_dataframe = pd.DataFrame({
        'Ranking' : ['Rank 1' , 'Rank 2' , 'Rank 3'],
        'Usa' : irit_USA.name.values,
        'Japan' : irit_JPN.name.values,
        'Europe' : irit_EUR.name.values,
    } , index = ['Rank 1' , 'Rank 2' , 'Rank 3'])
    return rank_dataframe