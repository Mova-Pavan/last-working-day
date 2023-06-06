from pipes import Template
import pandas as pd
from flask import Flask,render_template,redirect,request



app=Flask(__name__,template_folder='Templates')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/',methods = ['POST', 'GET'])
def handle_get():   
    if request.method == 'POST':
        year = request.form['year']
        print(year)
    
        s = pd.date_range(year , periods=12, freq='BM')
        # df = pd.DataFrame(s, columns=['Date'])
        # x=s.tolist()
        x=pd.Series(s)
    return render_template('result.html',wd=x.dt.date) 

    
if __name__=="__main__":
    app.run(debug=True)


