function full_screen(el) {
  if (el.classList.contains("fullscreen")) {
    el.classList.remove("fullscreen");
    let blackout = document.getElementById("blackout");
    if (blackout) blackout.remove();
  } else {
    el.classList.add("fullscreen");
    let blackout = document.createElement("div");
    blackout.id = "blackout";
    blackout.addEventListener("click", () => full_screen(el));
    document.body.append(blackout);
  }
}

let fullscreenables = Array.from(document.querySelectorAll(".fullscreenable"));

for (let el of fullscreenables) {
  el.addEventListener("click", () => full_screen(el));
}
