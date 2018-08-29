(function test() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     console.log(this.responseText);
    } else {
        console.log(this);
    }
  };
  xhttp.open("POST", ajaxUrl, true);
  xhttp.send("vote=true&user=Sagge");
})();

