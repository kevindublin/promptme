function startTimer(duration, display) {
    let timer = duration, minutes, seconds;
    setInterval(function () {
        minutes = parseInt(timer / 60, 10)
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
        	$("#draftForm :input").prop('readonly', true);
            timer = 0;
        }
    }, 1000);
}

window.onload = function () {
    let writeTimer = 60 * 6,
        display = document.querySelector('#timer');
    startTimer(writeTimer, display);
};
