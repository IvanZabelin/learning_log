from django.shortcuts import render


def index(request):
    """Домашняя страница."""
    return render(request, 'learning_logs/index.html')