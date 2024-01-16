from django.shortcuts import render

def loobby(request):
    return render(request, 'chat/lobby.html')
