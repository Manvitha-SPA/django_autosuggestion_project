from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render

def home(request):
    if request.method == "GET":
        languages = ["C++", "Python", "PHP", "Java", "C", "Ruby", 
                     "R", "C#", "Dart", "Fortran", "Pascal", "Javascript"]
        return render(request, "index.html", {"languages": languages})