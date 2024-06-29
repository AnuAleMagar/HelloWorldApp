from flask import Flask,render_template,request,url_for,redirect
from markupsafe import escape
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/contact')
def contact():
    return render_template("contact.html")
@app.route('/login')
def login():
    username=request.args.get('username')
    if username:
         return redirect(url_for('loginsuccess',username=username))
    
    return render_template("login.html")
@app.route('/login/<username>')
def loginsuccess(username):
    return f'Hello {escape(username)}, Welcome to my app'

if __name__ == '__main__':
         app.run(debug=False)