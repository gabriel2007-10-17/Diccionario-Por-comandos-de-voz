from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Word = db.Column(db.String(100), nullable=False)
    definition = db.Column(db.String(200), nullable=False)
    language = db.Column(db.String(10), nullable=False)  # Corregido: db.column a db.Column

    def __repr__(self):  # Corregido: ___repr___ a __repr__
        return f"Word('{self.Word}')"

@app.route('/')
def index():
    search_term = request.args.get('search', '')
    language = request.args.get('language', 'es')

    words = Word.query.filter(Word.language == language, Word.Word.contains(search_term)).all()  # Corregido: Word.word a Word.Word

    return render_template('index.html', words=words, search_term=search_term, language=language)

@app.route('/add', methods=['POST'])
def add_word():
    word = request.form['word']
    definition = request.form['definition']
    language = request.form['language']

    new_word = Word(Word=word, definition=definition, language=language)  # Corregido: word a Word
    db.session.add(new_word)
    db.session.commit()

    return redirect(url_for('index', language=language))

@app.route('/delete/<int:id>')
def delete_word(id):
    word_to_delete = Word.query.get_or_404(id)
    db.session.delete(word_to_delete)
    db.session.commit()
    return redirect(url_for('index', language=word_to_delete.language))

if __name__ == '__main__':
    db.create_all()  # Crea la base de datos y las tablas
    app.run(debug=True)