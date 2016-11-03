$( function () {
    document.writeln("hey") ;
    window.setTimeout(function () {
        document.writeln("Testing settime out global function");
    }, 2000);
});
