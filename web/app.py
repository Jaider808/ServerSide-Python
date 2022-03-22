from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person
from logic.Document import Document

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []
model2 = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/document', methods=['GET'])
def document():
    return render_template('document.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)


@app.route('/document_detail', methods=['POST'])
def document_detail():
    id_document = request.form['ISBN']
    title = request.form['title']
    numbers = request.form['number_of_pages']
    category = request.form['category']
    author = request.form['author']
    q = Document(id_document=id_document, title=title, number_page=numbers, category=category, author=author)
    model2.append( q)
    return render_template('document_detail.html', value=q)


@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in model]
    print(data)
    return render_template('people.html', value=data)


@app.route('/file')
def file():
    datad = [(i.id_document, i.title, i.number_of_pages, i.category,i.author) for i in model2]
    print(datad)
    return render_template('file.html', value=datad)


if __name__ == '__main__':
    app.run()