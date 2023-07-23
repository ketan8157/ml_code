from sklearn.linear_model import LinearRegression
import pandas as pd
data=pd.read_csv("ml_lr_data.csv")
x=data[["hours"]]
y=data["marks"]
model=LinearRegression()
model.fit(x,y)
import joblib
joblib.dump(model,"my_mark_model")
