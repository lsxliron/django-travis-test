from mixins import custom as mixins
from django.test import TestCase
from django.views.generic import TemplateView
from mock import patch, MagicMock

class TestMyMultipleObjectMixin(TestCase):

    class DummyView(mixins.MyMultipleObjectMixin, TemplateView):
        pass

    def setUp(self):
        self.view = self.DummyView()

    def test_queryset(self):

        with patch.object(self.view, 'model') as mocked_model:
            mocked_model.objects.all = MagicMock(return_value="all items")
            qs = self.view.get_queryset()
        self.assertEqual(qs, "all items")


class TestMySingleObjectMixin(TestCase):

    class DummyView(mixins.MySingleObjectMixin, TemplateView):
        kwargs = None
        pass

    def setUp(self):

        self.view = self.DummyView()

    def test_single_object(self):
        with patch.object(self.view, 'kwargs', return_value={"uuid":"my_uuid"}):
            # mocked_kwargs{'uuid': 'my_uuid'}
            with patch.object(self.view, 'model') as mocked_model:
                mocked_model.objects.get = MagicMock(return_value="my_object")
                obj = self.view.get_object()
        self.assertEqual(obj, 'my_object')
        self.assertTrue('objects.get' in mocked_model.method_calls[0])


class TestMyContextMixin(TestCase):
    class DummyView(mixins.MyContextMixin, TemplateView):
        form_title = "my_title"
        pass


    def setUp(self):
        self.view = self.DummyView()


    def test_context(self):
        """
            tests the context mixin
        """
        context = self.view.get_context_data()
        self.assertEqual(context['form_title'], 'my_title')