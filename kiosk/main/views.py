from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ProductCategory

# List categories
class CategoryListView(ListView):
    model = ProductCategory
    template_name = 'categories/category_list.html'
    context_object_name = 'categories'

# Create a new category
class CategoryCreateView(CreateView):
    model = ProductCategory
    fields = ['name', 'description']
    template_name = 'categories/category_form.html'
    # success_url = reverse_lazy('category_list')

# Update a category
class CategoryUpdateView(UpdateView):
    model = ProductCategory
    fields = ['name', 'description']
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('category_list')

# Delete a category
class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'categories/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')
