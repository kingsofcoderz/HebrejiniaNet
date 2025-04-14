from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Make sure users.txt exists
if not os.path.exists('users.txt'):
    open('users.txt', 'w').close()

@app.route('/')
def home():
    return 'Welcome to Hebrejinianet Chat!'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with open('users.txt', 'a') as f:
            f.write(f"{username}:{password}\n")

        return 'Signup successful! Now you can login.'

    return '''
    <form method="post">
      Username: <input type="text" name="username"><br>
      Password: <input type="password" name="password"><br>
      <input type="submit" value="Sign Up">
    </form>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with open('users.txt', 'r') as f:
            users = f.readlines()

        for user in users:
            saved_username, saved_password = user.strip().split(':')
            if username == saved_username and password == saved_password:
                return f'Login successful! Welcome, {username}'

        return 'Invalid username or password'

    return '''
    <form method="post">
      Username: <input type="text" name="username"><br>
      Password: <input type="password" name="password"><br>
      <input type="submit" value="Login">
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
