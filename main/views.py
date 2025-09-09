from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app' : 'Ozon Sportswear',
        'name': 'Farrell Bagoes Rahmantyo',
        'npm' : '2406420596',
    }

    return render(request, "main.html", context)