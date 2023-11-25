from django.shortcuts import render
def index(request):
    return  render(request,'main/index.html')

def about(request):
    return render(request,'main/about.html')

def work(request):
    return render(request,'main/work.html')
def works(request):
    return render(request,'main/works.html')

def contact(request):
    return render(request,'main/contact.html')




