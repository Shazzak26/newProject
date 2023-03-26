from django.shortcuts import render,redirect
from .models import Category

# Create your views here.
def index(request):
    category = Category.objects.all()
    context = {'data': category}
    return render(request, 'administrator/products/index.html', context)


             # category create
def cat_create(request):
    if request.method=='POST':
        category.objects.create(
            name=request.POST.get(category),
            user=request.user
        )
        return redirect("categories.html")
    
    return render(request, "cat_create.html")


def cat_update(request):
    return render(request, "cat_update.html")


def categories(request):
    return render(request, "categories.html")

def home(request):
    return render(request, "base.html")

def register(request):
    return render(request, "register.html")