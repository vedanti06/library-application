# Book Catalog Application

This is a Flask-based web application that uses Elasticsearch to manage a book catalog. It provides CRUD (Create, Read, Update, Delete) operations for books.

## Features

- List all books
- Add new books
- Edit existing books
- Delete books
- Search for books by title, author, genre, publication year, or description

## Prerequisites

- Python 3.7+
- Elasticsearch 8.x
- Flask 2.1.0
- Elasticsearch Python client 8.4.3

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
    
## To run the application:

1. Ensure Elasticsearch is running on your local machine at `https://localhost:9200`. You may need to adjust the connection settings in `main.py`.

2. Install the required dependencies using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python main.py
   ```

4. Open a web browser and navigate to `http://localhost:5000` to access the Book Catalog application.

Make sure to replace the placeholder Elasticsearch authentication credentials in `main.py` with your actual credentials for secure access.

## Application screenshots

**Add book Page**:Demonstrates the Add Book form in the Book Catalog application. Users can input details such as:
Book Title, Author, Genre, Publication Year, Description
![Add Book](/screenshots/screenshot_add book.PNG)
**Book listing Page**:The screenshot shows the main book listing page, which displays:
All books in the catalog
Sorted by publication year in descending order
Key book information at a glance
![Books](screenshot_books added.PNG)
**Search Page**: Demonstrates the book search functionality in the Book Catalog application.
![Search Results](/screenshots/search_screenshot.PNG)
