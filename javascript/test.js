var myob = { "a": 1,
             "b": undefined,
             "c": function () {
               return "Hello World!"
             },
             "toString": function () {
               return "myob";
             }
}

var func = function () {
  return "hey";
}


//myob.delete("a");

for (prop in myob) {
  document.writeln(prop);
}

var ob2 = Object.create(myob);
delete ob2.a;
for (prop in document) {
  document.writeln(prop);
}

this.alert("This is the first dialog");
document.writeln(document.getElementsbyName("body"));