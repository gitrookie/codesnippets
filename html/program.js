/*global   */
/*
var ps = $("p");
document.writeln(ps.length);
for (prop in ps) {
  document.writeln(prop)
}
ps.css("background-color", "pink");
ps.click(function () {
  $(this).slideUp("slow")
});
*/

// document.writeln(f)
$(function () {
var f = $(".first p").css("background-color", "pink");
var divs = $("div");
/*  divs.click (function () {
  $("p", this).slideUp("slow");
});*/
/*$("div").each(function() {
  $("p", this).css("background-color", "pink");
});*/
/*$("div").each(function(idx, doc) {
  $(doc).prepend(idx + ":: ");
  if (doc.id == "last") return false;
});*/
// divs.css("background-color", "red");
divs.click (function (){
  //$("p", this).css("background-color", "red").slideUp("slow");
  if ($("p", this).css("background-color") == "green") {
    //$("p", this).css("background-color", "red");
    document.writeln("Hello");
  }
})

});