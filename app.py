from flask import Flask,  render_template,request, url_for , jsonify


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate')
def calculate():
    input1 = float(request.args.get('input1'))
    input2 = float(request.args.get('input2'))
    operation = request.args.get('operation')

    if operation == 'add':
        result = input1 + input2
    elif operation == 'multiply':
        result = input1 * input2
    elif operation == 'subtract':
        result = input1 - input2
    else:
        result = "Invalid operation"

    return jsonify({'result': result})

print(__name__)
if __name__=='__main__':
    app.run(debug=True)