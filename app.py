from flask import Flask,render_template,request,make_response,url_for,redirect
from markupsafe import escape
app=Flask(__name__)


@app.route('/')
def index():
    visit_count=request.cookies.get('visit_count','0')
    visit_count = int(visit_count) + 1
    response = make_response(render_template("index.html"))
    response.set_cookie('visit_count', str(visit_count))
    return response
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
@app.route('/pagevisitcount')
def page():
    visit_count=request.cookies.get('visit_count','0')
    return f'Hello, Youhave visited this websites {escape(visit_count)} times.'

if __name__ == '__main__':
         app.run(debug=False)