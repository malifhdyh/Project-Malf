from flask import Flask, render_template

app = Flask(__name__)

# Aktifkan debug mode
app.debug = True
# atau
app.config['DEBUG'] = True

@app.route('/')
def home():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Port opsional, default 5000