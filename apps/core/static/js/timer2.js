
// 6 minutes from now
let time_in_minutes = 6;
let current_time = Date.parse(new Date());
let deadline = new Date(current_time + time_in_minutes*60*1000);


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
		clock.innerHTML = 'minutes: '+t.minutes+'<br>seconds: '+t.seconds;
		if(t.total<=0){ clearInterval(timeinterval); }
	}
	update_clock(); // run function once at first to avoid delay
	timeinterval = setInterval(update_clock,1000);
}
run_clock('clockdiv',deadline);


let paused = false; // is the clock paused?
let time_left; // time left on the clock when paused

function pause_clock(){
	if(!paused){
		paused = true;
		clearInterval(timeinterval); // stop the clock
		time_left = time_remaining(deadline).total; // preserve remaining time
	}
}

function resume_clock(){
	if(paused){
		paused = false;

		// update the deadline to preserve the amount of time remaining
		deadline = new Date(Date.parse(new Date()) + time_left);

		// start the clock
		run_clock('clockdiv',deadline);
	}
}

// handle pause and resume button clicks
document.getElementById('pause').onclick = pause_clock;
document.getElementById('resume').onclick = resume_clock;

