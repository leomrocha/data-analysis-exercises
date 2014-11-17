# -*- coding: utf-8 -*-
"""
Ranker module that obtains the rankins of arrivals
"""
#pandas
#import numpy as np
import pandas as pd

#geographic data
#from GeoBases import GeoBase
#geo_o = GeoBase(data='ori_por', verbose=False)

################################################################################
# Helpers
################################################################################

def strip_field(data):
    """
    strip white characters from input data if is string
    """
    if type(data) == str:
        return data.strip()
    return data

def to_date(data):
    """
    converts input data in yyyy-mm-dd format to Pandas Timestamp object.
    If it fails returns original object
    """
    try:
        return pd.Timestamp(data)
    except:
        return data
        

################################################################################
# Processing
################################################################################


class Ranker(object):
    """
    Creates ranking positions for Arrivals
    """
    def __init__(self):
        self.ranking = None
    
    def setup_arrivals_ranking(self, year=2013):
        """
        Sets up and calls the processing for ranking according to the arrivals in
        
        """
        fname = 'bookings.csv'
        col_names = ['arr_port', 'pax', 'off_time']
        cols = self.get_cols(fname, col_names)
        off_time = [i for i in cols if 'off_time' in i][0]
        arr_port = [i for i in cols if 'arr_port' in i][0]
        self.bks,self.col_names = self.load(fname, cols, 
                                    data_converters={arr_port:strip_field, off_time: to_date})
        self.ranking = self.rank(self.bks, year, 'arr_port', 'pax')
        
    def rank(self, df, year, group_col, sum_col):
        """
        Process the input DataFrame grouping by group_col and indexing by sum_col
        """
        arrs = df[df.off_time.apply(lambda x: x.date().year == year if (type(x) == pd.tslib.Timestamp ) else False)].groupby(group_col).sum()
        arrs.sort(sum_col, ascending=False, inplace=True)
        return arrs
        
    def get_cols(self, fname, col_names):
        """
        get column names
        """
        #load first line of the bookings file to get names that will be parsed ...
        cols = []
        headers = []
        with open(fname) as f:
            head = f.readline()
            #split as the separator will do
            headers = head.split('^')
            for h in headers:
                for c in col_names:
                    if c in h:
                        cols.append(h)
        return cols
        
    def load(self, fname, cols, data_converters={}, separator='^'):
        """
        Loads the file from which to get rankings
        """
        #get cols
        #
        
        df = pd.read_table(fname,sep=separator, 
                    usecols=cols, 
                    converters=data_converters)
        #now strip whitespaces from column name 
        df.rename(columns=lambda x: x.strip(), inplace=True)
        cols[:] = [c.strip() for c in cols]
        return df, cols
        
    def get_last(self, n):
        """
        Returns the last 'n' airports in arrivals ranking in JSON format
        """
        return self.ranking.tail(n).to_json()

    def get_first(self, n):
        """
        Returns the first 'n' airports in arrivals ranking in JSON format
        """
        return self.ranking.head(n).to_json()

