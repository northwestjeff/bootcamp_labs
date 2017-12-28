


myLibrary = [];

const learn = Book("Learn Python the Hardway", "Stevens", 200, true);
const gonegirl = Book("Gone Girl", "Jackson", 360, true);
const thecircle = Book("The Circle", "Miller", 120, false)



function Book(title, author, pages, read) {
    this.title = title;
    this.author = author;
    this.pages = pages;
    this.read = read;
    this.info = function () {
        return title + " is a book by " + author + "which is " + pages + " pages. " + read
    }
}

function addBook() {

}


function render() {
    for (i = 0; i < myLibrary.length; i ++) {
        const main = document.getElementById('main');
        const div = document.createElement("div")
        div.innerHTML = myLibrary[i]
        main.appendChild(div)

    }
}

// NEW BOOK button that pops up a form
// add a button for read/unread
// add a button to remove from library
//


render()
