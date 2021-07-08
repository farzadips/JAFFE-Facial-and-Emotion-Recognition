import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm


ratings60 = pd.read_csv('ratings_60.txt', delimiter=' ', names = ['id', 'HAP', 'SAD', 'SUR', 'ANG', 'DIS', 'FEA', 'sample'])
print(ratings60.head())
hap = ratings60['HAP']
sad = ratings60['SAD']
sur = ratings60['SUR']
ang = ratings60['ANG']
dis = ratings60['DIS']
fea = ratings60['FEA']

print(np.mean(hap), np.mean(sad), np.mean(sur), np.mean(ang), np.mean(dis), np.mean(fea))
plt.figure(figsize=(10,10))
emotion = fea
sns.distplot(emotion, fit=norm)
plt.title("Emotion Distribution Plot", size=15, weight='bold')
plt.show()