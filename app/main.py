from flask import Flask, request

app = Flask(__name__)

SECRET_KEY = 'supersecretkey'  # Hardcoded secret

@app.route('/')
def index():
	name = request.args.get('name')  # No input validation
	return f'Hello, {name}!'

@app.route('/secret')
def secret():
	return SECRET_KEY  # Exposes secret

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
