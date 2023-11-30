from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

forms_list = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    category = request.form.get('category')

    new_form = {'name': name, 'email': email, 'category': category}
    forms_list.append(new_form)

    return redirect(url_for('forms'))


@app.route('/forms')
def forms():
    return render_template('forms.html', forms=forms_list)


if __name__ == '__main__':
    app.run(debug=True)
