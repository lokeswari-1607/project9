from django.shortcuts import render

# Create your views here.
def a2_first(request):
    d={'a':120,'b':300,'c':400}
    return render(request,'a2_first.html',d)

def a2_second(request):
    d={'name':'laddu'}
    return render(request,'a2_second.html',d)