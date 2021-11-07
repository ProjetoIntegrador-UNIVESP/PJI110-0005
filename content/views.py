from django.shortcuts import render, redirect
from content.models import Curso
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http.response import Http404
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def login_user(request):
    return render(request, 'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            messages.error(request, "Usuário ou Senha inexistente")
            return redirect('login')
    else:
        return redirect('home')

def logout_user(request):
    logout(request)
    return redirect('home')

def handler404(request, exception):
    return render(request, '404.html')

@login_required(login_url='/login/')
def cursos(request):
    usuario = request.user
    if usuario.is_superuser:
        curso = Curso.objects.all()
        dados = {'cursos':curso}
        return render(request, 'cursos.html', dados)
    else:
        raise Http404()

@login_required(login_url='/login/')
def novo_curso(request):
    usuario = request.user
    if usuario.is_superuser:
        id_curso = request.GET.get('id')
        dados = {}
        if id_curso:
            try:
                dados['curso'] = Curso.objects.get(id=id_curso)
            except Exception:
                raise Http404()
        return render(request, 'curso.html', dados)
    else:
        raise Http404()

@login_required(login_url='/login/')
def submit_novo_curso(request):
    if request.POST:
        nome = request.POST.get('nome')
        link = request.POST.get('link')
        usuario = request.user
        id_curso = request.POST.get('id_curso')
        if id_curso:
            Curso.objects.filter(id=id_curso).update(nome=nome, link=link)
        else:
            Curso.objects.create(nome=nome, link=link, usuario=usuario)
    return redirect('cursos')

@login_required(login_url='/login/')
def delete_curso(request, id_curso):
    usuario = request.user
    if usuario.is_superuser:
        try:
            curso = Curso.objects.get(id=id_curso)
            curso.delete()
        except Exception:
            raise Http404()
    else:
        raise Http404()
    return redirect('cursos')

@login_required(login_url='/login/')
def lista_cursos(request):
    try:
        curso = Curso.objects.all()
        dados = {'cursos':curso}
        return render(request, 'lista-cursos.html', dados)
    except Exception:
        raise Http404()