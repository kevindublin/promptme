# Prompt Me
*a web service to spark creative writing & community. Currently testing the MVP. Many features left to add.*

![logo](https://raw.githubusercontent.com/kevindublin/promptme/master/apps/core/static/images/logo.png "logo")

## Known Issues:

- Home page slider and contents break styling on maximum Retina and widescreen displays
- ~~View Feedback shows all feedback for a user on each individual draft~~
- ~~Mobile Write view TinyMCE auto switches to full screen and can't see drip words~~
- Mobile view of Feedback Queue has uneven rows
- Bottom dock in mobile view is off-centere
- ~~Write View collapses and hides drip bank if not filled when window forces min width~~
- ~~Image and prompt will occasionally change when write is pressed~~
- ~~Feedback Queue view crashes when queue is empty~~

![prompt](https://raw.githubusercontent.com/kevindublin/promptme/master/apps/core/static/images/home_promptme.png "prompted")

![write](https://raw.githubusercontent.com/kevindublin/promptme/master/apps/core/static/images/home_write.png "written")

![dashboard](https://raw.githubusercontent.com/kevindublin/promptme/master/apps/core/static/images/home_dashboard.png "edited")


## Features to Add:

**Individual Features**
- Social Login with django-allauth
- Add pie charts for feedback results, analytics
- Third app with Full TinyMCE in-browser text editor to work on drafts
- Export writing to Google Drive and Dropbox
- Take photos of handwritten or printed text and OCR into editor as a draft for those who prefer to write by hand, uploadcare

**Community Features**
- Add broadside model many to one
- Post public broadside messages
- Add private messaging
- Add Collaborators model to User
- Follow User Feature
- Collaborator Feed to see that friends have written a new draft, ask to read it
- Exquisite Corpse, Renga, Call & Response games

**Membership and Subscription Features**
- Membership model
- Membership Tiers tied to account
- Pay Portal, accept payments through PayPal
- Number of queue calls, prompts, & drafts written tied to membership tier

**Writing Career Features**
- Submission Tracker
- Open calls for submissions
- User posted Calls for submissions
- Web scraper which pulls calls from all over the web and prompt me calls that API
