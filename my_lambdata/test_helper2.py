import pandas as pd


class Additions:
    """
    Takes inputs of a dataframe, a list or series and a desired column name
    concatinates the given list to the dataframe and adds the given name
    as the new column's name.
    """
    def __init__(self, df, list_name, new_col_name):
        self.df = df
        self.list_name = list_name
        self.new_col_name = new_col_name

    def exten_df(self):
        X = self.df.copy()
        X[self.new_col_name] = pd.Series(self.list_name)
        return X

if __name__ == "__main__":
    df = pd.read_csv('https://raw.githubusercontent.com/mtoce/Build2-Project/master/astros_bangs_20200127.csv')
    names = list(df['game_date'])
    new_df = Additions(df, names, 'last')
    new_df = new_df.exten_df()
    print(new_df['last'])