from flask import Flask, render_template, request, redirect, url_for
from elasticsearch import Elasticsearch
import uuid

app = Flask(__name__)

# Elasticsearch connection
es = Elasticsearch('https://localhost:9200', basic_auth=('elastic', '<password>'), verify_certs=False)

# Ensure index exists
INDEX_NAME = "book_catalog"
if not es.indices.exists(index=INDEX_NAME):
    es.indices.create(index=INDEX_NAME, body={
        "mappings": {
            "properties": {
                "title": {"type": "text"},
                "author": {"type": "text"},
                "genre": {"type": "keyword"},
                "publication_year": {"type": "integer"},
                "description": {"type": "text"}
            }
        }
    })

@app.route('/')
def index():
    # Retrieve all books
    body = {
        "query": {"match_all": {}},
        "sort": [{"publication_year": {"order": "desc"}}]
    }
    results = es.search(index=INDEX_NAME, body=body, size=100)
    books = [
        {**hit['_source'], 'id': hit['_id']} 
        for hit in results['hits']['hits']
    ]
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        book = {
            'title': request.form['title'],
            'author': request.form['author'],
            'genre': request.form['genre'],
            'publication_year': int(request.form['publication_year']),
            'description': request.form['description']
        }
        
        # Add book to Elasticsearch
        es.index(index=INDEX_NAME, body=book)
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/edit/<book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    if request.method == 'POST':
        # Update book in Elasticsearch
        updated_book = {
            'title': request.form['title'],
            'author': request.form['author'],
            'genre': request.form['genre'],
            'publication_year': int(request.form['publication_year']),
            'description': request.form['description']
        }
        es.update(index=INDEX_NAME, id=book_id, body={'doc': updated_book})
        return redirect(url_for('index'))
    
    # Retrieve specific book for editing
    book = es.get(index=INDEX_NAME, id=book_id)['_source']
    book['id'] = book_id
    return render_template('edit_book.html', book=book)

@app.route('/delete/<book_id>')
def delete_book(book_id):
    es.delete(index=INDEX_NAME, id=book_id)
    return redirect(url_for('index'))

@app.route('/search')
def search_books():
    query = request.args.get('query', '')
    body = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["title", "author","publication_year", "description", "genre"]
            }
        }
    }
    results = es.search(index=INDEX_NAME, body=body)
    books = [
        {**hit['_source'], 'id': hit['_id']} 
        for hit in results['hits']['hits']
    ]
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=False)