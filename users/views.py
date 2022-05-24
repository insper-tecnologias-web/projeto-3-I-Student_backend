from django.http import HttpResponse


def index(request):
    return HttpResponse("Ei! Não era pra você estar vendo essa parte!!")
