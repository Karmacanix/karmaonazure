from django.shortcuts import render

# Create your views here.
def index(request):
    print("Request for blog index page received")
    developer = "karmacanix"
    context = {"developer": developer}
    return render(request, "blog/index.html", context)