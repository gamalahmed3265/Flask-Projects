from flask import Flask


app=Flask(__name__)

@app.route("/")
def welcome():
    return "hello world"

@app.route("/members")
def members():
    return "members"

if __name__ =="__main__":
    app.run()