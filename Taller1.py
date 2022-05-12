# Prueba de uso de el diagrama de piper

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


from wqchartpy import triangle_piper
from wqchartpy import durvo
from wqchartpy import stiff
from wqchartpy import schoeller
from wqchartpy import gibbs
from wqchartpy import chadha
from wqchartpy import gaillardet
from wqchartpy import hfed

df = pd.read_csv(r'data_template.csv', index_col=None, header=0)
dfmeq = pd.read_csv(r'data_templatemeq.csv', index_col=None, header=0)
dfstiff = pd.read_csv(r'data_template_stiff.csv', index_col=None, header=0)

dfstiff1 = dfstiff.loc[dfstiff['Sample'] == 'Grupo 1']
dfstiff2 = dfstiff.loc[dfstiff['Sample'] == 'Grupo 2']
dfstiff3 = dfstiff.loc[dfstiff['Sample'] == 'Grupo 3']


triangle_piper.plot(df, 
                    unit='mg/L', 
                    figname='triangle Piper diagram', 
                    figformat='png')

durvo.plot(df,unit='mg/L',
           figname='Durvo diagram',
           figformat='png')

schoeller.plot(dfmeq,unit='meq/L',
           figname='Schoeller diagram',
           figformat='png')

gibbs.plot(df,unit='mg/L',
           figname='Gibbs diagram',
           figformat='png')

chadha.plot(dfmeq,unit='mg/L',
           figname='Chadha diagram',
           figformat='png')

gaillardet.plot(df,unit='mg/L',
           figname='Gaillardet diagram',
           figformat='png')

hfed.plot(df,unit='mg/L',
          figname='HFED diagram',
          figformat='png')