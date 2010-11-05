from django import forms
from django.utils.translation import ugettext as _

class VariantForm(forms.Form):
    def __init__(self, product=None, *args, **kwargs):
        self.product = product
        super(NonConfigurableVariantForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return True

    def get_variant(self):
        return self.product.variants.get()
