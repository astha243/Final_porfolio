from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
@app.route('/')
def my_home():
    return render_template('index.html')

# to render the html template as requested by the user.
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
  with open('database.csv', newline= '' , mode='a') as database:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email,subject,message])

#new route with post method so that the users can post datas      
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        #to get the data as dict 
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'some thing went wrong'

