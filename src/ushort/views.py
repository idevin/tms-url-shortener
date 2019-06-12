from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from ushort import utils
from ushort.forms import MainForm
from ushort.models import Url
from django.http import HttpResponse
from shortener import settings


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
        'uri': uri
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

            return render(request, 'get.html', context={'full_url': full_url})
        else:
            return redirect_home()
        pass
    else:
        return redirect_home()


def redirect_to_url(request, hash):
    try:
        r = Url.objects.get(hash=hash)
        r.clicks += 1
        r.save()
    except Url.DoesNotExist:
        return redirect_home()

    return redirect(r.url)
