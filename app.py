from flask import Flask, render_template, request, jsonify,flash
import sqlite3
import numpy as np

app = Flask(__name__)


@app.route('/main')
def main():
    return render_template("home.html")
@app.route('/team')
def teams():
    return render_template("team.html")

@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/contact')
def contact():
    return render_template("contact.html")
##

@app.route('/parent2/lenning')
def lenning_p2():
    return render_template('parent2/lenning.html')
@app.route('/parent2/fullbend')
def fullbend_p2():
    return render_template('parent2/fullbend.html')
@app.route('/parent2/bend40')
def bend40_p2():
    return render_template('parent2/bend40.html')
@app.route('/parent2/bend70')
def bend70_p2():
    return render_template('parent2/bend70.html')
@app.route('/parent2/sq')
def sq_p2():
    return render_template('parent2/sq.html')


##
@app.route('/parent2/bm/lenning')
def lenning_bmp2():
    return render_template('parent2/bm/lenning.html')
@app.route('/parent2/bm/fullbend')
def fullbend_bmp2():
    return render_template('parent2/bm/fullbend.html')
@app.route('/parent2/bm/bend40')
def bend40_bmp2():
    return render_template('parent2/bm/bend40.html')
@app.route('/parent2/bm/bend70')
def bend70_bmp2():
    return render_template('parent2/bm/bend70.html')
@app.route('/parent2/bm/sq')
def sq_bmp2():
    return render_template('parent2/bm/sq.html')

## 
@app.route('/parent2/cv&bm/lenning')
def lenning_cvbmp2():
    return render_template('parent2/cv&bm/lenning.html')
@app.route('/parent2/cv&bm/fullbend')
def fullbend_cvbmp2():
    return render_template('parent2/cv&bm/fullbend.html')
@app.route('/parent2/cv&bm/bend40')
def bend40_cvbmp2():
    return render_template('parent2/cv&bm/bend40.html')
@app.route('/parent2/cv&bm/bend70')
def bend70_cvbmp2():
    return render_template('parent2/cv&bm/bend70.html')
@app.route('/parent2/cv&bm/sq')
def sq_cvbmp2():
    return render_template('parent2/cv&bm/sq.html')

## Parent page 1 
@app.route('/main95th')
def main95():
    return render_template('main95th.html')


##
@app.route('/parent1/lenning')
def lenning():
    return render_template('parent1/lenning.html')
@app.route('/parent1/fullbend')
def fullbend_p1():
    return render_template('parent1/fullbend.html')
@app.route('/parent1/bend40')
def bend40_p1():
    return render_template('parent1/bend40.html')
@app.route('/parent1/bend70')
def bend70_p1():
    return render_template('parent1/bend70.html')
@app.route('/parent1/sq')
def sq_p1():
    return render_template('parent1/sq.html')


##
@app.route('/parent1/bm/lenning')
def lenning_bmp1():
    return render_template('parent1/bm/lenning.html')
@app.route('/parent1/bm/fullbend')
def fullbend_bmp1():
    return render_template('parent1/bm/fullbend.html')
@app.route('/parent1/bm/bend40')
def bend40_bmp1():
    return render_template('parent1/bm/bend40.html')
@app.route('/parent1/bm/bend70')
def bend70_bmp1():
    return render_template('parent1/bm/bend70.html')
@app.route('/parent1/bm/sq')
def sq_bmp1():
    return render_template('parent1/bm/sq.html')

## 
@app.route('/parent1/cv&bm/lenning')
def lenning_cvbmp1():
    return render_template('parent1/cv&bm/lenning.html')
@app.route('/parent1/cv&bm/fullbend')
def fullbend_cvbmp1():
    return render_template('parent1/cv&bm/fullbend.html')
@app.route('/parent1/cv&bm/bend40')
def bend40_cvbmp1():
    return render_template('parent1/cv&bm/bend40.html')
@app.route('/parent1/cv&bm/bend70')
def bend70_cvbmp1():
    return render_template('parent1/cv&bm/bend70.html')
@app.route('/parent1/cv&bm/sq')
def sq_cvbmp1():
    return render_template('parent1/cv&bm/sq.html')


if __name__ == '__main__':
    app.run(host='10.0.0.57', port=8900, debug=True)