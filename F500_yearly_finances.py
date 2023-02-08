import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# find the dataset source here:
# https://www.kaggle.com/datasets/yashsrivastava51213/revenue-and-profit-of-fortune-500-companies?select=fortune500.csv
# pd.read_csv(r'C:\Users\ekopen\Documents\Kaggle\fortune500.csv').to_pickle('./fortune500.pkl')
# df = pd.read_pickle('fortune500.pkl')
#
# df = df[df['Rank'] <= 500]
# df['Revenue (in millions)'] = pd.to_numeric(df['Revenue (in millions)'].str.replace(',',''))
# df['Profit (in millions)'] = df['Profit (in millions)'].str.replace(',','')
# df['Profit Margin'] = 0
# average_pm = .08
# for x in range(len(df.index)):
#     if df.iloc[x,4] != 'N.A.':
#         df.iloc[x,5] = pd.to_numeric(df.iloc[x,4])/df.iloc[x,3]
#     else:
#         df.iloc[x,5] = average_pm
# df['Profit (in millions)'] = df['Revenue (in millions)'] * df['Profit Margin']
# df.to_pickle('./cleaneddf.pkl')

df = pd.read_pickle(r"C:\Users\ekopen\PycharmProjects\pythonProject\cleaneddf.pkl")
df_focus = df[(df['Year'] >= 2001) & (df['Year'] <= 2001)]
dfgrouped = df.groupby('Year').agg('sum').reset_index()
dfgrouped['Profit Margin'] = dfgrouped['Profit (in millions)'] / dfgrouped['Revenue (in millions)']

df_dict = {}
year_dict = {}

for x in dfgrouped['Year']:
    year_dict['DF'] = df[df['Year'] == x]
    year_dict['Average PM'] = np.average(year_dict['DF']['Profit Margin'], weights=year_dict['DF']['Revenue (in millions)'])
    year_dict['Std Dev PM'] = np.std(year_dict['DF']['Profit Margin'])
    year_dict['Upper Bound'] = (year_dict['Std Dev PM'] + year_dict['Std Dev PM'] * 3)
    year_dict['Lower Bound'] = (year_dict['Std Dev PM'] + year_dict['Std Dev PM'] * -3)
    df_dict[x] = year_dict
    year_dict = {}

for x in df_dict:
    print(df_dict)

# x2 = df['Year']
# y3 = df['Profit Margin']
# z = np.polyfit(x2, y3, 1)
# p = np.poly1d(z)
#
# plt.plot(x2, y3, label="Profit Margin")
# plt.plot(x2, p(x2), label="Profit Margin")
# plt.xlabel("Year")
# plt.ylabel("%")
# plt.title("F500 Profit Margin Over Time")
# plt.show()

