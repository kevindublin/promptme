let nouns = ['breeze', 'gravel', 'summer', 'concrete', 'liquor', 'banana', 'beak', 'whiskey', 'willow', 'blade', 'grass', 'limb', 'oak', 'branch', 'tracks', 'pine', 'slough', 'footprint', 'leaf', 'cinnamon', 'smoke', 'lavender', 'vanilla', 'cherry', 'gasoline', 'seashell', 'cigarette', 'marrow', 'skin', 'bulb', 'fungus', 'pollen', 'berry', 'cobweb', 'booger', 'butter', 'moss', 'shedding', 'eye jelly', 'syrup', 'honey', 'jelly', 'moss', 'mesh', 'slobber', 'mucus', 'vernix', 'beetle', 'finch', 'yolk', 'birdsong', 'horizon', 'waves', 'seaweed', 'tumbleweed', 'snow', 'shell', 'kneecap', 'twig', 'apple', 'core', 'hills', 'desert', 'acorn', 'odor', 'nausea', 'musk', 'riverbank', 'canal', 'bay', 'bridge', 'island', 'meadow', 'river', 'edge', 'lint', 'boulder', 'bamboo', 'yarn', 'silk', 'marshmallow', 'velvet', 'breasts', 'swallow', 'puddle', 'sand', 'bric-a-brac', 'midge', 'mantis', 'vertebrae', 'vein', 'bladder', 'skeleton', 'beard', 'shoulders', 'maw', 'muzzle', 'gullet', 'jowl', 'mold', 'whirlwind', 'ladder', 'neptune', 'pillow', 'speaker', 'earth', 'pigeon', 'waif', 'smegma', 'phlegm', 'cliff', 'stupor'];
let adjectives = ['moist', 'oceanic', 'merciless', 'mush', 'mushy', 'pulp', 'slush', 'squelchy', 'leather', 'downy', 'fleece', 'muffle', 'hush', 'balmy', 'tender', 'soothe', 'dense', 'hanging', 'firm', 'rigid', 'stiff', 'arctic', 'spiny', 'frozen', 'warm', 'cozy', 'sultry', 'toasty', 'melt', 'thaw', 'chilly', 'frost', 'numb', 'prick', 'crisp', 'sharp', 'warp', 'mix', 'whip', 'muddle', 'blend', 'whisk', 'rustled', 'fluttery', 'arousing', 'kindled', 'foamy', 'burnt', 'shrapnel', 'wooden', 'heliotropic', 'misty', 'hazy', 'murky', 'steamy', 'foggy', 'fuzzy', 'blurry', 'inland', 'dazed', 'swampy', 'penetrated', 'ruptured', 'burst', 'split', 'crack', 'fracture', 'breach', 'shrunken', 'split', 'shatter', 'achy', 'flattened', 'squish', 'stretched', 'baggy', 'saggy', 'gaseous', 'tart', 'glued', 'washed', 'gruff', 'deep', 'empty', 'streaked', 'damp', 'humid', 'brisk', 'dewy', 'dry', 'thick', 'drizzle', 'showered', 'chipped', 'broken', 'soggy', 'nipped', 'flooded', 'glazed', 'engorged', 'puce', 'chartreuse', 'ambrosial', 'bent', 'acrid', 'tangy'];
let verbs = ['wilt', 'crumble', 'throb', 'pulse', 'crumple', 'slope', 'lean', 'huddle', 'tilt', 'sag', 'droop', 'flop', 'faint', 'queasy', 'dampen', 'loose', 'crust', 'beat', 'thump', 'thud', 'drum', 'pitter-patter', 'vibrate', 'palpitate', 'collapse', 'tumble', 'decay', 'disintegrate', 'flower', 'bud', 'mold', 'sprout', 'bloom', 'blossom', 'wither', 'gutter', 'woosh', 'bark', 'growl', 'grumble', 'grunt', 'snarl', 'yelp', 'yap', 'bay', 'howl', 'thunder', 'bawl', 'roar', 'hum', 'purr', 'crash', 'clang', 'whomp', 'bray', 'chortle', 'chirp', 'dribble', 'squirt', 'murmur', 'blurt', 'chatter', 'twaddle', 'click', 'clink', 'jingle', 'jiggle', 'waft', 'whisper', 'hiss', 'warble', 'tremble', 'whimper', 'guttural', 'rasp', 'ripple', 'swelter', 'cast', 'spill', 'hush', 'clatter', 'whir', 'achoo', 'ahem', 'boom', 'bang', 'bump', 'buzz', 'fizz', 'drip', 'honk', 'knock', 'moan', 'plop', 'poof', 'quack', 'rustle', 'sizzle', 'tick', 'tock', 'whimper', 'zoom', 'zip', 'quake', 'erupt', 'freeze', 'freezes', 'break', 'showers'];
let lightWords = ['beacon', 'candlelight', 'firelight', 'floodlight', 'fluorescent', 'illumination', 'phosphene', 'shine', 'moonshine', 'moon-glow', 'moonshot', 'sunbeam', 'moonbeam', 'moonlight', 'Orion', 'mars', 'starlight', 'shimmer', 'sunlight', 'sunshine', 'torchlight', 'flickers', 'lamp', 'lamplight', 'darkly', 'gloom', 'sunshade', 'moon-shade', 'shady', 'shadow', 'sunset', 'dusk', 'penumbra', 'umbra', 'moon-dawn', 'dawn', 'flicker', 'lightning', 'glow', 'light string', 'sunset', 'radiate', 'moon-gleam', 'moon-spark', 'spark', 'glint', 'foggy', 'cloudy', 'luminous', 'flux', 'sparkle', 'twinkle', 'flare', 'flash', 'moon-flash', 'moon-bright', 'bright', 'ember', 'lit', 'moonlit', 'sunlit', 'starlit', 'embers', 'lamp-lit', 'streetlamp', 'streetlight', 'glitter', 'blaze', 'moon-fall', 'star-shine', 'strobe', 'strobe-lit', 'blinking', 'grave', 'diffused', 'moon-drip', 'shade', 'moonglade', 'solstice', 'sunny', 'dim', 'sunray', 'daylight', 'sunrise', 'rainy', 'haze', 'mist', 'smog', 'dew', 'halo', 'misty', 'overcast', 'kindle', 'kindling', 'torch', 'bonfire', 'beacon', 'fade', 'squint', 'luster', 'polish', 'sheen', 'moonwake']; 
let compounds = ["barefoot", "bloodroot", "prairie smoke", "spider touch", "exile worry", "milk-heavy", "daylily", "dahlia-edge", "wild rose", "side road", "car tire", "road story", "daisy stem", "sideburns", "father's shirt", "mother's skirt", "shaving cream", "straight razor", "foam-covered", "young cheek", "hospital bed", "casket lid", "teacher's desk", "bathroom stall", "toilet tank", "final message", "first call", "ruthless mercy", "pool's edge", "lagoon beach", "beer foam", "massage thumbs", "ugly spectacle", "charming sting", "handmade magic", "love-soaked", "simple shrine", "salt flats", "natural mirror", "simple palace", "wet secret", "waterfall bottom", "hotspring chaos", "gueyser panic", "glacial surprise", "tropical solution", "mountain forest", "humble mountain", "modest temple", "profane temple", "ancient skyscraper", "cursed rainbow", "sacred lake", "holy forest", "imperfect canals", "exile's eye", "sloppy membrane", "feather cut", "tar-colored", "casket handle", "reluctant emissary", "lazy pulse", "molasses-tinged", "batter-colored", "winter formula", "spring ending", "autumn beginning", "unworthy offering", "bullet-comforted", "residual closure", "diseased death", "simple agony", "pickled gossip", "gossip heavy", "fresh decay", "banter-fueled", "sex funk", "hunter's moonlight", "harvest moon", "sweatshirt", "sun spark", "star spark", "solar-born", "stardeath", "starbirth", "foghorn", "moongloom", "coffin dark", "emberlit", "lamp glow", "lamp flicker", "sun patch", "light rain", "rainfall", "warm rain", "droplet", "heat haze", "snowfall", "snowbank", "snowdrift", "snowflake", "thunder storm", "paw print", "bird tracks", "ant trail", "dry rot", "bulb rot", "desert lake", "canyon brush", "pine cone", "petal edge", "hill slip", "valley call", "field holler", "desert weeds", "beach rot", "toe lint", "shoe lint", "silk sliced", "velvet angles", "sand fall", "wood rot", "morning beam", "sun glow", "dim bulb"];
let i = randInt()
let rand = randInt(i)


function randInt() {
 
 	let max = 103;
  	let i = Math.round(Math.random() * max);
  return i

}


// 6 minutes from now
let time_in_minutes = 6;
let current_time = Date.parse(new Date());
let deadline = new Date(current_time + time_in_minutes*60*1000);
let dripBank = document.getElementById("drips");

wordOne = nouns[rand];
wordTwo = adjectives[rand];
wordThree = verbs[rand];
wordFour = lightWords[rand];
wordFive = compounds[rand];


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
