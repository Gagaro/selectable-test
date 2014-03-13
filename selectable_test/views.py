from django import forms
from django.views.generic.edit import FormView
from selectable.forms import AutoCompleteSelectField, AutoComboboxWidget
from selectable.base import LookupBase
from selectable.registry import registry


class MyLookup(LookupBase):
    def get_query(self, request, term):
        return range(1, 11)

registry.register(MyLookup)


class MyForm(forms.Form):
    autocomplete = AutoCompleteSelectField(
        lookup_class=MyLookup,
        label='Test',
        widget=AutoComboboxWidget(lookup_class=MyLookup),
        required=False,
    )


class MyView(FormView):
    template_name = "home.html"
    form_class = MyForm
