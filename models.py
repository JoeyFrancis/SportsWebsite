from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Utilizador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telemovel = models.CharField(max_length=20)
    data_nascimento = models.DateField()

class Socio(Utilizador):
    nr_votos = models.IntegerField(default=0)
    foto = models.URLField(default='')

    def __str__(self):
        return f'Socio {self.user.username}'

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.CharField(max_length=1000)
    data = models.DateField(default=timezone.now)
    imagem = models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self):
        return self.titulo

class Equipa(models.Model):
    simbolo = models.URLField(default='', unique=True)
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Jogo(models.Model):
    clube = models.OneToOneField(Equipa, on_delete=models.CASCADE, to_field='nome', related_name='jogo_clube', null=True)
    data = models.DateField(default=timezone.now)
    nome = models.CharField(max_length=100,default=None)
    estadio = models.CharField(max_length=100)
    hora = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.nome

class Bilhete(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE,default=None)
    stadium = models.CharField(max_length=100,default=None)
    data = models.DateField()
    quantidade = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return f'Bilhete para {self.jogo}'

    def calcular_preco_total(self):
        # lógica para calcular o preço total do bilhete
        pass

class Carrinho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Carrinho de {self.usuario.username}'

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_list/', null=True, blank=True)

    def __str__(self):
        return self.nome

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantidade} x {self.produto.nome} no carrinho de {self.carrinho.usuario.username}'
