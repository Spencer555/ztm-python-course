from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


print(__name__)


@app.route("/<string:page_name>")
def about_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n {email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect('thankyou.html')
        
        except:
            return 'Did not save to database'
    return 'Something went wrong try again later'

    

# to run flask app
# flask --app main_filename run
# create linux virtual env
# mkvirtualenv - -python = /usr/bin/python3.6 my-virtualenv

# to switch to virtual env 
# workon my-virtualenv

# run in development mode so u dont have to restart server to view changes
# flask --app server run --debug
