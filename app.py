from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def password_generator():
    if request.method == "POST":
        getValue = request.form.get
        length = getValue("length")
        uppr, dig, punc = getValue("uppr"), getValue("dig"), getValue("punc")
        exclude = getValue("exclude")
        return f"length {length} uppr, dig, punc {uppr},{dig}, {punc} exclude {exclude}"
    return render_template('pass_gen.html')

if __name__=="__main__":
    app.run(debug=True)
