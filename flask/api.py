from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/init')
def my_form_post():

    import data_reader
    dataset = data_reader.reader()

    return render_template('init.html', value2=dataset)

@app.route('/result', methods=['POST'])
def result():
    print("Hello, World!")
    projectpath = request.form['projectFilepath']

    print("HGJHGDJHGDJSHGJDHGSd")
    print(projectpath)
    print("HGJHGDJHGDJSHGJDHGSd")

    import keras_first_network
    animal = keras_first_network.ml_script(projectpath)
    return render_template('result.html', value=animal)

@app.route('/result/csv', methods=['POST'])
def my_form_post_3():
    table = pd.DataFrame.from_csv("result.csv")
    return render_template("csv.html", data=table.to_html())
    

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

