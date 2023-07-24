from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_type = request.GET.get('sort', None)
    template = 'catalog.html'

    if sort_type == 'name':
        all_list = Phone.objects.order_by(sort_type)

    elif sort_type == 'min_price':
        all_list = Phone.objects.order_by('price')

    elif sort_type == 'max_price':
        all_list = Phone.objects.order_by('-price')

    else:
        all_list = Phone.objects.all()
    
    context = {'phones': all_list}
    return render(request, template, context)


def show_product(request, slug):
    item = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': item}
    return render(request, template, context)
