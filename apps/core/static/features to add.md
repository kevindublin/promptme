Known Issues:

-Fix View Feedback, so it's only for individual 

Features to Add:

**Individual Features**
-third app with Full TinyMCE in-browser text editor
-Export writing to Google Drive and Dropbox
-Social Login with django-allauth
-Take photos of handwritten or printed text and OCR into editor as a draft for those who prefer to write by hand, uploadcare


**Community Features**
-Add broadside model many to one
-Post public broadside messages
-Add private messaging
-Add Friends model to User
-Follow User Feature
-Collaborator Feed to see that friends have written a new draft

**Membership and Subscription Features**
-Membership Tiers tied to account
-Pay Portal, accept payments through PayPal

**Writing Career Features**
-Submission Tracker
-Open calls for submissions
-User posted Calls for submissions
-Web scraper and separate API which pulls from elsewhere



models.py

Class Message(models.Model):
	Sender = models.ForeignKey(User, related_name="sender")
	Recepient = # almost same as above field, just change the related-name
	msg_content = TextField
	sent = Boolean = False
	unread = BooleanField = True




Create a form for this model, use model form .

forms.py

Class MessageForm(forms.ModelForm)
	

views.py


Inbox view
Message.objects.filter(reciever=request.user)
sent = true

"Outbox" queries in views.py by
Message.objects.filter(sender = request.user)
sent=true

Unsent view
Message.objects.filter(sender = request.user)
sent=false

HTML

Three tabs, one with each inbox. Maybe add, messaget his user?
