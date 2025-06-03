from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ImageForm
from .models import Image

# Create your views here.
def home(request):
    """
    Render the home page with a form to upload images.
    """
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Optionally, you can redirect or display a success message
            messages.success(request, "Image uploaded successfully!")
            return redirect('success')  # Replace 'success' with your success page URL name
    form = ImageForm()
    images = Image.objects.all()
    return render(request, 'myapp/home.html',{"form":form, "images": images})

def success(request):
    """
    Render the success page after an image is uploaded.
    """
    
    return render(request, 'myapp/success.html',)