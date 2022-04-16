import pymysql

mydb = pymysql.connect(host='localhost',user='root',password='Dd13161613!')
my_cursor = mydb.cursor()
my_cursor.execute('CREATE DATABASE IF NOT EXISTS assignment')
# my_cursor.execute('CREATE DATABASE  assignment')
my_cursor.execute("CREATE TABLE IF NOT EXISTS assignment.user(id INTEGER AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255), password VARCHAR(255))")

import json

from flask import (Flask, render_template, redirect,
                   url_for, request, make_response,
                   flash)

app = Flask(__name__, static_url_path='')

@app.route('/',methods=['POST','GET'])
def index():
    if "signup" in request.form:
        print('--------sign up----------')
        query = 'SELECT * FROM assignment.user WHERE email=%s and password=%s'
        val = request.form['email']
        val2 = request.form['password']
        if my_cursor.execute(query,(val,val2))==0:
            # print(my_cursor.execute(query,query2))
            query4 = "INSERT INTO assignment.user (email, password) VALUES (%s, %s)"
            my_cursor.execute(query4, (val,val2))
            mydb.commit()
            print(my_cursor.execute(query,(val,val2)))
            return redirect(url_for('member'))
        # print(request.form['email'])
        else:
            # flash("Error")
            # redirect(url_for('index'))
            return render_template('add.html',errorMessage='ERROR!')
        print('-----------------')
        print(my_cursor.execute(query,(val,val2)))
        # return render_template('member.html')
    elif "signin" in request.form:
        print('-------signin--------')
        query = 'SELECT * FROM assignment.user WHERE email=%s and password=%s'
        val = request.form['email']
        val2 = request.form['password']
        print(my_cursor.execute(query,(val,val2)))
        if my_cursor.execute(query,(val,val2))==1:
            return redirect(url_for('member'))
        elif my_cursor.execute(query,(val,val2))==0:
            return render_template('add.html',errorMessage='ERROR!')
    else:
        return render_template('add.html')

@app.route('/member',methods=['POST','GET'])
def member():
    return render_template('member.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)