from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageForm
from django.shortcuts import get_object_or_404
from .models import Image


# Create your views here.
@login_required()
def image_create(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            # data = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request, "Image added successfully")
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageForm(data=request.GET)
    return render(request, 'images/image/image_create.html', {'section': 'images',
                                                              'form': form})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'images/image/image_details.html', {'section': 'images', 'image': image})
