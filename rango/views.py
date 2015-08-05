from django.shortcuts import render

# Create your views here.


def index(request):
    context_dict = {'boldmessage': "I am bold font from the context",'sasi':"kumar"}
    return render(request, 'index.html', context_dict)
