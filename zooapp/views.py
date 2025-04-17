from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm  # Supondo que você tenha um formulário para editar os itens

def home(request):
    return render(request, 'home.html')

# View para listar os itens
def listar_itens(request):
    itens = Item.objects.all()
    return render(request, 'listar_itens.html', {'itens': itens})

# View para editar um item (somente para a modificação, será usada no modal)
def editar_item(request, id):
    item = get_object_or_404(Item, id=id)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('listar_itens')  # Redireciona após salvar
    else:
        form = ItemForm(instance=item)
    
    # Retorna o formulário para ser renderizado no modal
    return render(request, 'editar_item_modal.html', {'form': form, 'item': item})

# View para adicionar um novo item
def adicionar_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_itens')  # Redireciona para a lista de itens após salvar
    else:
        form = ItemForm()

    return render(request, 'adicionar_item.html', {'form': form})

def excluir_item(request, id):
    item = get_object_or_404(Item, id=id)
    item.delete()
    return redirect('listar_itens')
