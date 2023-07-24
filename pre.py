#!/usr/bin/python3
print("Content-type: text/html")
print()
import joblib
import cgi
form=cgi.FieldStorage()
hr=form.getvalue("hr")
pre=joblib.load("my_mark_model.model")

value=int(hr)
print(pre.predict([[value]]))
