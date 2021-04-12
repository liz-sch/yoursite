from flask import Flask
from flask import render_template
from flask import url_for, redirect, request
from flask_bootstrap import Bootstrap

import sqlite3 as sql

app	= Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template('home.htm')

@app.route('/myform.htm')
def new_contact():
    return render_template('myform.htm')


def create_database():
    conn = sql.connect('database.db')
    conn.execute('CREATE TABLE Contacts(name TEXT, phone TEXT, email TEXT')
    conn.close()

@app.route('/addrec', methods = ['POST', 'GET'])
def addrec():
    if request.method	==	'POST':
        try:
            nm = request.form['nm']
            tl = request.form['tl']
            em = request.form['em']
								
            with sql.connect("database.db")	as con:
                cur	= con.cursor()
        
                cur.execute("INSERT	INTO Contacts(name, tel, em) VALUES	[?,?,?]", (nm,tel,em))
												
                con.commit()

						
        finally:
            return render_template("result.htm")
	
    con.close()

@app.route('/list.htm')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
		
    cur = con.cursor()
    cur.execute("select * from Contacts")
		
    rows = cur.fetchall()
    return render_template("list.htm", rows = rows)

if __name__	==	'__main__':
    app.run(debug	=	True)