import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("./files/persona_definition_survey.csv")\
    .rename(columns=lambda x: x.strip())

print(list(df))

colstart = input("Copy first column without quotation: ")
colend = input("Copy last column without quotation: ")

cols = list(df.loc[:, colstart:colend])

df_filtered = df[cols].dropna()

colrank = ['Rank the following game aspects in order of importance.  [Graphics]',
           'Rank the following game aspects in order of importance.  [GamePlay]',
           'Rank the following game aspects in order of importance.  [User Interface]',
           'Rank the following game aspects in order of importance.  [Collection]',
           'Rank the following game aspects in order of importance.  [Competition]',
           'Rank each type of event in order of preference [Limited Time Battle Events '
           + '(Rarity Rumble/Battle for Survival/Mighty Money/]',
           'Rank each type of event in order of preference [Preservation/Stampede Events]',
           'Rank each type of event in order of preference [PvP Arenas]',
           'Rank each type of event in order of preference [Tournaments]',
           'Rank each type of event in order of preference [Community Events]']

for col in df_filtered.columns:
    if col in colrank:
        df_filtered[col] = [s[-1:] for s in df_filtered[col]]

for col in df_filtered.columns:
    if col in colrank:
        df_filtered[col] = df_filtered[col].apply(pd.to_numeric)

print(list(df_filtered))

grouping = input("Enter the column to aggregate with: ")
plot_average = ""
plot_median = []

for col in df_filtered.columns:
    if col in colrank:
        average = df_filtered.groupby(grouping).agg({col: np.average})
        median = df_filtered.groupby(grouping).agg({col: np.median})
        plot_average.append(average)
        #plot_median.append(median)

pay_average = df_filtered.groupby('What is your age?')\
    .agg({'Rank the following game aspects in order of importance.  [Graphics]': np.average,
          'Rank the following game aspects in order of importance.  [GamePlay]': np.average,
          'Rank the following game aspects in order of importance.  [User Interface]': np.average,
          'Rank the following game aspects in order of importance.  [Collection]': np.average,
          'Rank the following game aspects in order of importance.  [Competition]': np.average})
print(pay_average)

#plot_average.plot()
print(plot_average)
#plot_median.plot()
#plt.show()
