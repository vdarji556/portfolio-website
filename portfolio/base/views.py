from django.shortcuts import render, redirect
from django.contrib import messages
from base.models import Contect , Project,Technology  # Ensure correct model name

def contect(request):
    if request.method == "POST":
        name = request.POST.get('name', '')  
        email = request.POST.get('email', '')
        contect = request.POST.get('content', '')
        number = request.POST.get('number', '')

        # Validation
        if len(name) < 2 or len(name) > 30:
            messages.error(request, 'Length of name should be between 2 and 30 characters.')
            return render(request, 'home.html')

        if '@' not in email or '.' not in email:
            messages.error(request, 'Invalid email address.')
            return render(request, 'home.html')

        if len(contect) < 10:
            messages.warning(request, 'Content should be at least 10 characters long.')
            return render(request, 'home.html')

        if len(number) < 10 or len(number) > 15:
            messages.warning(request, 'Enter a valid phone number (10-15 digits).')
            return render(request, 'home.html')

        # Save to database
        contact_entry = Contect(
            name=name,
            email=email,
            number=number,
            contect=contect,
            )

        contact_entry.save()

        messages.success(request, 'Thank you for contacting me! Your message has been saved.')
        return render(request, 'home.html')  # Ensure 'home' exists in urls.py
    projects = Project.objects.all()
    context = {
        'projects':projects
    }
    return render(request, 'home.html',context )
