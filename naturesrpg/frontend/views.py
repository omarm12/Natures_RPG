from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'frontend/index.html')

def logged_in(request):
    if request.session["username"] is None:
        return render(request, 'frontend/index.html')

    return render(request, 'frontend/index.html')

def handler404(request):
    response = render(request, '400.html')
    response.status_code = 404
    return response

def handler500(request):
    response = render(request, '500.html')
    response.status_code = 500
    return response