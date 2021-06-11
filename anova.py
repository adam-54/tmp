#ANOVA

import pandas as pd #to read the data
import numpy as np #create vector
from scipy import stats #for anova
url = 'https://raw.githubusercontent.com/adam-54/tmp/main/inwest_gosp.csv'

inwest_gosp= pd.read_csv(url,sep=',',header=0)

print("\n",inwest_gosp.head(5)) #\n for next line in output

# Identify unique values
print("\n",sorted(inwest_gosp.WIEK.unique()))

#data = np.inwest_gosp

# Sort them into groups, according to column 1
group1 = inwest_gosp.INWEST[inwest_gosp.WIEK==1]
group2 = inwest_gosp.INWEST[inwest_gosp.WIEK==2]
group3 = inwest_gosp.INWEST[inwest_gosp.WIEK==3]
group4 = inwest_gosp.INWEST[inwest_gosp.WIEK==4]


F_statistic, pVal = stats.f_oneway(group1, group2, group3, group4)

print("\n",F_statistic,pVal)

import pandas as pd
from statsmodels.formula.api import ols 
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

#Anova table
inwest_gosp= pd.read_csv(url,sep=',',header=0) 
model = ols('INWEST ~ C(WIEK)', inwest_gosp).fit() 
anovaResults = anova_lm(model)
print("\n",anovaResults)

#Multiple comparison
p1_tukey_test = pairwise_tukeyhsd(inwest_gosp["INWEST"], inwest_gosp["WIEK"] )
print("\n", p1_tukey_test._results_table)

#Homogeneity of variance test
(W,p) = stats.levene(group1, group2, group3, group4)
print("\n", W, p)


#https://github.com/thomas-haslwanter/statsintro_python/blob/master/ISP/Code_Quantlets/08_TestsMeanValues/anovaOneway/ISP_anovaOneway.py
#import pandas as pd #to read the data
#import numpy as np
#from scipy import stats #for anova
#url = 'https://raw.githubusercontent.com/thomas-haslwanter/statsintro_python/master/ISP/Code_Quantlets/08_TestsMeanValues/anovaOneway/altman_910.txt'

#data = np.genfromtxt(url, delimiter=',')

#print(data)
# Sort them into groups, according to column 1
#group1 = data[data[:,1]==1,0]
#group2 = data[data[:,1]==2,0]
#group3 = data[data[:,1]==3,0]

#print(group1)