from flask import Flask, render_template

app = Flask(__name__)


print(__name__)



@app.route("/<string:page_name>")
def about_page(page_name):
    return render_template(f'{page_name}.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    return'form submitted hoorayy'
# to run flask app
# flask --app main_filename run

# run in development mode so u dont have to restart server to view changes
# flask --app server run --debug


# Building A Portfolio 4

# 2.14