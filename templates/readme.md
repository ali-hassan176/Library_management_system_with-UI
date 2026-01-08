# Frontend Documentation - UET Library Management System

## 📁 Frontend Structure

```
frontend/
├── templates/
│   ├── base.html       # Base template with navbar and layout
│   ├── books.html      # Browse books with filters
│   ├── search.html     # Advanced search interface
│   ├── members.html    # Member lookup and management
│   └── admin.html      # Admin dashboard with sidebar
│
└── static/
    ├── css/
    │   └── style.css   # Main stylesheet with dark mode
    └── js/
        └── main.js     # JavaScript utilities and dark mode
```

---

## 🎨 Design System

### Color Palette

#### Light Mode:
```css
--primary: #667eea        /* Purple-Blue gradient start */
--secondary: #764ba2      /* Purple gradient end */
--success: #48bb78        /* Green for success */
--danger: #f56565         /* Red for errors */
--warning: #ed8936        /* Orange for warnings */
--info: #4299e1           /* Blue for info */
--bg-primary: #ffffff     /* White background */
--bg-secondary: #f7fafc   /* Light gray */
--text-primary: #2d3748   /* Dark text */
--text-secondary: #718096 /* Gray text */
```

#### Dark Mode:
```css
--primary: #7c3aed        /* Brighter purple */
--secondary: #a855f7      /* Brighter purple gradient */
--bg-primary: #1a202c     /* Dark navy */
--bg-secondary: #2d3748   /* Dark gray */
--text-primary: #f7fafc   /* Light text */
--text-secondary: #cbd5e0 /* Light gray text */
```

### Typography:
- **Font Family:** Inter (Google Fonts)
- **Headings:** 2.5rem - 1rem, weight 700-800
- **Body:** 1rem, weight 400-500
- **Small Text:** 0.85rem, weight 400

### Spacing System:
- **Base unit:** 1rem = 16px
- **Small:** 0.5rem (8px)
- **Medium:** 1rem (16px)
- **Large:** 2rem (32px)
- **Extra Large:** 3rem (48px)

### Border Radius:
- **Small:** 10px (inputs, buttons)
- **Medium:** 15px (cards)
- **Large:** 20px (sections)
- **Extra Large:** 50px (pills, avatars)

---

## 🏗️ Template Architecture

### Template Inheritance Flow

```
base.html (Parent Template)
    ↓
    ├── books.html (Child)
    ├── search.html (Child)
    ├── members.html (Child)
    └── admin.html (Child)
```

### base.html - Master Template

**Structure:**
```html
<!DOCTYPE html>
<html>
<head>
    <!-- Meta tags, title, CSS -->
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <nav class="navbar">
        <!-- Navigation bar -->
    </nav>
    
    <main class="main-content">
        {% block content %}
        <!-- Child content goes here -->
        {% endblock %}
    </main>
    
    <div id="notification"></div>
    
    <script src="/static/js/main.js"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

**Key Features:**
1. **Navbar Component** - Sticky navigation with active states
2. **Dark Mode Toggle** - Theme switcher button
3. **Notification Container** - For toast messages
4. **Block System** - Jinja2 template inheritance

---

## 📄 Page-by-Page Breakdown

### 1. books.html - Browse Books Page

#### Purpose:
Browse all books with category filtering and quick search

#### HTML Structure:
```html
<div class="books-page-container">
    <div class="page-header">
        <h1>Browse Library Collection</h1>
    </div>
    
    <div class="filters-section">
        <input id="quickSearch">
        <button class="filter-btn" data-category="all">All</button>
        <button class="filter-btn" data-category="Novel">Novels</button>
        ...
    </div>
    
    <div id="booksGrid" class="books-grid">
        <!-- JavaScript populates book cards here -->
    </div>
</div>

<div id="borrowModal" class="modal">
    <!-- Borrow confirmation modal -->
</div>
```

#### JavaScript Flow:

**1. Load Books on Page Load:**
```javascript
async function loadBooks() {
    // Fetch all books from API
    const response = await fetch('/api/books/all');
    const books = await response.json();
    
    // Store globally for filtering
    allBooks = books;
    
    // Display on page
    displayBooks(books);
}

// Called when page loads
loadBooks();
```

**2. Display Books:**
```javascript
function displayBooks(books) {
    const grid = document.getElementById('booksGrid');
    
    // Generate HTML for each book
    grid.innerHTML = books.map(book => `
        <div class="book-card">
            <div class="book-badge ${book.available_copies > 0 ? 'available' : 'unavailable'}">
                ${book.available_copies > 0 ? 'Available' : 'Unavailable'}
            </div>
            <div class="book-cover">
                <i class="fas fa-book"></i>
            </div>
            <div class="book-info">
                <h3>${book.title}</h3>
                <p>${book.author}</p>
                <p>${book.isbn}</p>
                <span class="book-category">${book.category}</span>
                <div class="book-copies">${book.available_copies} copies</div>
            </div>
            <button onclick="openBorrowModal('${book.isbn}', '${book.title}')">
                Borrow Book
            </button>
        </div>
    `).join('');
}
```

**3. Category Filtering:**
```javascript
// When user clicks a category button
function filterByCategory(category) {
    currentCategory = category;
    
    // Update active button
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    event.target.classList.add('active');
    
    // Apply filter
    const filtered = allBooks.filter(book => 
        category === 'all' || book.category === category
    );
    
    displayBooks(filtered);
}

// Attach to buttons
document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        filterByCategory(btn.dataset.category);
    });
});
```

**4. Quick Search:**
```javascript
// Real-time filtering as user types
document.getElementById('quickSearch').addEventListener('input', (e) => {
    const searchTerm = e.target.value.toLowerCase();
    
    const filtered = allBooks.filter(book => 
        book.title.toLowerCase().includes(searchTerm) ||
        book.author.toLowerCase().includes(searchTerm)
    );
    
    displayBooks(filtered);
});
```

**5. Borrow Modal:**
```javascript
// Open modal
function openBorrowModal(isbn, title) {
    selectedBookISBN = isbn;
    document.getElementById('borrowBookTitle').textContent = title;
    document.getElementById('borrowModal').style.display = 'block';
}

// Close modal
function closeModal() {
    document.getElementById('borrowModal').style.display = 'none';
}

// Confirm borrow
async function confirmBorrow() {
    const memberId = document.getElementById('borrowMemberId').value.trim();
    
    if (!memberId) {
        showNotification('Please enter Member ID', 'warning');
        return;
    }
    
    // Send API request
    const response = await fetch('/api/books/borrow', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            isbn: selectedBookISBN,
            member_id: memberId
        })
    });
    
    const data = await response.json();
    
    if (data.success) {
        showNotification('Book borrowed successfully!', 'success');
        closeModal();
        loadBooks(); // Refresh to show updated availability
    } else {
        showNotification(data.message, 'error');
    }
}
```

**Flow Diagram: Borrowing a Book**
```
User clicks "Borrow Book"
    ↓
openBorrowModal(isbn, title)
    ↓
Modal appears with input field
    ↓
User enters Member ID
    ↓
User clicks "Confirm Borrow"
    ↓
confirmBorrow() function
    ↓
Validate Member ID entered
    ↓
fetch('/api/books/borrow', {POST})
    ↓
Wait for server response
    ↓
data = await response.json()
    ↓
if (data.success):
    Show success notification
    Close modal
    Reload books (updated availability)
else:
    Show error notification
```

---

### 2. search.html - Advanced Search Page

#### Purpose:
Search books by ISBN, Title, or Author with tab interface

#### HTML Structure:
```html
<div class="search-page-container">
    <div class="search-panel">
        <div class="search-tabs">
            <button class="search-tab active" data-type="isbn">ISBN</button>
            <button class="search-tab" data-type="title">Title</button>
            <button class="search-tab" data-type="author">Author</button>
        </div>
        
        <div class="search-content">
            <div class="search-input-group">
                <i class="fas fa-search"></i>
                <input id="searchInput" placeholder="Enter ISBN...">
                <button id="searchBtn">Search</button>
            </div>
        </div>
    </div>
    
    <div id="searchResults">
        <!-- Results appear here -->
    </div>
</div>
```

#### JavaScript Flow:

**1. Tab Switching:**
```javascript
let currentSearchType = 'isbn';

const placeholders = {
    isbn: 'Enter ISBN number...',
    title: 'Enter book title...',
    author: 'Enter author name...'
};

document.querySelectorAll('.search-tab').forEach(tab => {
    tab.addEventListener('click', () => {
        // Update active tab
        document.querySelectorAll('.search-tab').forEach(t => 
            t.classList.remove('active')
        );
        tab.classList.add('active');
        
        // Change search type
        currentSearchType = tab.dataset.type;
        
        // Update placeholder
        document.getElementById('searchInput').placeholder = 
            placeholders[currentSearchType];
        
        // Clear previous results
        document.getElementById('searchResults').innerHTML = `
            <div class="search-placeholder">
                <i class="fas fa-search"></i>
                <h3>Start Your Search</h3>
            </div>
        `;
    });
});
```

**2. Perform Search:**
```javascript
async function performSearch() {
    const query = document.getElementById('searchInput').value.trim();
    
    if (!query) {
        showNotification('Please enter a search term', 'warning');
        return;
    }
    
    // Show loading
    const resultsDiv = document.getElementById('searchResults');
    resultsDiv.innerHTML = `
        <div class="loading">
            <i class="fas fa-spinner fa-spin"></i>
            Searching...
        </div>
    `;
    
    // Send search request
    const response = await fetch('/api/books/search', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            type: currentSearchType,
            query: query
        })
    });
    
    const books = await response.json();
    
    // Display results
    if (books.length === 0) {
        resultsDiv.innerHTML = `
            <div class="empty-state">
                <i class="fas fa-book-dead"></i>
                <h3>No Books Found</h3>
            </div>
        `;
    } else {
        resultsDiv.innerHTML = `
            <div class="results-header">
                <h3>Found ${books.length} book(s)</h3>
            </div>
            <div class="books-grid">
                ${books.map(book => /* book card HTML */).join('')}
            </div>
        `;
    }
}

// Attach to button
document.getElementById('searchBtn').addEventListener('click', performSearch);

// Also allow Enter key
document.getElementById('searchInput').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        performSearch();
    }
});
```

**Search Flow Diagram:**
```
User selects search type (tab)
    ↓
currentSearchType = 'isbn' | 'title' | 'author'
    ↓
User enters search query
    ↓
User clicks Search or presses Enter
    ↓
performSearch()
    ↓
Validate query not empty
    ↓
Show loading indicator
    ↓
POST /api/books/search
    {
        "type": "isbn",
        "query": "9780134093413"
    }
    ↓
Server searches using appropriate method:
    - ISBN → AVLTree.search()
    - Title → TitleIndex.get_isbn() → AVLTree.search()
    - Author → AuthorIndex.get_books() → AVLTree.search(each)
    ↓
Server returns JSON array of books
    ↓
Display results in grid OR show "No books found"
```

---

### 3. members.html - Member Management Page

#### Purpose:
Look up member information, view borrowed books, return books

#### HTML Structure:
```html
<div class="members-page-container">
    <!-- Member Lookup Section -->
    <div class="member-lookup-section">
        <h2>Member Lookup</h2>
        <input id="memberIdSearch" placeholder="Enter Member ID">
        <button onclick="searchMember()">Search</button>
    </div>
    
    <!-- Member Details Result -->
    <div id="memberResult"></div>
    
    <!-- All Members List -->
    <div class="all-members-section">
        <h2>All Members</h2>
        <div id="membersList"></div>
    </div>
</div>

<div id="returnModal" class="modal">
    <!-- Return book confirmation -->
</div>
```

#### JavaScript Flow:

**1. Search Specific Member:**
```javascript
async function searchMember() {
    const memberId = document.getElementById('memberIdSearch').value.trim();
    
    if (!memberId) {
        showNotification('Please enter Member ID', 'warning');
        return;
    }
    
    const resultDiv = document.getElementById('memberResult');
    resultDiv.innerHTML = '<div class="loading">Searching...</div>';
    
    // Fetch member data
    const response = await fetch(`/api/members/${memberId}`);
    
    if (!response.ok) {
        resultDiv.innerHTML = `
            <div class="empty-state">
                <h3>Member Not Found</h3>
                <p>No member with ID: ${memberId}</p>
            </div>
        `;
        return;
    }
    
    const member = await response.json();
    displayMemberDetail(member);
}
```

**2. Display Member Details:**
```javascript
function displayMemberDetail(member) {
    const resultDiv = document.getElementById('memberResult');
    
    let borrowedBooksHTML = '';
    if (member.borrowed_books.length > 0) {
        borrowedBooksHTML = `
            <h3>Currently Borrowed Books</h3>
            <div class="books-grid">
                ${member.borrowed_books.map(book => `
                    <div class="book-card borrowed">
                        <div class="book-badge">Borrowed</div>
                        <div class="book-cover">
                            <i class="fas fa-book"></i>
                        </div>
                        <div class="book-info">
                            <h3>${book.title}</h3>
                            <p>${book.author}</p>
                            <p>${book.isbn}</p>
                        </div>
                        <button class="btn btn-return" 
                                onclick="openReturnModal('${member.member_id}', '${book.isbn}', '${book.title}')">
                            Return Book
                        </button>
                    </div>
                `).join('')}
            </div>
        `;
    } else {
        borrowedBooksHTML = '<p>No borrowed books</p>';
    }
    
    resultDiv.innerHTML = `
        <div class="member-detail-card">
            <div class="member-header">
                <div class="member-avatar-large">
                    <i class="fas fa-user"></i>
                </div>
                <div>
                    <h2>${member.name}</h2>
                    <p>${member.member_id}</p>
                </div>
            </div>
            
            <div class="member-stats-row">
                <div class="stat-box">
                    <h3>${member.borrowed_count}</h3>
                    <p>Books Borrowed</p>
                </div>
                <div class="stat-box">
                    <h3>${5 - member.borrowed_count}</h3>
                    <p>Available Slots</p>
                </div>
            </div>
            
            ${borrowedBooksHTML}
        </div>
    `;
}
```

**3. Return Book:**
```javascript
async function confirmReturn() {
    const response = await fetch('/api/books/return', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            member_id: currentMemberId,
            isbn: currentReturnISBN
        })
    });
    
    const data = await response.json();
    
    if (data.success) {
        showNotification('Book returned successfully!', 'success');
        closeReturnModal();
        searchMember(); // Refresh member details
        loadAllMembers(); // Refresh members list
    } else {
        showNotification(data.message, 'error');
    }
}
```

**4. Load All Members:**
```javascript
async function loadAllMembers() {
    const list = document.getElementById('membersList');
    
    const response = await fetch('/api/members/all');
    const members = await response.json();
    
    list.innerHTML = `
        <div class="members-grid">
            ${members.map(member => `
                <div class="member-card">
                    <div class="member-avatar">
                        <i class="fas fa-user"></i>
                    </div>
                    <div class="member-info">
                        <h3>${member.name}</h3>
                        <p>${member.member_id}</p>
                        <div class="member-stats">
                            <span>${member.borrowed_count} borrowed</span>
                            <span>${5 - member.borrowed_count} available</span>
                        </div>
                    </div>
                </div>
            `).join('')}
        </div>
    `;
}

// Load on page load
loadAllMembers();
```

---

### 4. admin.html - Admin Dashboard

#### Purpose:
Manage books, members, and view statistics with sidebar navigation

#### HTML Structure:
```html
<div class="admin-dashboard">
    <!-- Sidebar Navigation -->
    <div class="admin-sidebar">
        <div class="sidebar-header">
            <h3>Admin Panel</h3>
        </div>
        <nav class="sidebar-nav">
            <a href="#" data-section="overview" onclick="showSection('overview')">
                Overview
            </a>
            <a href="#" data-section="add-book" onclick="showSection('add-book')">
                Add Book
            </a>
            <a href="#" data-section="manage-books" onclick="showSection('manage-books')">
                Manage Books
            </a>
            <a href="#" data-section="add-member" onclick="showSection('add-member')">
                Add Member
            </a>
            <a href="#" data-section="manage-members" onclick="showSection('manage-members')">
                Manage Members
            </a>
        </nav>
    </div>
    
    <!-- Main Content -->
    <div class="admin-main">
        <div id="overview-section" class="admin-section active">
            <!-- Statistics dashboard -->
        </div>
        <div id="add-book-section" class="admin-section">
            <!-- Add book form -->
        </div>
        <div id="manage-books-section" class="admin-section">
            <!-- Books table -->
        </div>
        <div id="add-member-section" class="admin-section">
            <!-- Add member form -->
        </div>
        <div id="manage-members-section" class="admin-section">
            <!-- Members table -->
        </div>
    </div>
</div>
```

#### JavaScript Flow:

**1. Section Switching:**
```javascript
function showSection(sectionName) {
    // Update sidebar active state
    document.querySelectorAll('.sidebar-link').forEach(link => {
        link.classList.remove('active');
    });
    document.querySelector(`[data-section="${sectionName}"]`)
        .classList.add('active');
    
    // Show/hide sections
    document.querySelectorAll('.admin-section').forEach(section => {
        section.classList.remove('active');
    });
    document.getElementById(`${sectionName}-section`)
        .classList.add('active');
    
    // Load data if needed
    if (sectionName === 'manage-books') {
        loadBooksTable();
    } else if (sectionName === 'manage-members') {
        loadMembersTable();
    }
}
```

**2. Load Statistics:**
```javascript
async function loadStats() {
    // Fetch both books and members
    const [booksRes, membersRes] = await Promise.all([
        fetch('/api/books/all'),
        fetch('/api/members/all')
    ]);
    
    const books = await booksRes.json();
    const members = await membersRes.json();
    
    // Calculate statistics
    const availableBooks = books.filter(b => b.available_copies > 0).length;
    const totalCopies = books.reduce((sum, b) => sum + b.available_copies, 0);
    
    // Update DOM
    document.getElementById('totalBooks').textContent = books.length;
    document.getElementById('availableBooks').textContent = availableBooks;
    document.getElementById('totalMembers').textContent = members.length;
    
    // Load category breakdown
    loadCategoryStats(books);
}

// Call on page load
loadStats();
```

**3. Category Statistics:**
```javascript
function loadCategoryStats(books) {
    const categories = {
        'Novel': { icon: '📖', count: 0 },
        'Programming': { icon: '💻', count: 0 },
        'Engineering': { icon: '⚙️', count: 0 },
        'Science': { icon: '🔬', count: 0 }
    };
    
    // Count books per category
    books.forEach(book => {
        if (categories[book.category]) {
            categories[book.category].count++;
        }
    });
    
    // Display in UI
    const categoryStatsDiv = document.getElementById('categoryStats');
    categoryStatsDiv.innerHTML = Object.entries(categories).map(([name, data]) => `
        <div class="category-item">
            <div>${data.icon} ${name}</div>
            <span>${data.count}</span>
        </div>
    `).join('');
}
```

**4. Add Book Form:**
```javascript
document.getElementById('addBookForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Collect form data
    const bookData = {
        isbn: document.getElementById('isbn').value.trim(),
        title: document.getElementById('title').value.trim(),
        author: document.getElementById('author').value.trim(),
        year: document.getElementById('year').value,
        category: document.getElementById('category').value,
        copies: document.getElementById('copies').value
    };
    
    // Send to API
    const response = await fetch('/api/books/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(bookData)
    });
    
    const data = await response.json();
    
    if (data.success) {
        showNotification('Book added successfully!', 'success');
        document.getElementById('addBookForm').reset();
        loadStats(); // Refresh statistics
    } else {
        showNotification(data.message, 'error');
    }
});
```

**5. Manage Books Table:**
```javascript
async function loadBooksTable() {
    const tableDiv = document.getElementById('booksTable');
    tableDiv.innerHTML = '<div class="loading">Loading...</div>';
    
    const response = await fetch('/api/books/all');
    const books = await response.json();
    
    // Generate HTML table
    tableDiv.innerHTML = `
        <table class="books-table">
            <thead>
                <tr>
                    <th>ISBN</th>
                    <th>Title</th>
                    <th>Author</th>
                    <th>Year</th>
                    <th>Category</th>
                    <th>Copies</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                ${books.map(book => `
                    <tr>
                        <td><code>${book.isbn}</code></td>
                        <td><strong>${book.title}</strong></td>
                        <td>${book.author}</td>
                        <td>${book.year}</td>
                        <td>${book.category}</td>
                        <td>${book.available_copies}</td>
                        <td>
                            <span class="table-badge ${book.available_copies > 0 ? 'badge-available' : 'badge-unavailable'}">
                                ${book.available_copies > 0 ? 'Available' : 'Unavailable'}
                            </span>
                        </td>
                    </tr>
                `).join('')}
            </tbody>
        </table>
    `;
}
```

**6. Table Search Filter:**
```javascript
let allBooks = []; // Store globally

async function loadBooksTable() {
    const response = await fetch('/api/books/all');
    allBooks = await response.json();
    displayBooksTable(allBooks);
}

function filterBooks() {
    const searchTerm = document.getElementById('bookSearchInput')
        .value.toLowerCase();
    
    const filtered = allBooks.filter(book => 
        book.title.toLowerCase().includes(searchTerm) ||
        book.author.toLowerCase().includes(searchTerm) ||
        book.isbn.toLowerCase().includes(searchTerm)
    );
    
    displayBooksTable(filtered);
}

// Attach to input
document.getElementById('bookSearchInput').addEventListener('input', filterBooks);
```

---

## 🎨 CSS Architecture

### Component-Based Styling

#### 1. **Layout Components:**
```css
/* Containers */
.main-content {
    max-width: 1400px;
    margin: 0 auto;
    padding: 2rem;
}

/* Grids */
.books-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 2rem;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
}
```

#### 2. **Card Components:**
```css
.book-card {
    background: var(--card-bg);
    border-radius: 20px;
    padding: 1.5rem;
    box-shadow: var(--shadow);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    border: 1px solid var(--border);
}

.book-card:hover {
    transform: translateY(-10px) scale(1.02);
    box-shadow: 0 20px 40px rgba(102, 126, 234, 0.2);
}
```

#### 3. **Button Components:**
```css
.btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: 12px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s;
    position: relative;
    overflow: hidden;
}

.btn::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.3);
    transform: translate(-50%, -50%);
    transition: width 0.6s, height 0.6s;
}

.btn:hover::before {
    width: 300px;
    height: 300px;
}

.btn-primary {
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    color: white;
}
```

#### 4. **Animation Components:**
```css
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(50px) scale(0.9);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

@keyframes pulse {
    0%, 100% {
        opacity: 1;
        transform: scale(1);
    }
    50% {
        opacity: 0.7;
        transform: scale(1.05);
    }
}
```

---

## ⚙️ JavaScript Utilities (main.js)

### 1. **Dark Mode Toggle:**
```javascript
function toggleTheme() {
    const html = document.documentElement;
    const currentTheme = html.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    html.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    
    // Update button text/icon
    const icon = document.getElementById('themeIcon');
    const text = document.getElementById('themeText');
    
    if (newTheme === 'dark') {
        icon.className = 'fas fa-sun';
        text.textContent = 'Light';