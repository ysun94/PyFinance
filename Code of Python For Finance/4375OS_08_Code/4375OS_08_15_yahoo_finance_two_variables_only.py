"""
  Name     : 4375OS_08_15_Yahoo_finance_two_variables_only.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
x=pd.read_csv('http://chart.yahoo.com/table.csv?s=IBM',usecols=[0,6],index_col=0)
print x.head()
