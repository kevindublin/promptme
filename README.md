# Prompt Me
*a web service to spark creative writing & community. Currently testing the MVP. Many features left to add.*

![logo](https://raw.githubusercontent.com/kevindublin/promptme/master/apps/core/static/images/logo.png "logo")

## Current Status:

Planning to refactor the code for the micro-education writing web suite **Dailies**. Installing Django REST Framework in order to setup Prompt Me as an API with endpoints for prompts, images, drafts, etc to be consumed by a single page app built with React that will allow greater interactivity in the Feedback Queue such as favorite word highlighting, in the drafting process such as seeing the definitions of words in the drip bank, smoother animations for the words being served outside of animate.css, and more. Continuing work slowly, likely not picking up speed again until Summer 2020.


## Known Issues:

- ~~Home page slider and contents break styling on maximum Retina and widescreen displays~~
- ~~Mobile view of Feedback Queue has uneven rows~~
- ~~Bottom dock in mobile view is off-center~~
- ~~Add password reset functionality~~
- ~~Private prompts will show up in collab feed if there are no other user prompts created~~
- Unlimited voting, will eventually change to each user getting a certain amount based on their tier
- ~~View Feedback shows all feedback for a user on each individual draft~~
- ~~Mobile Write view TinyMCE auto switches to full screen and can't see drip words~~
- ~~Write View collapses and hides drip bank if not filled when window forces min width~~
- ~~Image and prompt will occasionally change when write is pressed~~
- ~~Feedback Queue view crashes when queue is empty~~

![prompt](https://raw.githubusercontent.com/kevindublin/promptme/master/apps/core/static/images/home_promptme.png "prompted")

![write](https://raw.githubusercontent.com/kevindublin/promptme/master/apps/core/static/images/home_write.png "written")

![dashboard](https://raw.githubusercontent.com/kevindublin/promptme/master/apps/core/static/images/home_dashboard.png "edited")


## Features to Add:

**Individual Features**
- ~~Social Login~~
- Feedback dashboard
- Context dictionary: hover over words to show the definition
- Add pie charts for feedback results, analytics
- Third app with Full TinyMCE in-browser text editor to work on drafts
- Export writing to Google Drive and Dropbox
- Take photos of handwritten or printed text and OCR into editor as a draft for those who prefer to write by hand, uploadcare

**Community Features**
- ~~Post public prompts~~
- ~~Create feed for public prompts~~
- Add private messaging & inbox
- Follow User Feature (collaborators)
- Join a writing group and make your work visible to that group in a private queue
- Exquisite Corpse, Renga, Call & Response games

**Membership and Subscription Features**
- ~~Membership model~~
- Membership Tiers tied to account
- Pay Portal, accept payments through PayPal
- Number of queue calls, prompts, & drafts written tied to membership tier

**Writing Career Features**
- Submission Tracker via Submittable API
- Open calls for submissions
- User posted Calls for submissions
- Web scraper which pulls submission calls from all over the web and prompt me calls that API

## Setting up a Local Development Environment:

First you'll want to go to the upper right hand corner of the repository and click the green button that says "Clone or download" and select "Download ZIP" from the dropdown.

Once the zip file is downloaded, extract it and enter the "promptme" folder.

A few tasks to setup the environment. You'll likely want to use Linux. MacOS should work as well.

Now let's enter the terminal to install everything. Make sure you're in the folder with the "manage.py" file. Once there, context click and select "Open Terminal," then type the following commands:

- Type "python --version" and "python3 --version" and you should see 2.X.X and 3.X.X respectively to make sure python3 is installed. If not, then type sudo apt-get install python3" and enter your password when prompted.
- Type "pip --version" to make sure python package manager pip is installed. If that returns nothing, then try "pip3 --version" and if is says that pip isn't installed, then "sudo apt-get install python3-pip" will install it.
- Type "pip3 install --user pipenv" to make sure pipenv virtual environment is installed.

Now a few items to run locally.

Enter a virtual environment and install required packages in the root directory of the project:

- *pipenv shell*
- *pipenv install* to install remaining project packages

Now you're ready to make migrations and boot the server.

- *python manage.py makemigrations*
- *python manage.py migrate*
- *python manage.py collecstatic*
- *python manage.py runserver*

You should see something like:

***

System check identified no issues (0 silenced).
February 08, 2020 - 07:51:40
Django version 3.0.3, using settings 'promptme.local'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

***

Open your web browser and go to the address: http://127.0.0.1:8000/

Presto!
