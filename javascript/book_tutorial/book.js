myLibrary = [];

function Book(title, author, pages, read) {
    this.title = title;
    this.author = author;
    this.pages = pages;
    this.read = read;
    this.info = function () {
        return title + " is a book by " + author + "which is " + pages + " pages. " + read
    }
}

var learn = new Book("Learn Python the Hardway", "Stevens", 200, true);
var gonegirl = new Book("Gone Girl", "Jackson", 360, true);
var thecircle = new Book("The Circle", "Miller", 120, false);


function addBookToLibrary(book) {
    myLibrary.push(book)
}
// myLibrary.push(learn, gonegirl, thecircle);
addBookToLibrary(learn);
addBookToLibrary(gonegirl);
addBookToLibrary(thecircle);

function addBookSection(newBook) {
    const buttonClick = document.getElementById('new-book-button')
    buttonClick.addEventListener('click', function () {
        console.log('new book button clicked');
        const newBookSection = document.getElementById('new-book-form')
        newBookSection.style.display = 'block';
    })

}

function newBookSubmission() {
    const form = document.querySelector('#new-book-form');
    const submit = document.getElementById('new-submit')
    form.onSubmit = function (e) {
        console.log(form);
        // e.preventDefault();
        // // const {title, author, pages, read } = form;
        // console.log(read.value);
        // addBookToLibrary(new Book(
        //     title.value,
        //     author.value,
        //     pages.value,
        //     read.value
        // ))
    }
}


function render(array) {
    for (i = 0; i < myLibrary.length; i++) {

        // CREATES BOOK
        const shelf = document.getElementById('shelf');
        const div = document.createElement("div");
        shelf.appendChild(div);
        div.className = 'book';
        div.id = i;

        // TITLE SECTION
        const book = document.getElementById(i);
        const bookTitle = document.createElement('h2');
        bookTitle.className = 'title';
        book.appendChild(bookTitle);
        bookTitle.innerHTML = array[i].title;

        //AUTHOR SECTION
        const bookAuthor = document.createElement('h4');
        bookAuthor.className = 'author';
        book.appendChild(bookAuthor);
        bookAuthor.innerHTML = "By: " + array[i].author;

        // PAGES SECTION
        const bookPages = document.createElement('p');
        bookPages.classname = 'pages';
        book.appendChild(bookPages);
        bookPages.innerHTML = array[i].pages + ' pages';

        // READ/UNREAD SECTIONS
        const bookRead = document.createElement('p');
        bookRead.className = 'read';
        book.appendChild(bookRead);
        if (array[i].read) {
            bookRead.innerHTML = 'I have read this book.'
        } else {
            bookRead.innerHTML = 'I have not read this book, yet';
            const bookButton = document.createElement('input');
            bookButton.className = 'read-button';
            bookButton.id = 'read-button';
            bookButton.type = 'button';
            bookButton.value = "Mark Read!";
            book.appendChild(bookButton);
        }
        const removeButton = document.createElement('input');
        removeButton.className = 'remove-button';
        // removeButton.id = 'remove-button';
        removeButton.type = 'button';
        removeButton.value = "Remove Book from Shelf";
        book.appendChild(removeButton);
    }
}

function removeClick() {
    const button = document.getElementsByClassName('remove-button');
    for (i = 0; i < button.length; i++) {
        button[i].addEventListener('click', function () {
            console.log(this.parentElement.style.display = 'none')
                // button[i].parentElement.style.display = 'none'
            }
            , false);
    }

}

function newBook() {
    const button = document.getElementById('new-book');
    button.prompt("Please Enter Book Details:")

}


// NEW BOOK button that pops up a form
// Add event listener to 'Mark Read!' button to change the .read to true
// add a button to remove from library
//


render(myLibrary);
removeClick();
addBookSection();
newBookSubmission();
