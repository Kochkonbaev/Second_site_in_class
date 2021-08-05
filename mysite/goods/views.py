from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from .models import Goods
from .forms import NewForm


def all_goods(request):
    all_goods = Goods.objects.all()
    return render(request, 'goods/goods.html', {'all_goods': all_goods})


def goods_new(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('goods_detail', pk=news.pk)
    else:
        form = NewForm()
    return render(request, 'goods/goods_edit.html', {'form': form})


def goods_edit(request, pk):
    news = get_object_or_404(Goods, pk=pk)
    if request.method == "POST":
        form = NewForm(request.POST, instance=news)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('goods_detail', pk=news.pk)
    else:
        form = NewForm(instance=news)
    return render(request, 'goods/goods_edit.html', {'form': form})


def goods_detail(request, pk):
    goods_detail = get_object_or_404(Goods, pk=pk)
    return render(request,
                  'goods/goods_detail.html',
                  {'goods_detail': goods_detail,})


def goods_delete(request, pk):
    try:
        news = Goods.objects.get(id=pk)
        news.delete()
        return redirect('all_goods')

    except:
        return HttpResponseNotFound("<h2>Такой страницы нет</h2>")
