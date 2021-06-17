import pandas as pd
import csv
import plotly.graph_objects as go
df = pd.read_csv('pixelMathData.csv')
studentDf = df.loc[df['student_id'] == 'TRL_mda']
print(studentDf.groupby('level')['attempt'].mean())
mean = studentDf.groupby('level')['attempt'].mean()
fig = go.Figure(go.Bar(x = mean,y = ['Level1','Level2','Level3','Level4'],orientation = 'h'))
fig.show()