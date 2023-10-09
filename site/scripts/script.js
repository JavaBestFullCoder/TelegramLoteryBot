let input = document.querySelector(".input");
let btn = document.querySelector(".generate");

btn.addEventListener("click", () => {
    input.value = getRandomInt(1000000) + 1;
});

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}