from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template('home.html')


@app.route('/orders')
def order():
    return render_template('orders.html', number_of_orders=3, orders=['121234', '345643563', '346345634r56'])


@app.route('/orders/<orderid>')
def order_by_id(orderid):
    return render_template('order_details.html', order_id=orderid)


@app.route('/<name>')
def user(name):
    return '<h1>Name is:' + name + '</h1>'


@app.route('/admin')
def admin():
    # return redirect(url_for('hello_world'))
    return redirect(url_for('user', name='Admin2'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['pwd']

        if password != 'abc123':
            return redirect(url_for('login'))

        return render_template('profile.html', user=username)
    else:
        return render_template('login.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


if __name__ == '__main__':
    app.run(debug=True)
