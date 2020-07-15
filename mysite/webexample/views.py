from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h3>Hello world</h3>')