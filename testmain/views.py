from django.shortcuts import render
# from django

# Create your views here.

def main(request):
    return render(request, 'root.html')