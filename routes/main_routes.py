from flask import render_template, current_app as app

@app.route('/')
@app.route('/main')
def main():
    return render_template('index.html')
