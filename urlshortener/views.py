from django.shortcuts import render, redirect
from .forms import ShortenerForm
from .models import Shortener

def index(request):
    form  = ShortenerForm(request.POST or None)

    context = {
        'form': form
    }

    if request.method == 'GET':
        return render(request, 'home.html', context)

    if request.method == 'POST':

        if form.is_valid():
            shortened_object = form.save()

            context['new_url']  = request.build_absolute_uri('/') + shortened_object.short_url
            context['long_url'] = shortened_object.long_url

            return render(request, 'home.html', context)
        
        context['errors'] = form.errors
        return render(request, 'home.html', context)

def renderLoadFullUrl(request, short_url):
    try:
        shortened_object = Shortener.objects.get(short_url=short_url)
        return redirect(shortened_object.long_url, permanent=True)
    except Shortener.DoesNotExist:
        return render(request, 'redirect.html', {
            'error': 'URL não encontrada'
        })