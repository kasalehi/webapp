from flask import Flask, render_template, request, redirect, url_for,request
import csv

app=Flask(__name__)

@app.route('/<string:page_name>')
def home(page_name):
    return render_template(page_name)

@app.route('/')
def home2():
    return render_template('./index.html')

    
def write_to_database(data):
    with open("database.csv", mode="a",newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file =csv.writer(database2,delimiter=',',quotechar='"')
        file.writerow([email,subject,message])


@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data= request.form.to_dict()
        write_to_database(data)
        return redirect(url_for('home',page_name='thankyou.html'))
    else:
        return 'you have made a get request'

        

if __name__=='__main__':
    app.run(debug=True)