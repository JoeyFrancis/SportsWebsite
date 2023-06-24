import os
from datetime import date

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from SITE_TB_06 import settings
from clube.models import Utilizador, Jogo, Equipa, Bilhete, ItemCarrinho, Carrinho, Produto
from .models import Noticia


def index(request):
    return render(request, 'clube/index.html')

def historia(request):
    return render(request, 'clube/historia.html')

def faqs(request):
    return render(request, 'clube/faqs.html')

def fazlogin(request):
    if request.method == 'POST':
        # tratar os dados do formulário de Login, neste caso username e password
        name = request.POST['username']
        passwd = request.POST['password']
        u = authenticate(username=name, password=passwd)
        if u is not None:
            login(request,u)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'clube/login.html', {'msg_erro':'Credenciais inválidas!'})

    else:
        # mostrar o formulário de login
        return render(request, 'clube/login.html')

def fazlogout (request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def registo (request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    primeiro_nome = request.POST.get('first_name')
    ultimo_nome = request.POST.get('last_name')
    data_nascimento = request.POST.get('data_nascimento')
    telemovel = request.POST.get('telemovel')
    if username and email and password is not None:
        u = User.objects.create_user(username, email, password)
        u.first_name = primeiro_nome
        u.last_name = ultimo_nome
        u.save()
        util = Utilizador(user=u, telemovel=telemovel, data_nascimento=data_nascimento)
        util.save()
        return HttpResponseRedirect(reverse('fazlogin'))
    else:
        return render(request, 'clube/registo.html')

def visualizainfo(request):
    return render(request, 'clube/informacao.html')

def proximosjogos(request):
    jogos = Jogo.objects.filter(data__gte=date.today()).order_by('data')
    context = {'jogos': jogos}
    return render(request, 'clube/proximosjogos.html', context)


def adicionarjogo(request):
    equipas = Equipa.objects.all()
    context = {'equipas': equipas}

    if request.method == 'POST':
        nome_clube = request.POST['combobox_field']

        if Jogo.objects.filter(clube=nome_clube).exists():
            mensagem = 'Já vamos jogar com eles esta época!'
            return render(request, 'clube/adicionarjogo.html', {'mensagem': mensagem, **context})

        else:
            clube = Equipa.objects.get(nome__icontains=nome_clube)
            data = request.POST['data']
            hora = request.POST['hora']
            estadio = request.POST['estadio']
            jogo = Jogo(clube=clube, data=data, hora=hora, estadio=estadio)
            jogo.save()
            return redirect('proximosjogos')

    else:
        return render(request, 'clube/adicionarjogo.html', context)


def listanoticias(request):
    noticias = Noticia.objects.order_by('-data')
    return render(request, 'clube/listanoticias.html', {'noticias': noticias})

def detalhenoticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    return render(request, 'clube/detalhenoticia.html', {'noticia': noticia})

def novanoticia(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        conteudo = request.POST['conteudo']
        data = request.POST['data']
        imagem = request.FILES['imagem']
        fs = FileSystemStorage()
        filename = fs.save(imagem.name, imagem)
        url = os.path.join(settings.MEDIA_URL, filename)
        noticia = Noticia(titulo=titulo, conteudo=conteudo, data=data, imagem=url)
        noticia.save()
        return redirect('listanoticias')
    else:
        return render(request, 'clube/novanoticia.html')

def comprar_bilhete(request, ticket_id):
    jogo = Jogo.objects.get(id=ticket_id)  # Obtém o objeto Jogo associado ao Bilhete
    if request.method == 'POST':
        quantidade = int(request.POST.get('quantity', 1))
        bilhete = Bilhete(jogo=jogo, quantidade=quantidade)
        # Salvar o bilhete no banco de dados
        bilhete.save()
        return redirect('proximosjogos')
    return render(request, 'clube/pagamento.html', {'jogo': jogo})


def loja(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, 'loja/product_list.html', context)

def product_list(request):
    produtos = Produto.objects.all()
    return render(request, 'product_list.html', {'products': produtos})

def carrinho(request):
    carrinho_itens = ItemCarrinho.objects.all()
    total = 0
    for item in carrinho_itens:
        subtotal = item.produto.price * item.quantidade
        total += subtotal
        item.preco_total = subtotal
    context = {'carrinho_itens': carrinho_itens, 'total': total}
    return render(request, 'loja/carrinho.html', context)

def adicionar_ao_carrinho(request, produto_id):
    # obter o produto com base no id
    produto = get_object_or_404(Produto, id=produto_id)

    # verificar se o carrinho existe para o usuário ou criar um novo
    try:
        carrinho = Carrinho.objects.get(usuario=request.user, ativo=True)
    except Carrinho.DoesNotExist:
        carrinho = Carrinho(usuario=request.user)
        carrinho.save()

    # verificar se o item já existe no carrinho ou criar um novo
    try:
        item_carrinho = ItemCarrinho.objects.get(carrinho=carrinho, produto=produto)
        item_carrinho.quantidade += 1
        item_carrinho.save()
    except ItemCarrinho.DoesNotExist:
        item_carrinho = ItemCarrinho(carrinho=carrinho, produto=produto)
        item_carrinho.save()

    return redirect('carrinho')

def remover_do_carrinho(request, item_id):
    # obter o item do carrinho com base no id
    item_carrinho = get_object_or_404(ItemCarrinho, id=item_id)

    # verificar se o item pertence ao carrinho do usuário
    if item_carrinho.carrinho.usuario != request.user:
        return redirect('carrinho')

    # atualizar a quantidade do item no carrinho ou removê-lo se a quantidade for zero
    if item_carrinho.quantidade > 1:
        item_carrinho.quantidade -= 1
        item_carrinho.save()
    else:
        item_carrinho.delete()

    return redirect('carrinho')
