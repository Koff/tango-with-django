from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm, PageForm


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]
    context_dictionary = {'categories': category_list, 'pages': pages_list}
    return render(request, 'rango/index.html', context_dictionary)


def about(request):
    context_dictionary = {'italicmessage': 'This is an italic message'}
    return render(request, 'rango/about.html', context_dictionary)


def category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        print("Category name from category.view: " + category.name)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        print("Pages from category.view: " + str(pages))
        context_dict['category'] = category
        context_dict['category_name_slug'] = category_name_slug
    except Category.DoesNotExist:
        pass
    return render(request, 'rango/category.html', context_dict)


def add_category(request):
    # If method is POST
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        # And form is valid
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    else:
        form = CategoryForm()
    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_slug):
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                # probably better to use a redirect here.
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()
    print("Catgory from add_page.view: " + str(cat))
    context_dict = {'form': form, 'category': cat}
    return render(request, 'rango/add_page.html', context_dict)

