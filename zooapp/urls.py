from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("listar/", views.listar_itens, name="listar_itens"),
    path("editar/<int:id>/", views.editar_item, name="editar_item"),
    path(
        "adicionar/", views.adicionar_item, name="adicionar_item"
    ),  # Rota para adicionar item
    path("excluir/<int:id>/", views.excluir_item, name="excluir_item"),
    path("exportar_xlsx/", views.exportar_xlsx, name="exportar_xlsx"),
    path("importar/", views.importar_xlsx, name="importar_xlsx"),
]
