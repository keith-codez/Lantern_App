# views.py
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            # Save the form data into the database
            contact_message = form.save()

            # Redirect to the success page or show a message
            return redirect('success_view')  # or render a success message

    else:
        form = ContactForm()

    return render(request, 'contact/index.html', {'form': form})

def success_view(request):
    return render(request, 'contact/success.html')