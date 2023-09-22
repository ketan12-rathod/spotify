from django.shortcuts import render,HttpResponse

# Create your views here.
def simple_response(request):
    # Create a simple HTTP response with plain text content and a 200 OK status code.
    response = HttpResponse("Hello, world!")
    return response