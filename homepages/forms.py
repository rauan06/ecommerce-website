from django import forms

SIZE_CHOICES = [('xs','XS'),('m','M'), ('xl','XL')]


class Cart(forms.Form):
    """Form with essential information for cart"""
    sizes = forms.ChoiceField(required=True, label="",  label_suffix=" ", widget=forms.RadioSelect(), choices=SIZE_CHOICES) # Radio Select Field
    quantity = forms.IntegerField(label=" ",  label_suffix=" ", widget=forms.NumberInput(), min_value=1, max_value=100)


class UpdateTotal(forms.Form):
    """Form for views.update_total"""
    quantity = forms.IntegerField(label=" ",  label_suffix=" ", widget=forms.NumberInput(), min_value=1, max_value=100)
    

# class EntryForm(forms.ModelForm):
#     class Meta:
#         model = Entry
#         fields = ['text']
#         labels = {'text' : ''}
#         widgets = {'text': forms.Textarea(attrs={'cols':80})}