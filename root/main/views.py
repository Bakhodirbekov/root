from django.shortcuts import render
from .froms import JobApplicationForm
from .models import Category
from .models import SubCategory
from .models import Work

def index(request):
    ctg = Category.objects.all()
    ctx = {
        'ctg': ctg
    }
    return render(request,'main/index.html', ctx)


def about(request):
    ctx = {}
    return render(request,'main/about.html', ctx)

def work(request):
    wctg = Work.objects.all()
    ctx = {
        'wctg' : wctg
    }
    return render(request,'main/work.html',ctx)
def works(request):
    sctg = SubCategory.objects.all()
    ctx = {
        'sctg' : sctg
            }
    return render(request,'main/works.html',ctx)

def contact(request):
    ctx = {}
    return render(request,'main/contact.html',ctx)

def success(request):
    ctx = {}
    return render(request,'main/success.html',ctx)

def registor_file(request):
    ctx = {}
    return render(request, 'main/registor_file.html', ctx)


def catigory_page(request):
    ctg = Category.objects.all()
    ctx = {
        'ctg': ctg
    }
    return render(request, 'main/catigory.html', ctx)