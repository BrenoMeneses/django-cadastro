from django.shortcuts import render, redirect
from .forms import formularioCadastro
from .models import user


def home(request):
    
    return render(request, 'html/index.html')






def login(request):

    return render(request, 'html/login.html')






def cadastro(request):

    form = formularioCadastro()
    if request.method == 'POST':

        form = formularioCadastro(request.POST)

        if form.is_valid():
            form.save()
            return redirect(f'/meuperfil/breno/')
        
    context = {
        'form': form
    } 
    return render(request, 'html/cadastro.html', context)





def meuperfil(request, nome):

    users = user.objects.all()

    context = {
        'users': users,
        'nome': nome,
    }

    return render(request, 'html/meuperfil.html', context)

