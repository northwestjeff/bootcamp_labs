var die1 = new Die(1);
var die2 = new Die(2);

var round1 = new Round(1, 3);
var round2 = new Round(2, 7);
var round3 = new Round(3, 11);

var dieList = [die1, die2];
var rollList = [die1, die2];
var currentRound = round1


function Round(num, sum) {
    this.num = num;
    this.complete = false
    this.sum = sum
}

function Die(id) {
    this.number = id;
    this.held = false;
    this.value = 3;
    this.roll = function() {
        console.log("ROlling!!!")
        if (this.held === false) {
            this.value = Math.floor(Math.random() * 6) + 1;
            console.log("die" + this.number + " random" + this.value )
        }
    }
}

// Starts the game with blank Holds
$('.btn--radius')[0].classList.remove("held")
$('.btn--radius')[0].innerText = "HOLD"

// checks for the word "Held" to add the Held class or not
function holdCheck(elem){
    if (elem.classList.value.includes("held") === true) {
        elem.innerText = "HOLD";
        elem.classList.remove('held')
    } else {
        elem.innerText = "HELD";
        elem.classList.add('held')
    }
};

// Makes the Die.held true or false
function holdDie() {
    if ($('#hold1')[0].classList.value.includes("held") === true) {
        die1.held = true;
    } else {die1.held = false
    }
    if ($('#hold2')[0].classList.value.includes("held") === true) {
        die2.held = true;
    } else {die2.held = false
    }
    // if (elem.id === "hold1" && elem.classList.value.includes("held")) {
    //     die1.held = true;
    // } else {
    //     die1.held = false;
    // }
    // console.log("die1 held is " + die1.held)
    // if (elem.id === "hold2" && elem.classList.value.includes("held")) {
    //     die2.held = true;
    // } else {
    //     die2.held = false;
    // }
    // console.log("die2 held is " + die2.held)
}

// ROLL
$('#roll').click( function() {
    console.log("click ROLL");
    die1.roll();
    die2.roll();
    updateImage();
    roundCheck();
    doubleAngry();

});

$('.btn--radius').click(function () {
    // if(this) {
    //
    // } else {
    var num = $(this).attr('id').slice(-1);
    if (die + num === )
    holdCheck(this)
    holdDie(this)

    // }
});

function updateImage() {
    $('#die1').find('> img').attr("src", "img/" + die1.value + ".png")
    $('#die2').find('> img').attr("src", "img/" + die2.value + ".png")
}

// strikethrough successful rounds
// check for double 3s


function roundOne() {
    if (die1.value + die2.value === round1.sum) {
        round1.complete = true
    }
}

function roundTwo() {
    if (die1.value === 4 || die2.value === 4) {
        if (die1.value === 3 || die2.value === 3) {
            round2.complete = true
        }
    }
}


function roundThree() {
    if (die1.value + die2.value === round3.sum) {
        round3.complete = true
    }
}


function roundCheck() {
    roundOne()
    roundTwo()
    roundThree()
    if (round1.complete === true) {
        $('#instructionsList').find("li")[0].style.textDecoration = "line-through";
    }
    if (round1.complete === true && round2.complete === true) {
        $('#instructionsList').find("li")[1].style.textDecoration = "line-through";
    }
    if (round2.complete === true && round3.complete === true) {
        $('#instructionsList').find("li")[2].style.textDecoration = "line-through";
        $
    }
}


function doubleAngry() {
    if (die1.value === 3 && die2.value === 3) {
        round1.complete = false;
        round2.complete = false;
        round3.complete = false;
    }
}
