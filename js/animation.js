function getRndInteger(min, max) {
      return Math.floor(Math.random() * (max - min) ) + min;
    }

function piss(stink) {
  var x = document.getElementById(stink);
  if (x.style.display == "none") {
    x.style.display = "block";
    let id = null;
    const elem = document.getElementById(stink);
    var rand = getRndInteger(0,300);
    let pos = getRndInteger(0,300);
    elem.style.top = pos + 'px';
    elem.style.left = pos + 'px';
  } else {
    x.style.display = "none";
  }
} 

//clearInterval(id);
  //  id = setInterval(frame, 5);
    //function frame() {
      //if (pos == 350) {
        //clearInterval(id);
      //} else {
        //pos++;