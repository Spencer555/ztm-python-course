from flask import Flask, render_template

app = Flask(__name__)


print(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"



@app.route("/blogs")
def my_blogs():
    return "<h1>The Greatest Collection To Exist</h1>"



@app.route("/blog/2020")
def my_blog2():
    return render_template('index.html')



@app.route("/about.html")
def about():
    return render_template('about.html')



@app.route("/<username>/<int:post_id>")
def by_username(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)


'''
mime -  Multipurpose Internet Mail Extensions
browsers use this to determine how to process the url not the file extension
stucture of mime type 
type/subtype
refer to doc
'''


# static file - is a file thats never going to change

# to run flask app
# flask --app main_filename run

# run in development mode so u dont have to restart server to view changes
# flask --app server run --debug
