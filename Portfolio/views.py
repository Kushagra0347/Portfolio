from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

def home(request):
	if(request.POST):
		name = request.POST['name']
		from_email = request.POST['email']
		subject = f"{from_email} - {request.POST['subject']}"
		message = request.POST['message']
		message += f"\n{name}"
		print(message)

		try:
			send_mail(subject, message, 'kushagra1925.be20@chitkara.edu.in', ['guptakush0347@gmail.com'])
			messages.success(request, 'Message Sent!')
		except BadHeaderError:
			print("Error")
			return messages.info(request, 'Failed to send the Message! Please try Again')
		return redirect('home')
	return render(request, 'index.html')

def details(request, name):
	return render(request, f'portfolio-details/{name}.html')