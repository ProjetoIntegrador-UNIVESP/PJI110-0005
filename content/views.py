from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from content.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

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

"""
@login_required(login_url='/login/')
def curso(request):
    id_curso = request.GET.get('id')
    dados = {}
    if id_curso:
        try:
            dados['curso'] = Curso.objects.get(id=id_curso)
        except Exception:
            raise Http404()
    return render(request, 'curso.html', dados)
"""

@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        try:
            dados['evento'] = Evento.objects.get(id=id_evento)
        except Exception:
            raise Http404()
    return render(request, 'evento.html', dados)

"""
@login_required(login_url='/login/')
def submit_curso(request):
    if request.POST:
        id_curso = request.POST.get('id_curso')
        nome = request.POST.get('nome')
        link = request.POST.get('link')
        usuario = request.user
        if id_curso:
            curso = curso.objects.get(id=id_curso)
            if curso.usuario == usuario:
                curso.nome = nome
                curso.link = link
                curso.save()
        else:
            curso.objects.create(nome=nome,
                                link=link,
                                usuario=usuario)
    return redirect('agenda')
"""

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.descricao = descricao
                evento.data_evento = data_evento
                evento.save()
            #Evento.objects.filter(id=id_evento).update(titulo=titulo,
            #                                           data_evento=data_evento,
            #                                           descricao=descricao)
        else:
            Evento.objects.create(titulo=titulo,
                                  data_evento=data_evento,
                                  descricao=descricao,
                                  usuario=usuario)
    return redirect('/')

"""
@login_required(login_url='/login/')
def delete_curso(request, id_curso):
    usuario = request.user
    try:
        curso = Curso.objects.get(id=id_curso)
        if usuario == curso.usuario:
            curso.delete()
        else:
            raise Http404()
    except Exception:
        raise Http404()
    return redirect('agenda')
"""

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        evento = Evento.objects.get(id=id_evento)
    except Exception:
        raise Http404()
    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')

"""
@login_required(login_url='/login/')
def lista_cursos(request):
    usuario = request.user
    curso = Curso.objects.filter(usuario=usuario)
    dados = {'cursos':curso}
    return render(request, 'agenda.html', dados)
"""

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    data_atual = datetime.now() - timedelta(hours=1)
    evento = Evento.objects.filter(usuario=usuario,
                                   data_evento__gt=data_atual)
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)

"""
@login_required(login_url='/login/')
def lista_cursos_historico(request):
    usuario = request.user
    data_atual = datetime.now()
    curso = Curso.objects.filter(usuario=usuario,
                                data_criacao__lt=data_atual)
    dados = {'cursos':curso}
    return render(request, 'historico.html', dados)
"""

@login_required(login_url='/login/')
def lista_eventos_historico(request):
    usuario = request.user
    data_atual = datetime.now()
    evento = Evento.objects.filter(usuario=usuario,
                                   data_evento__lt=data_atual)
    dados = {'eventos':evento}
    return render(request, 'historico.html', dados)

"""
def json_lista_curso(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)
    curso = Curso.objects.filter(usuario=usuario).values('id', 'nome')
    return JsonResponse(list(curso), safe=False)
"""

def json_lista_evento(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)
    evento = Evento.objects.filter(usuario=usuario).values('id', 'titulo')
    return JsonResponse(list(evento), safe=False)