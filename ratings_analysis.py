import csv
import pandas as pd

ratings = pd.read_csv('ratings_60.txt', delimiter=' ', names = ['id', 'HAP', 'SAD', 'SUR', 'ANG', 'DIS', 'PIC', 'sample'])
print(ratings.head())