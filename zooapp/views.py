from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm

def home(request):
    return render(request, 'home.html')

def listar_itens(request):
    itens = Item.objects.all()
    return render(request, 'listar_itens.html', {'itens': itens})

def editar_item(request, id):
    item = get_object_or_404(Item, id=id)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('listar_itens')
        # Caso o form seja inválido, ele cai aqui e exibe os erros no modal
    else:
        form = ItemForm(instance=item)

    return render(request, 'editar_item_modal.html', {'form': form, 'item': item})

def adicionar_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_itens')
    else:
        form = ItemForm()
    return render(request, 'adicionar_item.html', {'form': form})

def excluir_item(request, id):
    item = get_object_or_404(Item, id=id)
    item.delete()
    return redirect('listar_itens')
