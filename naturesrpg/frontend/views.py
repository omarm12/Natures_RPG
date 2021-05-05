from django.shortcuts import render

# Create your views here.
def home(request):
    if 'u' in request.GET:
        print("")
        
    return render(request, 'frontend/index.html')

def handler404(request):
    response = render(request, '400.html')
    response.status_code = 404
    return response

def handler500(request):
    response = render(request, '500.html')
    response.status_code = 500
    return response