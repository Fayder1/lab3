from django.shortcuts import render
from products.models import ProductCategory, Product


def main(request):
    return render(
        request,
        'main/index.html',
        {
            'title': 'Сундук зі скарбами',
            'link_list': ['main/css/index.css'],
            'menu': ProductCategory.objects.all(),
            'obj': Product.objects.all(),
        }
    )


def contacts(request):
    return render(
        request,
        'main/contacts.html',
        {
            'title': 'Контакти',
            'link_list': ['main/css/contacts.css'],
            'menu': ProductCategory.objects.all(),
        }
    )
