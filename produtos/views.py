from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto
from .forms import ProdutoForm


@login_required
def listagem(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})


@login_required
def create(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listagem_produtos')
    return render(request, 'novo_produto.html', {'form': form})


@login_required
def update(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, request.FILES or None,  instance=produto)
    if form.is_valid():
        form.save()
        return redirect('listagem_produtos')

    return render(request, 'novo_produto.html', {'form': form})


@login_required
def delete(request, id):
    produto = get_object_or_404(Produto, pk=id)

    if request.method == "POST":
        produto.delete()
        return redirect('listagem_produtos')

    return render(request, 'deletar_produto.html', {'produto': produto})
