from django import forms 

CHOICES = (('Link with us', 'Link with ss'),
		   ('Write for us', 'Write for us'),
		   ('Profile your business / brand', 'Profile your business / brand '),
		   ('Submit your music/art', 'Submit your music/art' ),
		   ('Partnership Opportunities','Partnership Opportunities'),
		   ('Co-Hosting and Event', 'Co-Hosting an Event'),
		   ('Other', 'Other'))


class Contact_Form(forms.Form):
	name = CharField(required=True, label='Your Name: ')
	email = CharField(widget=forms.EmailInput(required=True, label='Your Email: '))
	subject = CharField(widget=forms.Select(choices=CHOICES, required=True, label='Im Trying to: '))
	body = CharField(widget=forms.TextArea(required=True, label='Your Message: '))