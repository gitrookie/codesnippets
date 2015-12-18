var my_var = "hello world!"
var my_object = { "first name": "Gaurav",
                  "last name": "Sood",
                  "toString": function () { return "Gaurav Sood"; }
                };
document.writeln(my_var.toUpperCase())
document.writeln(my_object["first name"])



var person = Object.create(null);
Object.defineProperty(person, 'firstName', {
    value: "Yehuda",
    writable: true,
    enumerable: true,
    configurable: true
});
// document.writeln(Object.getPrototypeOf(my_object));
// document.writeln(person.toString());
document.writeln(my_object.toString());

var add = function (a, b) {
    return a + b;
 }
document.writeln(add(2, 3))
document.writeln(my_object.hasOwnProperty("toString"))


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
