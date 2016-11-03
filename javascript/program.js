var my_var = "hello world!";
var my_object = { "first name": "Gaurav",
                  "last name": "Sood",
                  "toString": function () { return "Gaurav Sood"; }
                };
//document.writeln(my_var.toUpperCase())
//document.writeln(my_object["first name"])



var person = Object.create(null);
Object.defineProperty(person, 'firstName', {
    value: "Yehuda",
    writable: true,
    enumerable: true,
    configurable: true
});

person.toString = function () {
  return person.firstName;
};
//document.writeln(Object.getPrototypeOf(my_object));
//document.writeln(person.toString());
// document.writeln(my_object.toString());

var add = function (a, b) {
    return a + b;
};
// document.writeln(add(2, 3));
// document.writeln(my_object.hasOwnProperty("toString"));

/*
var Person = function (firstname, lastname) {
    this.firstname = firstname;
    this.lastname = lastname;
}


Person.prototype = {
    toString: function () { return this.firstname + ' ' + this.lastname; }
}

var newObject = function (func) {
    var args = Array.prototype.slice.call(arguments, 1);
    var ob = Object.create(func.prototype);
    func.apply(ob, args);
    return ob;
}

// var per = newObject(Person, "Gaurav", "Sood");
var per = new Person("Gaurav", "Sood")
document.writeln(per.toString());
 */

function foo () {
    return "This is function";
}

var o1 = Object.create({x:1, y:2});
// document.writeln(Object.prototype.isProtoypeOf(o1));
var x = 2;
var y = 3;
var o2 = o1;
var o3 = {x:1, y:2};
document.writeln("<p>Testing Operators in Javascript</p>");
//document.writeln("<br>");
document.writeln(1 === '1');
//document.writeln("<br>");
document.writeln("<p>Testing Objects which are not primitives</p>");
//document.writeln("<br>");
document.writeln(o1 == o2);
document.writeln("<br>");
document.writeln(typeof new Function());
document.writeln("<br>");
document.writeln("Constructors in JavaScript");
function Book (title, author, year) {
    this.title = title;
    this.author = author;
    this.year = year;
}

Book.prototype = {
    computer: "yes"
};

var book = new Book("JavsScript the good parts", "Gaurav Sood", 2015);
document.writeln(book.title);
document.writeln(Book.prototype.isPrototypeOf(book));
document.writeln(book.computer);
document.writeln("<br>");
document.writeln("Range Constructor in JavaScript");


function Range(from, to) {
    this.from = from;
    this.to = to;
};

// It overwrites the predefined prototype property so now Range.prototype
// no longer has constructor as its property
Range.prototype = {
    includes: function(x) { return this.from <= x && x <= this.to; },

    foreach: function(f) {
        for(var x = Math.ceil(this.from); x <= this.to; x++) f(x);
    },

    toString: function() { return "(" + this.from + "..." + this.to + ")"; },
    constructor: Range
};

var r = new Range(1, 3);
for (prop in r) {
    document.writeln(prop);
}
document.writeln(r.constructor === Range);

document.writeln("<p>Complex Number Class in JavaScript</p>");

function Complex(real, img) {

    if (isNaN(real) || isNaN(img)) {
        throw TypeError("Not a Number");
    };

    this.real = real;
    this.img = img;
};

Complex.prototype.add = function (that) {
    return new Complex(this.real + that.real, that.img + this.img);
};

Complex.prototype.toString = function() {
    return this.real.toString() + " +" + " i" + this.img.toString();
};

var c = new Complex(2, 4);
var d = new Complex(4, 6);
document.writeln(c instanceof Object);

