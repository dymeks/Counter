from flask import Flask, render_template, request, redirect,session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def landing_page():
	if "counter" in session:
		session['counter'] +=1
	else:
		session['counter'] = 1		
	return render_template('index.html')

@app.route('/plus_two')
def plus_two():
	session['counter'] +=1
	return redirect('/')	

@app.route('/reset')
def reset():
	session['counter'] = 0
	return redirect('/')
	
app.run(debug=True)