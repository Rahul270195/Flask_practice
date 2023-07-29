from flask import Flask,render_template,request,url_for,redirect

app =Flask(__name__)


@app.route('/')
def home():
    return "<p>Hello World</p>"

@app.route('/welcome')
def welcome():
    return "Welcome to the Flask tutorials"


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "the person is passed and the score is "+str(score)


@app.route('/fail/<int:score>')
def fail(score):
    return "the person is failed and the score is "+str(score)

@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template("calculate.html")
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        
        average_marks=(maths+science+history)/3
        #result="" 
        #if average_marks>=50:
            #result="success"
        #else:
            #result="fail"
            
        #return redirect(url_for(result,score=average_marks))


        return render_template('results.html',results=average_marks)


## Assignemnt Try for loop

        
        ##return render_template('results.html',results=average_marks)
        






if __name__ == '__main__':
    app.run(debug=True)
    