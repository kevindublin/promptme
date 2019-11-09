# Prompt Me
*a web service to spark creative writing & community. Currently testing the MVP. Many features left to add.*

## Known Issues:

- View Feedback shows all feedback for a user on each individual draft
- Mobile Write view TinyMCE auto switches to full screen and can't see drip words
- Mobile View of Feedback Queue has uneven columns
- Bottom dock in mobile view is off-center
- Write View collapses and hides drip bank if not filled when window forces min width
- Feedback Queue view crashes when queue is empty (maybe fixed)


## Features to Add:

**Individual Features**
- Third app with Full TinyMCE in-browser text editor
- Export writing to Google Drive and Dropbox
- Social Login with django-allauth
- Take photos of handwritten or printed text and OCR into editor as a draft for those who prefer to write by hand, uploadcare


**Community Features**
- Add broadside model many to one
- Post public broadside messages
- Add private messaging
- Add Friends model to User
- Follow User Feature
- Collaborator Feed to see that friends have written a new draft

**Membership and Subscription Features**
- Membership Tiers tied to account
- Pay Portal, accept payments through PayPal

**Writing Career Features**
- Submission Tracker
- Open calls for submissions
- User posted Calls for submissions
- Web scraper and separate API which pulls from elsewhere
