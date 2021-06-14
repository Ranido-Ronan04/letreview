
      // function showDiv (divId)
      //   {
      //     var div = document.getElementById (divId);
      //     var divs = document.getElementsByTagName('div');
      //     for (var i in divs) 
      //     {
      //       divs [i].className = "hidden";
      //     }
      //     div.className = "shown";
//       //   }
// function myFunction() {
//   var checkBox = document.getElementById("myCheck");
//   var text = document.getElementById("text");
//   if (checkBox.checked == true){
//     text.style.display = "block";
//   } else {
//      text.style.display = "none";
//   }
// }


function myProf() {
  var checkBox = document.getElementById("myProfEd");
  var text = document.getElementById("text");
  if (checkBox.checked == true){
    text.style.display = "block";
  } else {
     text.style.display = "none";
  }
}

function myGen() {
  var checkBox = document.getElementById("myGenEd");
  var text = document.getElementById("text1");
  if (checkBox.checked == true){
    text.style.display = "block";
  } else {
     text.style.display = "none";
  }
}

function myTle() {
  var checkBox = document.getElementById("myTLE");
  var text = document.getElementById("text2");
  if (checkBox.checked == true){
    text.style.display = "block";
  } else {
     text.style.display = "none";
  }
}
