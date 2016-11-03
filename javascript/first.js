
onLoad () {
    var x = "Hello World";

    function foo () {
        var x = "Gaurav Sood";
    }
    
    foo();

    document.writeln(x);

var y = new Date();
document.writeln(y.toString());
document.writeln(Object.getPrototypeOf(y));

// Closures
function foo () {
    var x = 25;
    function bar () {
        return x + 25;
    }
    return bar;
}

document.writeln(foo()());
document.writeln(typeof "ga");


function typeAndValue (x) {
    if (x == null) return "";
    switch(x.constructor) {
    case Number: return "Number: " + x;
    case String: return "String: '" + x + "'";
    }
};

// document.writeln(typeAndValue(5));
// document.writeln(y.constructor === Date);

// alert("OK");
// location = "http://www.google.com";
