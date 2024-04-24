from django.shortcuts import render, redirect
from .models import Finch, Hat
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    id_list = finch.hats.all().values_list('id')
    hat_that_finch_doesnt_have = Hat.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch,
        'feeding_form': feeding_form,
        'hats': hat_that_finch_doesnt_have
    })

def assoc_hat(request, finch_id, hat_id):
  Finch.objects.get(id=finch_id).hats.add(hat_id)
  return redirect('detail', finch_id=finch_id)

def unassoc_hat(request, finch_id, hat_id):
  Finch.objects.get(id=finch_id).hats.remove(hat_id)
  return redirect('detail', finch_id=finch_id)

def add_feeding(request, finch_id):
    submitted_form = FeedingForm(request.POST)
    if submitted_form.is_valid():
        new_feeding = submitted_form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
    model = Finch
    fields = ['type', 'color', 'description']

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['type', 'color', 'description']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'

class HatList(ListView):
    model = Hat

class HatDetail(DetailView):
    model = Hat

class HatCreate(CreateView):
    model = Hat
    fields = '__all__'

class HatUpdate(UpdateView):
    model = Hat
    fields = ['type', 'color']

class HatDelete(DeleteView):
    model = Hat
    success_url = '/hats'