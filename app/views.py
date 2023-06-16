from django.shortcuts import render

# Create your views here.
def codition(request):
    d={'a':30}
    return render(request,codition.html,context=d)
