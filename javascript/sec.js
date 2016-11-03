window.onload = function () {
    //    window.setTimeout(function () {
    //        document.writeln("Testing settime out global function");
    //    }, 2000);
    //    document.writeln("How are you");
    var x = getElementById("para");
    x.onclick(function () {
        document.writeln(location.hash);
    });
    
};
