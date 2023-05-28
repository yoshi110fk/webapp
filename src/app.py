from getpatelem import getclaim1
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def predicts():
    if request.method == 'POST':
        number = request.form['patentnumber']
        if number == '':
            return redirect(request.url)
        claim_1st = getclaim1(number)
        return render_template('result.html', claim_1st = claim_1st, number = number)
    
    elif request.method == 'GET':
        return render_template('index.html')
        
if __name__ == '__main__':
    app.run(debug=True)

