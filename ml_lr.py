from sklearn.linear_model import LinearRegression
import pandas as pd
data=pd.read_csv("SLR_ML_data - Sheet1.csv")
x=data[["hours"]]
y=data["marks"]
model=LinearRegression()
model.fit(x,y)
