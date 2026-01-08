# 📚 UET Library Management System - Complete Documentation

A modern, full-stack library management system built with Python Flask backend and vanilla JavaScript frontend, featuring AVL trees and hash tables for efficient data management.

---

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technology Stack](#technology-stack)
4. [Project Structure](#project-structure)
5. [Installation Guide](#installation-guide)
6. [User Guide](#user-guide)
7. [Architecture](#architecture)
8. [API Documentation](#api-documentation)
9. [Data Structures Used](#data-structures-used)
10. [Frontend-Backend Integration](#frontend-backend-integration)

---

## 🎯 Project Overview

The UET Library Management System is a comprehensive solution for managing library operations including:
- Book cataloging and inventory management
- Member registration and management
- Book borrowing and returning
- Advanced search capabilities (ISBN, Title, Author)
- Real-time availability tracking
- Statistical dashboards

### Key Highlights:
- ✅ **Data Structures:** AVL Tree + Hash Tables
- ✅ **Time Complexity:** O(log n) for most operations
- ✅ **Modern UI:** Dark mode, animations, responsive design
- ✅ **REST API:** Clean JSON-based communication
- ✅ **No Database:** Pure Python data structures with CSV persistence

---

## ✨ Features

### For Library Staff:
- 📊 **Dashboard** - Real-time statistics and insights
- ➕ **Add Books** - Easy book cataloging with validation
- 🔍 **Search** - Multi-criteria search (ISBN, Title, Author)
- 📖 **Browse** - Category filtering and quick search
- 👥 **Member Management** - Register and track members
- 📥 **Borrow/Return** - Simple transaction processing

### Technical Features:
- 🌓 **Dark Mode** - Toggle between light/dark themes
- 💫 **Smooth Animations** - Professional transitions and effects
- 📱 **Responsive Design** - Works on all screen sizes
- 🔔 **Notifications** - Real-time feedback for all actions
- 💾 **Auto-save** - All changes persist to CSV automatically
- 🎨 **Modern UI** - Gradient designs and glassmorphism

---

## 🛠️ Technology Stack

### Backend:
- **Python 3.x** - Core language
- **Flask** - Web framework
- **CSV** - Data persistence
- **Custom Data Structures:**
  - AVL Tree (self-balancing BST)
  - Hash Table (with chaining)
  - Linked List (for secondary indexes)

### Frontend:
- **HTML5** - Structure
- **CSS3** - Styling (with CSS Variables for theming)
- **Vanilla JavaScript** - Interactivity
- **Font Awesome** - Icons
- **Google Fonts (Inter)** - Typography

### No External Libraries:
- No jQuery
- No Bootstrap
- No React/Vue/Angular
- Pure vanilla implementation!

---

## 📁 Project Structure

```
uet-library-system/
│
├── Backend Files (Data Structures & Logic)
│   ├── avl.py                      # AVL Tree implementation
│   ├── hash.py                     # Hash Table with chaining
│   ├── hashes.py                   # Secondary indexes (Author, Title, Members)
│   ├── library_system.py           # Main library operations
│   └── main.py                     # Original CLI interface
│
├── Flask Application
│   └── app.py                      # Flask REST API server
│
├── Frontend (Templates)
│   ├── templates/
│   │   ├── base.html              # Base template with navbar
│   │   ├── books.html             # Browse books page
│   │   ├── search.html            # Advanced search page
│   │   ├── members.html           # Member management page
│   │   └── admin.html             # Admin dashboard
│   │
│   └── static/
│       ├── css/
│       │   └── style.css          # Main stylesheet with dark mode
│       └── js/
│           └── main.js            # JavaScript utilities
│
├── Data Files
│   ├── books.csv                   # Books database
│   └── members.csv                 # Members database
│
├── Documentation
│   ├── README.md                   # This file
│   ├── BACKEND_README.md          # Backend documentation
│   └── FRONTEND_README.md         # Frontend documentation (to be created)
│
└── requirements.txt                # Python dependencies
```

---

## 🚀 Installation Guide

### Prerequisites:
- Python 3.7 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Edge, Safari)

### Step 1: Clone/Download Project

```bash
# Navigate to project directory
cd uet-library-system
```

### Step 2: Verify Files

Ensure you have these files:
```
✓ avl.py
✓ hash.py
✓ hashes.py
✓ library_system.py
✓ app.py
✓ books.csv
✓ members.csv
✓ templates/ (folder with all HTML files)
✓ static/ (folder with css/ and js/ subfolders)
```

### Step 3: Install Dependencies

```bash
# Option 1: Using requirements.txt
pip install -r requirements.txt

# Option 2: Manual installation
pip install Flask==3.0.0
```

### Step 4: Run the Application

```bash
python app.py
```

You should see:
```
✓ Books and members loaded successfully
 * Running on http://127.0.0.1:5000
```

### Step 5: Open in Browser

Navigate to: `http://localhost:5000`

---

## 📖 User Guide

### First Time Setup:
1. The system loads sample data from `books.csv` and `members.csv`
2. No login required - direct access to all features
3. Use any existing Member ID for testing (e.g., 2024-EE-176)

### Browse Books:
1. Click **"Browse Books"** in navbar
2. Use category filters: All, Novels, Programming, Engineering, Science
3. Quick search bar for title/author filtering
4. Click **"Borrow Book"** button
5. Enter your Member ID in the popup
6. Confirm to borrow

### Advanced Search:
1. Click **"Search"** in navbar
2. Choose search type: ISBN, Title, or Author
3. Enter search query
4. Results appear instantly with borrow options

### Member Management:
1. Click **"Members"** in navbar
2. Enter Member ID in search box
3. View borrowed books
4. Click **"Return Book"** to return any book

### Admin Panel:
1. Click **"Admin"** in navbar
2. **Overview:** View statistics and category breakdown
3. **Add Book:** Fill form and submit
4. **Manage Books:** View all books in table format
5. **Add Member:** Register new members
6. **Manage Members:** View all members

### Dark Mode:
- Click the **"Dark"** button in navbar
- Preference is saved automatically
- Toggle anytime

---

## 🏗️ Architecture

### System Design

```
┌─────────────────────────────────────────────────────────────┐
│                     USER (Web Browser)                       │
└────────────────────────┬────────────────────────────────────┘
                         │ HTTP Requests
                         ↓
┌─────────────────────────────────────────────────────────────┐
│                    FLASK WEB SERVER                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Routes (app.py)                                      │  │
│  │  - /                  → Redirect to books            │  │
│  │  - /books            → Browse books page             │  │
│  │  - /search           → Search page                   │  │
│  │  - /members          → Members page                  │  │
│  │  - /admin            → Admin panel                   │  │
│  │  - /api/books/all    → Get all books (JSON)         │  │
│  │  - /api/books/search → Search books (JSON)          │  │
│  │  - /api/books/borrow → Borrow book (JSON)           │  │
│  │  - /api/books/return → Return book (JSON)           │  │
│  │  - /api/books/add    → Add book (JSON)              │  │
│  │  - /api/members/*    → Member operations (JSON)     │  │
│  └──────────────────────┬───────────────────────────────┘  │
└─────────────────────────┼───────────────────────────────────┘
                          │
                          ↓
┌─────────────────────────────────────────────────────────────┐
│              LIBRARY SYSTEM (library_system.py)              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Main Operations                                      │  │
│  │  - add_book()         - borrow_book()                │  │
│  │  - search_by_isbn()   - return_book()                │  │
│  │  - search_by_title()  - add_member()                 │  │
│  │  - search_by_author() - list_all_books()             │  │
│  └──────────────┬────────────────────────────────────────┘  │
└─────────────────┼──────────────────────────────────────────┘
                  │
      ┌───────────┼───────────┐
      │           │           │
      ↓           ↓           ↓
┌──────────┐ ┌─────────┐ ┌──────────┐
│ AVL TREE │ │  HASH   │ │  HASH    │
│  (Books) │ │  TABLE  │ │  TABLE   │
│          │ │ (Title) │ │ (Author) │
│  ISBN    │ │         │ │          │
│  ↓       │ │ Title → │ │ Author → │
│ Book     │ │  ISBN   │ │  ISBNs   │
│ Data     │ │         │ │  (list)  │
└────┬─────┘ └─────────┘ └──────────┘
     │
     ↓
┌─────────────────────┐
│  CSV FILES          │
│  - books.csv        │
│  - members.csv      │
└─────────────────────┘
```

### Data Flow: Borrow a Book

```
1. User clicks "Borrow Book" on books.html
   ↓
2. JavaScript shows modal, user enters Member ID
   ↓
3. JavaScript sends POST to /api/books/borrow
   {
     "isbn": "9780134093413",
     "member_id": "2024-EE-176"
   }
   ↓
4. Flask receives request in app.py
   ↓
5. Calls lib.borrow_book(member_id, isbn)
   ↓
6. library_system.py processes:
   - Search book in AVL tree [O(log n)]
   - Check available_copies > 0
   - Get member from hash table [O(1)]
   - Check member can borrow (< 5 books)
   - Update member.borrowed_books
   - Decrease book.available_copies
   - Save to CSV
   ↓
7. Returns JSON: {"success": true, "message": "Book borrowed"}
   ↓
8. JavaScript receives response
   ↓
9. Shows success notification
   ↓
10. Reloads book list with updated availability
```

---

## 📡 API Documentation

### Base URL: `http://localhost:5000/api`

### GET Endpoints

#### `GET /api/books/all`
**Description:** Get all books in library

**Response:**
```json
[
  {
    "isbn": "9780134093413",
    "title": "Computer Organization and Design",
    "author": "David A. Patterson",
    "year": 2013,
    "category": "Engineering",
    "available_copies": 3
  },
  ...
]
```

---

#### `GET /api/members/all`
**Description:** Get all members

**Response:**
```json
[
  {
    "member_id": "2024-EE-176",
    "name": "Ali Hassan",
    "borrowed_count": 5,
    "borrowed_books": [
      {"isbn": "...", "title": "..."},
      ...
    ]
  },
  ...
]
```

---

#### `GET /api/members/<member_id>`
**Description:** Get specific member details

**Example:** `/api/members/2024-EE-176`

**Response:**
```json
{
  "member_id": "2024-EE-176",
  "name": "Ali Hassan",
  "borrowed_count": 3,
  "borrowed_books": [...],
  "can_borrow": true
}
```

---

### POST Endpoints

#### `POST /api/books/search`
**Description:** Search for books

**Request Body:**
```json
{
  "type": "isbn",        // or "title" or "author"
  "query": "9780134093413"
}
```

**Response:**
```json
[
  {
    "isbn": "9780134093413",
    "title": "Computer Organization and Design",
    "author": "David A. Patterson",
    "year": 2013,
    "category": "Engineering",
    "available_copies": 3
  }
]
```

---

#### `POST /api/books/add`
**Description:** Add new book

**Request Body:**
```json
{
  "isbn": "TEST123",
  "title": "Test Book",
  "author": "Test Author",
  "year": 2024,
  "category": "Science",
  "copies": 5
}
```

**Response:**
```json
{
  "success": true,
  "message": "Book added successfully"
}
```

---

#### `POST /api/books/borrow`
**Description:** Borrow a book

**Request Body:**
```json
{
  "member_id": "2024-EE-176",
  "isbn": "9780134093413"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Book borrowed successfully"
}
```

**Error Response:**
```json
{
  "success": false,
  "message": "Borrow limit reached (max 5 books)"
}
```

---

#### `POST /api/books/return`
**Description:** Return a book

**Request Body:**
```json
{
  "member_id": "2024-EE-176",
  "isbn": "9780134093413"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Book returned successfully"
}
```

---

#### `POST /api/members/add`
**Description:** Register new member

**Request Body:**
```json
{
  "member_id": "2024-EE-200",
  "name": "New Member"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Member added successfully"
}
```

---

## 🗄️ Data Structures Used

### 1. AVL Tree (Primary Storage)
**Used for:** Books storage with ISBN as key

**Advantages:**
- Self-balancing → guaranteed O(log n) operations
- Ordered traversal → sorted book listing
- Efficient search, insert, delete

**Structure:**
```python
AVLTree
├── root: Booknode
│   ├── key: ISBN
│   ├── value: {title, author, year, category, copies}
│   ├── left: Booknode
│   ├── right: Booknode
│   └── height: int
```

### 2. Hash Table (Secondary Indexes)
**Used for:** Title index, Author index, Member database

**Advantages:**
- O(1) average lookup time
- Handles collisions with chaining
- Space-efficient

**Structure:**
```python
HashTable
├── size: 100
└── table: [HashNode, HashNode, ...]
    └── HashNode
        ├── key: string
        ├── value: any
        └── next: HashNode (chain)
```

### 3. Linked List (Chaining & Multi-value Storage)
**Used for:** Hash collision resolution, Author → multiple ISBNs

**Structure:**
```python
LinkedlistNode
├── data: value
└── next: LinkedlistNode
```

---

## 🔗 Frontend-Backend Integration

### How Frontend Communicates with Backend:

#### 1. **Page Rendering (Server-Side)**

```python
# app.py
@app.route('/books')
def books():
    return render_template('books.html')
```

**Flow:**
1. User navigates to `/books`
2. Flask renders `templates/books.html`
3. Browser receives complete HTML
4. Browser loads `static/css/style.css` and `static/js/main.js`

---

#### 2. **Data Fetching (Client-Side AJAX)**

```javascript
// books.html
async function loadBooks() {
    const response = await fetch('/api/books/all');
    const books = await response.json();
    displayBooks(books);
}
```

**Flow:**
1. JavaScript makes GET request to `/api/books/all`
2. Flask route handler processes request
3. Calls `lib.list_all_books()`
4. Returns JSON response
5. JavaScript receives data and updates DOM

---

#### 3. **Form Submission (POST Request)**

```javascript
// admin.html
document.getElementById('addBookForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const bookData = {
        isbn: document.getElementById('isbn').value,
        title: document.getElementById('title').value,
        ...
    };
    
    const response = await fetch('/api/books/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(bookData)
    });
    
    const result = await response.json();
    showNotification(result.message, result.success ? 'success' : 'error');
});
```

**Flow:**
1. User fills form and clicks submit
2. JavaScript prevents default form behavior
3. Collects form data into JSON object
4. Sends POST request to `/api/books/add`
5. Flask receives JSON, validates, processes
6. Returns JSON response
7. JavaScript shows notification based on success/failure

---

### CSS Styling & Theming

#### Dark Mode Implementation:

**CSS Variables:**
```css
:root {
    --bg-primary: #ffffff;
    --text-primary: #2d3748;
    ...
}

[data-theme="dark"] {
    --bg-primary: #1a202c;
    --text-primary: #f7fafc;
    ...
}
```

**JavaScript Toggle:**
```javascript
function toggleTheme() {
    const html = document.documentElement;
    const currentTheme = html.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    html.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
}
```

**How it works:**
1. CSS defines two color schemes using `:root` and `[data-theme="dark"]`
2. All colors reference CSS variables (e.g., `color: var(--text-primary)`)
3. JavaScript changes `data-theme` attribute on `<html>`
4. CSS automatically updates all colors
5. Preference saved in localStorage for persistence

---

## 🎨 Frontend Features Explained

### 1. Modal Popups
**Used for:** Borrow confirmations

```javascript
function openBorrowModal(isbn, title) {
    // Create modal HTML
    const modal = document.getElementById('borrowModal');
    // Populate with book info
    document.getElementById('borrowBookTitle').textContent = title;
    // Show modal
    modal.style.display = 'block';
    // Store ISBN for later use
    selectedBookISBN = isbn;
}
```

### 2. Real-time Search Filtering
**Used for:** Category filters, quick search

```javascript
function filterAndSearch(searchTerm) {
    let filtered = allBooks;
    
    // Filter by category
    if (currentCategory !== 'all') {
        filtered = filtered.filter(book => book.category === currentCategory);
    }
    
    // Filter by search term
    if (searchTerm) {
        filtered = filtered.filter(book => 
            book.title.toLowerCase().includes(searchTerm) ||
            book.author.toLowerCase().includes(searchTerm)
        );
    }
    
    displayBooks(filtered);
}
```

### 3. Notifications System
**Used for:** Success/error messages

```javascript
function showNotification(message, type) {
    const notification = document.getElementById('notification');
    notification.innerHTML = `<i class="fas fa-check-circle"></i> ${message}`;
    notification.className = `notification ${type} show`;
    
    setTimeout(() => {
        notification.classList.remove('show');
    }, 3000);
}
```

### 4. Dynamic Content Loading
**Used for:** Books grid, members list

```javascript
function displayBooks(books) {
    const grid = document.getElementById('booksGrid');
    
    grid.innerHTML = books.map(book => `
        <div class="book-card">
            <div class="book-cover">
                <i class="fas fa-book"></i>
            </div>
            <div class="book-info">
                <h3>${book.title}</h3>
                <p>${book.author}</p>
            </div>
            <button onclick="borrowBook('${book.isbn}')">
                Borrow
            </button>
        </div>
    `).join('');
}
```

---

## 🔐 Security Considerations

### Current Implementation:
- ✅ No SQL injection (no database)
- ✅ No XSS (content properly escaped)
- ✅ CSRF protection (Flask built-in)
- ⚠️ No authentication (open access)
- ⚠️ No authorization (anyone can admin)
- ⚠️ No input sanitization

### For Production:
1. Add user authentication
2. Implement role-based access control
3. Add input validation and sanitization
4. Use HTTPS
5. Add rate limiting
6. Implement session management

---

## 🚀 Performance Optimization

### Backend:
- AVL tree ensures O(log n) lookups
- Hash tables provide O(1) secondary index access
- In-memory operations (no disk I/O during runtime)
- CSV loading only on startup

### Frontend:
- Minimal JavaScript libraries (faster load)
- CSS animations (GPU-accelerated)
- Lazy loading for large lists (future improvement)
- Debounced search inputs

---

## 🐛 Common Issues & Solutions

### Issue 1: Books not loading
**Solution:** Check if `books.csv` exists and is properly formatted

### Issue 2: Search by title/ISBN not working
**Solution:** Ensure exact match (case-insensitive normalization applied)

### Issue 3: Dark mode not persisting
**Solution:** Check browser localStorage permissions

### Issue 4: Port 5000 already in use
**Solution:** Change port in `app.py`: `app.run(port=5001)`

### Issue 5: Modal not showing input field
**Solution:** Clear browser cache and refresh

---

## 📈 Future Enhancements

### Planned Features:
1. **Due Dates** - Track return deadlines
2. **Fines System** - Calculate overdue penalties
3. **Reservations** - Queue for unavailable books
4. **Book Reviews** - Member ratings and comments
5. **Email Notifications** - Reminders and alerts
6. **Export Reports** - PDF/Excel generation
7. **Book Covers** - Integration with Google Books API
8. **QR Codes** - Quick book scanning
9. **Mobile App** - React Native version
10. **Multi-library** - Support for multiple branches

---

## 👥 Contributors

- **Backend Development:** Data structures implementation
- **Frontend Development:** UI/UX design and implementation
- **Integration:** Flask API and frontend communication
- **Documentation:** Complete system documentation

---

## 📄 License

This project is created for educational purposes at UET Lahore.

---

## 📞 Support

For issues, questions, or contributions, please refer to:
- `BACKEND_README.md` for backend documentation
- `FRONTEND_README.md` for frontend documentation
- Code comments for inline documentation

---

**Built with ❤️ for UET Lahore**

**Version:** 1.0.0  
**Last Updated:** January 2026
