from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.list import ListView # 데이터 보여주기
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView #데이터 추가
from .models import ClassBlog

# Create your views here.
#목록보기 
class BlogView(ListView):
    model = ClassBlog

class BlogCreate(CreateView):
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

#상세내용보기
class BlogDetail(DetailView):
    model = ClassBlog

class BlogUpdate(UpdateView):
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView):
    model = ClassBlog
    success_url = reverse_lazy('list')