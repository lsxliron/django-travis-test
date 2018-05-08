# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
import forms
import models
from mixins.custom import MyContextMixin, MySingleObjectMixin, MyMultipleObjectMixin


class CreatePersonView(MyContextMixin, CreateView):
    form_class = forms.PersonForm
    template_name = 'myapp/create.html'
    form_title = "Create My Person"
    success_url = reverse_lazy('list-person')


class ListPersonView(MyMultipleObjectMixin, MyContextMixin, ListView):
    model = models.Person
    form_class = forms.PersonForm
    template_name = 'myapp/list.html'
    form_title = "List People"


class EditPersonView(MyContextMixin, MySingleObjectMixin, UpdateView):
    model = models.Person
    form_title = "Edit Person"
    form_class = forms.PersonForm
    template_name = "myapp/edit.html"
    pk_url_kwarg = 'uuid'
    success_url = reverse_lazy('list-person')


class DeletePersonView(MyContextMixin, MySingleObjectMixin, DeleteView):
    model = models.Person
    from_title = "Delete Person"
    template_name = 'myapp/delete.html'
    success_url = reverse_lazy('list-person')
