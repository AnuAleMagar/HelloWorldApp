from flask import Flask,render_template,request,url_for,redirect
from markupsafe import escape
app=Flask(__name__)
count=0
def increment_count():
     global count
     count+=1

@app.route('/')
def index():
    increment_count()
    return  render_template("index.html")
@app.route('/about')
def about():
    increment_count()
    return render_template("about.html")
@app.route('/contact')
def contact():
    increment_count()
    return render_template("contact.html")
@app.route('/login')
def login():
    increment_count()
    username=request.args.get('username')
    if username:
         return redirect(url_for('loginsuccess',username=username))
    
    return render_template("login.html")
@app.route('/login/<username>')
def loginsuccess(username):
    return f'Hello {escape(username)}, Welcome to my app'
@app.route('/pagevisitcount')
def page():
    return f'Hello, Youhave visited this websites {escape(count)} times.'

if __name__ == '__main__':
         app.run(debug=False)