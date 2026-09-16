const registerForm = document.getElementById("registerForm");
const feedbackForm = document.getElementById("feedbackForm");

let inviseCaptcha1;
let inviseCaptcha2;

function onloadFunction() {
  if (!window.smartCaptcha) {
    return;
  }
  inviseCaptcha1 = window.smartCaptcha.render("captcha-container1", {
    sitekey: "ysc1_gT1cMUmLEbVr9WqoMKPZw0NkJnbpVDt8fs3mkw8O9f8aa8bd",
    invisible: true, // Сделать капчу невидимой
    callback: callbackRegister,
    hideShield: true,
  });
  inviseCaptcha2 = window.smartCaptcha.render("captcha-container2", {
    sitekey: "ysc1_1Rmbe465Z21RaBuNsyeVkb9VjEr3mn0UEr9xvSdP2313d8ad",
    invisible: true, // Сделать капчу невидимой
    callback: callbackFeedback,
    hideShield: true,
  });
}

function callbackRegister(token) {
  registerForm.submit();
}

function callbackFeedback(token) {
  feedbackForm.submit();
}

function handleSubmit1(event) {
  event.preventDefault();
  if (!window.smartCaptcha) {
    return;
  }
  window.smartCaptcha.execute(inviseCaptcha1);
}
function handleSubmit2(event) {
  event.preventDefault();
  if (!window.smartCaptcha) {
    return;
  }
  window.smartCaptcha.execute(inviseCaptcha2);
}