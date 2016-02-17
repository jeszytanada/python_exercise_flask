from flask import Flask, render_template, request, session
app = Flask(__name__)
#request.data
#url_for(endpoint , **kwargs)
@app.route('/base/')
def hello():
	#assert False
    return render_template('base.html')

@app.route('/<name>/<int:answer>',methods=['GET', 'POST'])
def guess(name, answer):
	#assert False
    if name == 'jeszy':
        session['logged_in'] = True
        fname = request.form['fname']
        lname = request.form['lname']   
        correct = (answer == 27)
    return render_template('guess2.html', name=name, correct=correct)

@app.route('/login/',methods=['GET', 'POST'])
def login():
	#assert False
    if session['logged_in'] == True:
        fname = request.form['fname']
        lname = request.form['lname']   
    return render_template('store.html', fname, lname)

@app.route('/store/',methods=['GET', 'POST'])
def store():

    return render_template('store.html')
    

app.secret_key = 'yeyow'

if __name__ == '__main__':
    app.run(debug=True)