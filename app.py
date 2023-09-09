from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/aboutus')
def aboutus():
    return "this is our program"

@app.route('/demo',methods = ['POST'])
def math_operation():
    if(request.method=='POST'):
        operation = request.json['operation']
        num1 = request.json['num1']
        num2 = request.json['num2']

        if operation == "add":
            result = num1+num2
        elif operation == "multiply":
            result = num1*num2
        elif operation == "division":
            result = num1/num2
        else:
            result = num1-num2

        return "the operation is {} and the result is {}".format(operation,result)



if __name__ == "__main__":
    app.run(host = "0.0.0.0",port = 5000)
