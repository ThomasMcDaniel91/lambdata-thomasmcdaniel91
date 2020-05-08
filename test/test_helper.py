import unittest
import pandas as pd
from my_lambdata.helper import Additions
#df = pd.read_csv('https://raw.githubusercontent.com/mtoce/Build2-Project/master/astros_bangs_20200127.csv')
#names = list(df['game_date'])


class Test_Additions(unittest.TestCase):

    def test_exten_df(self):
        df = pd.read_csv('https://raw.githubusercontent.com/mtoce/Build2-Project/master/astros_bangs_20200127.csv')
        names = list(df['game_date'])
        X = Additions(df, names, 'last').exten_df()
        self.assertEqual(len(X['last']), len(names))

if __name__ == "__main__":    
    unittest.main()