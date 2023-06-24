from django.urls import path
from . import views
# o '.' significa que importa views da mesma directoria)

urlpatterns = [
    path('', views.index, name='index'),
    path('historia', views.historia, name='historia'),
    path('jogos/', views.proximosjogos, name='lista_jogos'),
    path('jogos/comprar/<int:ticket_id>/', views.comprar_bilhete, name='comprar_bilhete'),
    path('faqs', views.faqs, name='faqs'),
    path('loja', views.loja, name='loja'),
    path('carrinho', views.carrinho, name='carrinho'),
    path('product_list', views.product_list, name='products'),
    path('produto/<int:produto_id>/', views.adicionar_ao_carrinho, name='cart'),
    path('carrinho/remover/<int:item_id>/', views.remover_do_carrinho, name='remove_cart'),
    path('fazlogin', views.fazlogin, name='fazlogin'),
    path('fazlogout', views.fazlogout, name='fazlogout'),
    path('registo', views.registo, name='registo'),
    path('visualizainfo', views.visualizainfo, name='visualizainfo'),
    path('proximosjogos/', views.proximosjogos, name='proximosjogos'),
    path('adicionarjogo', views.adicionarjogo, name='adicionarjogo'),
    path('listanoticias', views.listanoticias, name='listanoticias'),
    path('listanoticias/<int:noticia_id>', views.detalhenoticia, name='detalhenoticia'),
    path('novanoticia', views.novanoticia, name='novanoticia'),
]