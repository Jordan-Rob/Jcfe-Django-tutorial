from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(required=False,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "Enter Your Title"
                                }
                            ))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          'placeholder': "Your Description",
                                          'rows': 16,
                                          'cols': 40
                                      }
                                  ))
    price = forms.DecimalField()

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "fee" in title:
            raise forms.ValidationError("invalid title")
        return title
                    

class RawProductForm(forms.Form):
    title = forms.CharField(required=False,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "Enter Your Title"
                                }
                            ))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          'placeholder': "Your Description",
                                          'rows': 16,
                                          'cols': 40
                                      }
                                  ))
    price = forms.DecimalField()
