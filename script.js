const DB_HOST = window.location.href.startsWith("http://localhost")
  ? "http://localhost:5000"
  : "https://ratemybark1.herokuapp.com";

function choose(items) {
  return items[Math.floor(Math.random() * items.length)];
}

function visit(data) {
  const xhr = new XMLHttpRequest();
  xhr.open("POST", `${DB_HOST}/visit`, true);
  xhr.send(data);
}

visit();

function vote(data) {
  const xhr = new XMLHttpRequest();
  xhr.open("POST", `${DB_HOST}/vote`, true);
  xhr.send(data);
  window.location.reload();
}

function fromHtml(html) {
  const div = document.createElement("div");
  div.innerHTML = html;
  return div.children[0];
}

function get2Barks() {
  let a, b;
  do {
    a = choose(barks);
    b = choose(barks);
  } while (a == b);

  return [a, b];
}
let log = console.log;

function setupButton(button, file) {
  const audio = button.querySelector("audio");
  audio.appendChild(fromHtml(`<source src="barks/${file}" type="audio/wav">`));

  // Add dog highlight
  let dogDiv = button.querySelector(".dog-image");
  dogDiv.children[0].addEventListener("mouseenter", () => {
    dogDiv.children[1].hidden = false;
    dogDiv.children[0].hidden = true;
  });
  dogDiv.children[1].addEventListener("mouseleave", () => {
    dogDiv.children[0].hidden = false;
    dogDiv.children[1].hidden = true;
  });

  // Play audio when dog is clicked
  dogDiv.children[0].addEventListener("mouseup", () => {
    audio.play();
  });
  dogDiv.children[1].addEventListener("mouseup", () => {
    audio.play();
  });

  button.querySelector(".vote").addEventListener("click", () => {
    console.log(`Voting for ${file}`);
    vote(file);
  });
}

document.addEventListener("DOMContentLoaded", () => {
  let a, b;
  [a, b] = get2Barks();
  setupButton(document.getElementById("a"), a);
  setupButton(document.getElementById("b"), b);
});
