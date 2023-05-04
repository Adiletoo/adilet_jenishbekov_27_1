from django.shortcuts import render, redirect

from Online_store.form import ProductsCreateForm , CommentCreateForm
from posts.models import Products, Comment


# Create your views here.

def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Products.objects.all()
        context = {
            'products': products
        }
        return render(request, 'products/products.html', context=context)

def product_detail_view(request, id):
    if request.method == 'GET':
        products = Products.objects.get(id=id)

        context = {
            'product': products,
            'comments': products.comment_set.all(),
            'form': CommentCreateForm
        }

        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        products = Products.objects.get(id=id)
        data = request.POST
        form = CommentCreateForm(data=data)

        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data.get('text'),
            )

        context = {
            'product': products,
            'comments': products.comment_set.all(),
            'form': form
        }

        return render(request, 'products/detail.html', context=context)


def create_products_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductsCreateForm,}
        return render(request, 'products/create.html', context=context)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = ProductsCreateForm(data, files)

        if form.is_valid():
            Products.objects.create(
                image=form.cleaned_data.get("image"),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get("description"),
                rate=form.cleaned_data.get('rate')
            )
            return redirect("/products/")
        return render(request, 'products/create.html', context={'form': form})
