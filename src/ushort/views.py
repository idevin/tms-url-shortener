from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db import IntegrityError
from ushort import utils
from ushort.forms import MainForm, HashForm
from ushort.models import Url
from shortener import settings
import urllib.parse


# Create your views here.

def redirect_home():
    return redirect('/')


def index(request):
    urls = Url.objects.all().order_by('-id')

    paginator = Paginator(urls, settings.PER_PAGE)
    page = request.GET.get('p', 1)
    items = paginator.get_page(page)
    uri = request.build_absolute_uri(location='')

    context = {
        'form': MainForm(),
        'items': items,
        'current_page': page,
        'uri': uri,
        'per_page': settings.PER_PAGE
    }

    return render(request, 'index.html', context=context)


def get(request):
    valid_form = MainForm(request.POST).is_valid()

    if request.method == 'POST' and valid_form:
        url = request.POST.get('url')
        if url:
            try:
                r = Url.objects.get(url=url)
            except Url.DoesNotExist:

                r = Url.objects.create(url=url)
                r.hash = utils.shorten(r.id)
                r.save()

            full_url = request.build_absolute_uri(location=r.hash)
            return render(request, 'get.html', context={
                'full_url': full_url,
            })

        else:
            return redirect_home()
        pass
    else:
        return redirect_home()


def redirect_to_url(request, hash):
    hash = urllib.parse.quote(hash)

    try:
        r = Url.objects.get(hash=hash)
        r.clicks += 1
        r.save()
    except Url.DoesNotExist:
        return redirect_home()

    return redirect(r.url)


def change_url(request, hash):
    form = HashForm(request.POST)

    try:
        r = Url.objects.get(hash=hash)
    except Url.DoesNotExist:
        return redirect_home()

    if request.method == 'GET':
        return render(request, 'hash.html', context={
            'form': form,
            'hash': r.hash,
            'original_hash': urllib.parse.unquote(r.hash),
            'uri': request.build_absolute_uri(location='/')
        })

    elif request.method == 'POST':
        h = request.POST.get('hash').strip()

        if h:
            h = urllib.parse.quote(h)
            r.hash = h
            try:
                r.save()
            except IntegrityError:
                pass

    return redirect_home()
