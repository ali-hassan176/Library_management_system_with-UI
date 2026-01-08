from flask import Flask, render_template, request, jsonify, redirect, url_for
from library_system import LibrarySystem
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Initialize library system
lib = LibrarySystem()

# Load initial data
try:
    lib.load_books_from_csv("books.csv")
    lib.load_members_from_csv("members.csv")
    print("✓ Books and members loaded successfully")
except Exception as e:
    print(f"Error loading data: {e}")

# ==================== ROUTES ====================

@app.route('/')
def index():
    return redirect(url_for('books'))

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/members')
def members():
    return render_template('members.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

# ==================== API ENDPOINTS ====================

@app.route('/api/books/all', methods=['GET'])
def api_get_all_books():
    books_list = lib.list_all_books()
    books_data = []
    
    for isbn, data in books_list:
        books_data.append({
            'isbn': isbn,
            'title': data['title'],
            'author': data['author'],
            'year': data['year'],
            'category': data['category'],
            'available_copies': data['available_copies']
        })
    
    return jsonify(books_data)

@app.route('/api/books/search', methods=['POST'])
def api_search_books():
    data = request.json
    search_type = data.get('type')
    query = data.get('query', '').strip()
    
    results = []
    
    try:
        if search_type == 'isbn':
            node = lib.books.search(query)
            if node:
                results = [{
                    'isbn': query,
                    'title': node.value['title'],
                    'author': node.value['author'],
                    'year': node.value['year'],
                    'category': node.value['category'],
                    'available_copies': node.value['available_copies']
                }]
        
        elif search_type == 'title':
            isbn = lib.title_index.get_isbn(query)
            if isbn:
                node = lib.books.search(isbn)
                if node:
                    results = [{
                        'isbn': isbn,
                        'title': node.value['title'],
                        'author': node.value['author'],
                        'year': node.value['year'],
                        'category': node.value['category'],
                        'available_copies': node.value['available_copies']
                    }]
        
        elif search_type == 'author':
            books = lib.search_by_author(query)
            for book in books:
                all_books = lib.list_all_books()
                for isbn, data in all_books:
                    if (data['title'] == book['title'] and 
                        data['author'] == book['author']):
                        results.append({
                            'isbn': isbn,
                            'title': data['title'],
                            'author': data['author'],
                            'year': data['year'],
                            'category': data['category'],
                            'available_copies': data['available_copies']
                        })
                        break
    except Exception as e:
        print(f"Search error: {e}")
        return jsonify([])
    
    return jsonify(results)

@app.route('/api/books/borrow', methods=['POST'])
def api_borrow_book():
    data = request.json
    member_id = data.get('member_id')
    isbn = data.get('isbn')
    
    if not member_id:
        return jsonify({'success': False, 'message': 'Member ID required'}), 400
    
    success = lib.borrow_book(member_id, isbn)
    
    if success:
        lib.save_books()
        lib.save_members()
        return jsonify({'success': True, 'message': 'Book borrowed successfully'})
    else:
        member = lib.members.get_member(member_id)
        if not member:
            return jsonify({'success': False, 'message': 'Member not found'})
        if not member.can_borrow():
            return jsonify({'success': False, 'message': 'Borrow limit reached (max 5 books)'})
        return jsonify({'success': False, 'message': 'Book not available'})

@app.route('/api/books/return', methods=['POST'])
def api_return_book():
    data = request.json
    member_id = data.get('member_id')
    isbn = data.get('isbn')
    
    if not member_id:
        return jsonify({'success': False, 'message': 'Member ID required'}), 400
    
    success = lib.return_book(member_id, isbn)
    
    if success:
        lib.save_books()
        lib.save_members()
        return jsonify({'success': True, 'message': 'Book returned successfully'})
    else:
        return jsonify({'success': False, 'message': 'Return failed'})

@app.route('/api/books/add', methods=['POST'])
def api_add_book():
    data = request.json
    
    success = lib.add_book(
        data['isbn'],
        data['title'],
        data['author'],
        int(data['year']),
        data['category'],
        int(data['copies'])
    )
    
    if success:
        return jsonify({'success': True, 'message': 'Book added successfully'})
    else:
        return jsonify({'success': False, 'message': 'Book already exists'})

@app.route('/api/members/add', methods=['POST'])
def api_add_member():
    data = request.json
    
    success = lib.add_member(data['member_id'], data['name'])
    
    if success:
        lib.save_members()
        return jsonify({'success': True, 'message': 'Member added successfully'})
    else:
        return jsonify({'success': False, 'message': 'Member already exists'})

@app.route('/api/members/all', methods=['GET'])
def api_get_all_members():
    members_data = []
    
    for member_id, member in lib.members.table_items():
        borrowed_books_details = []
        for isbn in member.borrowed_books:
            book_node = lib.books.search(isbn)
            if book_node:
                borrowed_books_details.append({
                    'isbn': isbn,
                    'title': book_node.value['title']
                })
        
        members_data.append({
            'member_id': member_id,
            'name': member.name,
            'borrowed_count': len(member.borrowed_books),
            'borrowed_books': borrowed_books_details
        })
    
    return jsonify(members_data)

@app.route('/api/members/<member_id>', methods=['GET'])
def api_get_member(member_id):
    member = lib.members.get_member(member_id)
    
    if not member:
        return jsonify({'success': False, 'message': 'Member not found'}), 404
    
    borrowed_books_details = []
    for isbn in member.borrowed_books:
        book_node = lib.books.search(isbn)
        if book_node:
            borrowed_books_details.append({
                'isbn': isbn,
                'title': book_node.value['title'],
                'author': book_node.value['author'],
                'category': book_node.value['category']
            })
    
    return jsonify({
        'member_id': member_id,
        'name': member.name,
        'borrowed_count': len(member.borrowed_books),
        'borrowed_books': borrowed_books_details,
        'can_borrow': member.can_borrow()
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)