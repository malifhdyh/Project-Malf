from flask import Flask, render_template, url_for
import os

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    # Debug info
    print("Static folder:", app.static_folder)
    print("Static files:", os.listdir(app.static_folder))
    print("CSS files:", os.listdir(os.path.join(app.static_folder, 'css')))
    print("JS files:", os.listdir(os.path.join(app.static_folder, 'js')))
    return render_template('base.html')

if __name__ == '__main__':
    app.run()