from apps.core.models import Draft

write_timer = '0:6:00'

verb = ['wilt','crumble','throb','pulse','crumple','slope','lean','huddle','tilt','sag','droop','flop','faint','queasy','dampen','loose','crust','beat','thump','thud','drum','pitter-patter','vibrate','palpitate','collapse','tumble','decay','disintegrate','flower','bud','mold','sprout','bloom','blossom','wither','gutter','woosh','bark','growl','grumble','grunt','snarl','yelp','yap','bay','howl','thunder','bawl','roar','hum','purr','crash','clang','whomp','bray','chortle','chirp','dribble','squirt','murmur','blurt','chatter','twaddle','click','clink','jingle','jiggle','waft','whisper','hiss','warble','tremble','whimper','guttural','rasp','ripple','swelter','cast','spill','hush','clatter','whir','achoo','ahem','boom','bang','bump','buzz','fizz','drip','honk','knock','moan','plop','poof','quack','rustle','sizzle','tick','tock','whimper','zoom','zip','quake','erupt','freeze','freezes','break','showers']
noun = ['breeze','gravel','summer','concrete','liquor','banana','beak','whiskey','willow','blade','grass','limb','oak','branch','tracks','pine','slough','footprint','leaf','cinnamon','smoke','lavender','vanilla','cherry','gasoline','seashell','cigarette','marrow','skin','bulb','fungus','pollen','berry','cobweb','booger','butter','moss','shedding','syrup','honey','jelly','moss','mesh','slobber','mucus','vernix','beetle','finch','yolk','birdsong','horizon','waves','seaweed','tumbleweed','snow','shell','kneecap','twig','apple','core','hills','desert','acorn','odor','nausea','musk','riverbank','canal','bay','bridge','island','meadow','river','edge','lint','boulder','bamboo','yarn','silk','marshmallow','velvet','breasts','swallow','puddle','sand','midge','mantis','vertebrae','vein','bladder','skeleton','beard','shoulders','maw','muzzle','gullet','jowl','mold','whirlwind','ladder','neptune','pillow','speaker','earth','pigeon','waif','smegma','phlegm','cliff','stupor', 'bric-a-brac']
adjective = ['moist','oceanic','merciless','mush','mushy','pulp','slush','squelchy','leather','downy','fleece','muffle','hush','balmy','tender','soothe','dense','hanging','firm','rigid','stiff','arctic','spiny','frozen','warm','cozy','sultry','toasty','melt','thaw','chilly','frost','numb','prick','crisp','sharp','warp','mix','whip','muddle','blend','whisk','rustled','fluttery','arousing','kindled','foamy','burnt','shrapnel','wooden','heliotropic','misty','hazy','murky','steamy','foggy','fuzzy','blurry','inland','dazed','swampy','penetrated','ruptured','burst','split','crack','fracture','breach','shrunken','split','shatter','achy','flattened','squish','stretched','baggy','saggy','gaseous','tart','glued','washed','gruff','deep','empty','streaked','damp','humid','brisk','dewy','dry','thick','drizzle','showered','chipped','broken','soggy','nipped','flooded','glazed','engorged','puce','chartreuse','ambrosial','bent','acrid','tangy']
compund = ["barefoot","bloodroot","prairie smoke","spider touch","exile worry","milk-heavy","daylily","dahlia-edge","wild rose","side road","car tire","road story","daisy stem","sideburns","father's shirt","mother's skirt","shaving cream","straight razor","foam-covered","young cheek","hospital bed","casket lid","teacher's desk","bathroom stall","toilet tank","final message","first call","ruthless mercy","pool's edge","lagoon beach","beer foam","massage thumbs","ugly spectacle","charming sting","handmade magic","love-soaked","simple shrine","salt flats","natural mirror","simple palace","wet secret","waterfall bottom","hotspring chaos","gueyser panic","glacial surprise","tropical solution","mountain forest","humble mountain","modest temple","profane temple","ancient skyscraper","cursed rainbow","sacred lake","holy forest","imperfect canals","exile's eye","sloppy membrane","feather cut","tar-colored","casket handle","reluctant emissary","lazy pulse","molasses-tinged","batter-colored","winter formula","spring ending","autumn beginning","unworthy offering","bullet-comforted","residual closure","diseased death","simple agony","pickled gossip","gossip heavy","fresh decay","banter-fueled","sex funk","hunter's moonlight","harvest moon","sweatshirt","sun spark","star spark","solar-born","stardeath","starbirth","foghorn","moongloom","coffin dark","emberlit","lamp glow","lamp flicker","sun patch","light rain","rainfall","warm rain","droplet","heat haze","snowfall","snowbank","snowdrift","snowflake","thunder storm","paw print","bird tracks","ant trail","dry rot","bulb rot","desert lake","canyon brush","pine cone","petal edge","hill slip","valley call","field holler","desert weeds","beach rot","toe lint","shoe lint","silk sliced","velvet angles","sand fall","wood rot","morning beam","sun glow","dim bulb"]
light = ['beacon','candlelight','firelight','floodlight','fluorescent','illumination','phosphene','shine','moonshine','moon-glow','moonshot','sunbeam','moonbeam','moonlight','Orion','mars','starlight','shimmer','sunlight','sunshine','torchlight','flickers','lamp','lamplight','darkly','gloom','sunshade','moon-shade','shady','shadow','sunset','dusk','penumbra','umbra','moon-dawn','dawn','flicker','lightning','glow','light string','sunset','radiate','moon-gleam','moon-spark','spark','glint','foggy','cloudy','luminous','flux','sparkle','twinkle','flare','flash','moon-flash','moon-bright','bright','ember','lit','moonlit','sunlit','starlit','embers','lamp-lit','streetlamp','streetlight','glitter','blaze','moon-fall','star-shine','strobe','strobe-lit','blinking','grave','diffused','moon-drip','shade','moonglade','solstice','sunny','dim','sunray','daylight','sunrise','rainy','haze','mist','smog','dew','halo','misty','overcast','kindle','kindling','torch','bonfire','beacon','fade','squint','luster','polish','sheen','moonwake',]
promptpackone = ["What sound do you trust the least?","When have you received divine intervention?","What is your heart made of?","When was your first heat?","What does it take to disgust you?","What do you do that's forbidden?","How do you bless the forbidden?","What's the farthest you've gone?","Who has the power you crave?","When were you most powerful?","What will end badly?","Who has the most tragic ending?","How do you make a happy ending?","When is there a happy ending?","What makes a great film?","Who is the star of life's film?","What is confusing about relationships?","When is a relationship over?","When has a relationship begun?","How does each relationship end?","How does each relationship begin?","What is the secret of a long relationship?","Where can you find love easy?","How do you give up love at last?","Who accepts love most graciously?","When does love require too much?","What is your greatest performance?","What can humans live without?","Who can you live without?","Where can you live without others?","Where does paranoia begin?","Where does paranoia end?","How does paranoia grow?","What must be kept close by?","Who has your closest secret?","What secret can kill you?","What secret keeps you alive?","What is the secret nobody knows?","Who is the friend who is almost finished?","What do you wish was already complete?","How do you complete what can't be finished?","What's incomplete yet perfect?","What calms you most quickly?","Who knows how to calm you?","When do you calm before the storm?","What question do you have no one has answered?","Which questions have no answers?","What can't google answer?","Who believes it was your fault?","What did you cause that no one knows?","What are your unhealthy habits?","What used to be fun but now isn't?","What is fun that used to be boring?","Who has used reckless gaffiti?","What is short and sweet?","What is short and arduous?","What do you wish would end quickly?","What do you wish you were good at?","Who is good at most things?","What causes misery?","What causes misery with hope?","Who ends misery?","When does misery begin most often?","When was the last time you lost control?","Who was the first person you gave control?","Who do you let control you?","Who do you control?","What are you in control of?","What sleeps at the back of your closet?","What is trapped in your closet?","Who has caused a feud?","When did the last feud end?","How did your worst feud begin?","What is impossible to measure?","What was your last misunderstanding?","When did your misunderstanding end?","Who do you misunderstand the most?","What were you wrong about?","What was the last thing you were wrong about?","Who was last wrong about you?","What is better in Europe?","What is stranger than fiction?","Who is stranger than fiction?","When did the world end?","Who will cause the world to end?","When will the world end?","How will the world end gloriously?","What was last year made of?","How many regrets are in a year?","When will last year's regrets pass over?","What have you gotten away with?","What do you wish would last forever?","Who would you spend eternity with?","When is it most crowded?","Where do you find the largest crowds?","Who do you notice in the crowd?","What rules are okay to break?","How will you end this night?","What is every night made of?","When does the night begin?"]
promptpacktwo = ["What do dogs dream of?","What are a cat's deepest desires?","Who would you like to have dinner with?","What makes you famous?","What makes you infamous?","What are you the patron saint of?","What do you rehearse?","How do you rehearse for the spontaneous?","How do you rehearse for everyday life?","What is your perfect day made of?","What is the last song you sang?","What is the last song someone sang to you?","How does the mind show its age?","How will you die?","When will you die?","How were you born?","What were your parents' lives like before you?","What do you share with the last person you saw?","Who are you most grateful for?","What is the source of your deepest gratitude?","What would you change about how you were raised?","When does your life story begin?","Who would be the best author of your life story?","Whose life story would you like to read?","What would you wake up and change tomorrow?","What questions would you ask a crystal ball?","Who reminds you of your future self?","Why haven't you reached your greatest dream?","What is the greatest accomplishment of your life?","Who have you let down?","Who have you not talked to in a long time?","Who do you miss having in your life?","How do you show friendship?","Who is your most valued friend?","When did your first friendship begin?","When did your last friendship end?","How did your last friendship end?","How will your next friendship begin?","What is your favorite memory?","Who shares your favorite memory with you?","When did you forget the details of your childhood?","What is your worst memory?","Who shares your worst memory?","How did your worst memory begin?","How did your worst memory end?","Who would you share your last day with?","How would you spend your last day?","Where is love in your life?","How is love a part of your life?","When did love last enter your life?","What are your most positive characteristics?","Who do you admire the most?","How was your childhood different?","How was your childhood the same?","How is your relationship with your mother?","What's a memory you share with your mother?","How is your relationship with your father?","What's a memory you share with your father?","What sounds do you currently hear?","What smells do you currently smell?","What can't you see behind you?","Who made the last thing you touched?","Where did the last thing you touched come from?","Where would you like to visit most?","What would you like to share that you don't?","Who would you like to share your life with?","What are important things to know about you?","Where do you come from?","Where does your father come from?","Where does your mother come from?","What happened the day your mom was born?","What happened the day your dad was born?","What wouldn't you share with someone you just met?","What was the last embarassing thing you saw?","How do you deal with embarassment?","When was the last time you were embarassed?","When was the last time you cried?","Who was the last person you cried in front of?","What was the thing that made you cry the most?","What is too serious to be joked about?","What was the last joke you told?","When was the last time you laughed?","What's the funniest thing you've seen?","How can someone make you laugh?","What are you holding back saying to someone?","What would you save from a fire?","Whose death would you find most upsetting?","What death has upset you the most?","When was your first experience with death?","How did you first understand death?","What is your most frequent problem?","What's your most recent problem?","What do you do that you don't like?","What do you celebrate?","What was the last thing you tripped over?","What is your favorite technology?","What are your bad habits?","What are your good habits?","How would you quit your bad habits?","How can you begin with a kiss?"]
promptpackthree = ["What would you choose as a last meal?","What would you never ask advice about?","What's your most unfair experience?","What do you no longer believe in?","What is the last smell you remember?","What attempts to be a tree in the wind?","Who has been dead much longer than alive?","What inanimate object waits?","What is the color of your last kiss?","How do you introduce a kiss?","What's your most worn out memory?","How can you tell a lie and swaddle truth?","When have you collaborated with death?","Who has revealed truth as an old lie?","Who worships at the temple of your body?","When does death carry you?","Where do you feel the most delight?","What has been dark and worked inside you?","When have you laughed until you forgot?","When have your eyes wanted to be hands?","When have you erased impossibility?","When did your ears learn no?","When was the last time you were told no?","When have you been an entrance?","Who do you know that is an entrance?","How does a rosebud feel before it blooms?","Who do you know who is an event?","What can you end that's endless?","When does a god yawn?","What have you misheard through static?","What propriety would you put in a trash can?","What are your most incorrect theories?","What would happen if you called an ex’s phone?","How can you translate your last physical experience?","What have you said that you immediately regret?","When has your desire become another person?","When have you been wrong but love wasn’t?","What is your history of bad choices?","What do you love that's fatal?","What do we all carry?","When is a puddle a mirror for the stars?","Who was the last person you saw in street light?","What does it mean to fear a woman?","What does it mean to fear a man?","Who knows your tongue better than you?","How can you repeat a cruel line after a kind?","How can you repeat one shape throughout?","What is full of hum and buzz and emptiness?","What is the last name you said out loud?","When has a stranger’s glance been an invitation?","How can the flesh echo?","What's the best way to learn a language?","How can you make lust holy?","What was the last experiment you conducted?","What have you forgiven yourself for?","Who has stirred gasps in distant rooms?","What’s most beautiful at dawn?","When is the last time you suffered?","When is life a duty?","What's important but too far to grasp?","What is on the edge of a sexual encounter?","What is your favorite city you weren’t born in?","What is the best place for orgasms?","What misheard lyrics do you still sing?","What sacred space do you put a mouth on?","What birdsong do you recognize?","What common object do you see as extraordinary?","How can you repeat a phrase throughout?","What do you do with an obnoxious word?","When do you worry about beauty?","How do you admit your indignity?","What is the sum of our lives?","Where is the strangest place for a reflection?","What can't be doubted?","What sounds have a body?","What is the source of your last mistake?","What are two things you always keep?","How can you explain the weather with gods?","When is the last time you were ashamed?","When is the last time you avoided eye contact?","How can you reveal the history of language?","When do you notice small flaws in large spaces?","Who would love you if you became a vampire?","Who is the most tender monster?","What's just outside the window?","Who will never love you?","What is the last thing you imagined?","How could your life be easier?","How can you translate birdsong?","What do you find funny that no else does?","What has been stolen from you?","What have you ever stolen?","What do you find most strange?","Where do you keep broken promises?","Who was the last person that yelled at you?","What was your last argument about?","Who was the last person you yelled at?","When was the last time you meddled?","What was the first promise?","What was the last thing you lost?"]
promptpackfour = ["What memory has your favorite smell?", "What do you know about your ancestors?", "What would your ancestors be proud of?", "What would your ancestors be ashamed of?", "Who are your ancestors?", "When was someone kind to you?", "When did you accomplish something wonderful?", "Where do you feel like home?", "How do you build a home?", "When have you experienced great joy?", "When have you learned something difficult?", "When was the last time you were courageous?", "Who has done something courageous for you?", "What does faith mean to you?", "Who taught you about faith?", "Where would you like to live and why?", "What type of place do you come from?", "What lifestyle exists in your dreams?", "What is the last dream you remember?", "What is a nightmare you've woken up from?", "When was the last time you felt happy?", "When was the last time you felt sad?", "How does someone convince you they love you?", "How do you show someone you love them?", "What are you grateful for today?", "What do you appreciate about yourself?", "What is your family story?", "What would you like to contribute to the world?", "What will you never forget?", "What community are you a part of?", "What was a childhood challenge you experienced?", "When have you been mistreated?", "When has your family caused you stress?", "When has your family brought you joy?", "When was the last time you felt lonely?", "What is the difference between being alone and lonely?", "When has your life felt abundant?", "What do you fear in the future?", "When have you been culture shocked?", "How have you felt marginalized?", "What is your last regret?", "When have you been rejected?", "What is a difficult journey you've traveled?", "What fear is holding you back?", "What do others misunderstand about you?", "What is an injustice you notice?", "Who have you mistreated?", "When do you feel you've failed?", "What trip has changed you?", "What is a secret no one knows?"]


def get_blanklist():
	blanklist = ['hush', 'gullet', 'streaked', 'rigid', 'wilt', 'tock', 'vernix', 'slobber',
		'grumble', 'growl', 'fungus', 'damp', 'mushy', 'dry', 'whirlwind', 'shatter', 'hush',
		'starlight', 'cigarette', 'engorged', 'bright', 'yap', 'prick', 'pulp', 'moonlight',
		'vanilla', 'plop', 'lavendar', 'soothe', 'mush', 'dry', 'sunlight', 'downy', 'cliff',
		'zoom', 'warble', 'jowl', 'riverbank', 'whimper', 'dampen', 'vertebrae', 'shine', 'twaddle',
		'squint', 'dazed', 'maw', 'shrapnel', 'sunshine', 'moss', 'boulder', 'deep', 'mesh', 'sunshade', 'bridge',
		'kindling', 'crashed', 'sizzle', 'muffle', 'vibrate', 'solstice', 'thud', 'fluttery', 'beetle', 'puce',
		'empty', 'shrunken', 'pitter-patter', 'soggy', 'snarl', 'blade']
	return blanklist


def get_drafts():
    alldrafts = Draft.objects.order_by('-revised')
    userdrafts = alldrafts.filter(user=user)
    userdrafts = [userdrafts]


def get_dict():
    fulldict = verb + noun + adjective + light
    return fulldict


def get_prompts():
    allprompts = promptpackone + promptpacktwo + promptpackthree + promptpackfour
    return allprompts


def get_next_fromq():
    alldrafts = Draft.objects.order_by('revised')
    queuedrafts = alldrafts.filter(in_queue=True)
    queuedrafts = queuedrafts.exclude(user=request.user)
    queuedrafts = [queuedrafts]

    return queuedrafts
