from django.shortcuts import render, redirect, get_object_or_404
from .forms import URLForm
from .models import ShortURL


def home(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            long_url = form.cleaned_data['long_url']
            short_url, created = ShortURL.objects.get_or_create(long_url=long_url)
            return render(request, 'shortener/home.html', {'form': form, 'short_url': request.build_absolute_uri('/') + short_url.short_code})
    else:
        form = URLForm()
    return render(request, 'shortener/home.html', {'form': form})

def redirect_to_long_url(request, short_code):
    short_url = get_object_or_404(ShortURL, short_code=short_code)
    short_url.clicks += 1
    short_url.save()
    return redirect(short_url.long_url)