const feedbackForm = document.getElementById("feedbackForm");

let inviseCaptcha;

function onloadFunction() {
  if (!window.smartCaptcha) {
    return;
  }
  inviseCaptcha = window.smartCaptcha.render("captcha-container", {
        sitekey: "ysc1_zjj8knueYqVEyOmcg83p3NSgTSr7seEEM4s5PxU0eeb57007",
        invisible: true, // Сделать капчу невидимой
        callback: callback,
        hideShield: true,
    });
}

function callback(token) {
  feedbackForm.submit();
}

function handleSubmit(event) {
  event.preventDefault();
  if (!window.smartCaptcha) {
    return;
  }
  window.smartCaptcha.execute(inviseCaptcha);
}