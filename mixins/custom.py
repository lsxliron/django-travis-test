from django.views.generic.edit import ContextMixin, SingleObjectMixin
from django.views.generic.list import MultipleObjectMixin


class MyContextMixin(ContextMixin):
    form_title = None

    def get_context_data(self, **kwargs):
        context = super(MyContextMixin, self).get_context_data(**kwargs)
        context['form_title'] = self.form_title
        return context


class MyMultipleObjectMixin(MultipleObjectMixin):
    form_title = None

    def get_queryset(self):
        return self.model.objects.all()


class MySingleObjectMixin(SingleObjectMixin):
    kwargs = {}

    def get_object(self, queryset=None):
        return self.model.objects.get(uuid=self.kwargs['uuid'])
