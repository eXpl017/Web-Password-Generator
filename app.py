from flask import Flask, render_template, request
from generate import generate
from checks import lenCheck, symbCheck

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def passwordGenerator():

    render_file = 'pass_gen.html'

    if request.method == "POST":

        length = request.form.get("length")
        len_check = lenCheck(length)
        if not len_check[0]:
            err_msg = len_check[1]
            return render_template(render_file, len_err_msg=err_msg)

        include = ['lowr'] + request.form.getlist("include")

        exclude = '' if 'punc' not in include else request.form.get('exclude')
        symb_check = symbCheck(exclude)
        if not symb_check[0]:
            err_msg = symb_check[1]
            return render_template(render_file, sym_err_msg=err_msg)

        password = generate(include, exclude, int(length))
        return render_template(render_file, password=password)

    return render_template(render_file)

if __name__=="__main__":
    app.run()
