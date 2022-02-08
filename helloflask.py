from flask import Flask,redirect,url_for,request,render_template
import json


class wanmitFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(variable_start_string ="%%",variable_end_string="%%",))




app = wanmitFlask(__name__)




@app.route('/')
def hell0():
    return "hello flask"

@app.route("/index")
def index():
    return render_template('hello.html', name="haha3")

@app.route('/books/<int:num>')
def book_num(num):
    return "this is %s page"%(str(num))


@app.route('/name/<name>')
def check_name(name):
    if name == 'admin':
        return redirect(url_for('index'))
    else:
        return redirect(url_for('book_num',num=len(name)))


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        data = json.loads(request.data)
        print(data)
        print(type(data))
        # print(request.data)
        user =data['name']
        return "hello %s"%(user)
    else:
        user = request.args.get('name')
        return "hello %s"%(user)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9527, debug=True)