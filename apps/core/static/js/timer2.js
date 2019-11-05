
// 6 minutes from now
let time_in_minutes = 6;
let current_time = Date.parse(new Date());
let deadline = new Date(current_time + time_in_minutes*60*1000);
let dripBank = document.getElementById("drips");
wordOne = "pulse";
wordTwo = "misty";
wordThree = "blossom";
wordFour = "residual";
wordFive = "lamp flicker";

function time_remaining(endtime){
	let t = Date.parse(endtime) - Date.parse(new Date());
	let seconds = Math.floor( (t/1000) % 60 );
	let minutes = Math.floor( (t/1000/60) % 60 );
	let hours = Math.floor( (t/(1000*60*60)) % 24 );
	let days = Math.floor( t/(1000*60*60*24) );
	return {'total':t, 'days':days, 'hours':hours, 'minutes':minutes, 'seconds':seconds};
}

let timeinterval;
function run_clock(id,endtime){
	let clock = document.getElementById(id);
	function update_clock(){
		let t = time_remaining(endtime);
		t.minutes = t.minutes < 10 ? "0" + t.minutes : t.minutes;
    t.seconds = t.seconds < 10 ? "0" + t.seconds : t.seconds;
		clock.innerHTML = t.minutes + ":" + t.seconds;
		if(t.total<=0){ clearInterval(timeinterval);
			tinymce.activeEditor.setMode('readonly');
		}

		if(t.minutes==5 && t.seconds==0){ dripBank.textContent += "| " + wordOne; }

		if(t.minutes==4 && t.seconds==0){ dripBank.textContent += " | " + wordTwo; }

		if(t.minutes==3 && t.seconds==0){ dripBank.textContent += " | " + wordThree; }

		if(t.minutes==2 && t.seconds==0){ dripBank.textContent += " | " + wordFour; }

		if(t.minutes==1 && t.seconds==0){ dripBank.textContent += " | " + wordFive + " |"; }

	}
	update_clock(); // run function once at first to avoid delay
	timeinterval = setInterval(update_clock,1000);
}
run_clock('timer',deadline);


let paused = false; // is the clock paused?
let time_left; // time left on the clock when paused

function pause_clock(){
	if(!paused){
		paused = true;
		//disable editor on pause
		tinymce.activeEditor.setMode('readonly');

		clearInterval(timeinterval); // stop the clock
		time_left = time_remaining(deadline).total; // preserve remaining time
	}
}

function resume_clock(){
	if(paused){
		paused = false;
		//activate editor on resume
		tinymce.activeEditor.setMode('design');
		// update the deadline to preserve the amount of time remaining
		deadline = new Date(Date.parse(new Date()) + time_left);

		// start the clock
		run_clock('timer',deadline);
	}
}

// handle pause and resume button clicks
document.getElementById('pause').onclick = pause_clock;
document.getElementById('resume').onclick = resume_clock;
