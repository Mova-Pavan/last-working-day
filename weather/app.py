import os
from flask import Flask,render_template,request

import requests

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def home():
   
   if request.method=="POST":
      name=request.form['city']
      print(name)
      r=requests.get('https://api.openweathermap.org/data/2.5/weather?q='+name+'&appid=c4a702105ce0f62d2cab5f9478819f04')

      json_object = r.json()

      temp = float(json_object['main']['temp'])
      # temp = round(temp ,2)
      humidity = float(json_object['main']['humidity'])
      pressure = float(json_object['main']['pressure'])
      temperature=str(round((temp-273.15),2))

      
      return render_template("home.html",temperature=temperature,humidity=humidity,pressure=pressure)
   else:
      return render_template("home.html")

if __name__ == '__main__':
   app.run(debug=True,port=8000)