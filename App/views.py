from django.shortcuts import render,get_object_or_404,redirect
from .models import Contact
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Contact
    context_object_name = 'contacts'

    def get_queryset(self):
        contacts = super().get_queryset()
        return contacts.filter(manager=self.request.user)

class ContactDetailView(DetailView):
    template_name = 'detail.html'
    model = Contact
    context_object_name = 'contact'

class ContactCreateView(CreateView):
    model = Contact
    template_name = 'create.html'
    fields = ['name','email','phone','info','gender','image']
    success_url = '/'

    def form_valid(self, form):
        instance=form.save(commit=False)
        instance.manager=self.request.user
        instance.save()
        return redirect('home')

class ContactUpdateView(UpdateView):
    model = Contact
    template_name = 'update.html'
    fields = ['name', 'email', 'phone', 'info', 'gender', 'image']
    success_url = '/'

    def form_valid(self, form):
        istance=form.save()
        return redirect('detail',istance.pk)

class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'delete.html'
    success_url = '/'

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')