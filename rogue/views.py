from django.shortcuts import render

def main(request):
    return render(request, 'rogue/main.html', {})
