const box = document.getElementById("box");
const box2 = document.getElementById("box2");
const box3 = document.getElementById("box3");
const box4 = document.getElementById("box3");

box.addEventListener("mouseover", function handleMouseOver() {
  box.style.color = "green";
});

box.addEventListener("mouseout", function handleMouseOver() {
  box.style.color = "black";
});

box2.addEventListener("mouseover", function handleMouseOver() {
  box2.style.color = "red";
});

box2.addEventListener("mouseout", function handleMouseOver() {
  box2.style.color = "black";
});


