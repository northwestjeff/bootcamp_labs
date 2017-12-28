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
var thecircle = new Book("The Circle", "Miller", 120, false)

myLibrary.push(learn, gonegirl, thecircle)



function addBook() {

}


function render(array) {
    for (i = 0; i < myLibrary.length; i++) {
        const main = document.getElementById('shelf');
        const div = document.createElement("div")
        div.innerHTML = array[i].title;
        main.appendChild(div)

    }
}

// NEW BOOK button that pops up a form
// add a button for read/unread
// add a button to remove from library
//


render(myLibrary)
