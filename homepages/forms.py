from django import forms

SIZE_CHOICES = [('xs','XS'),('m','M'), ('xl','XL')]


class Cart(forms.Form):
    # Form with essential information for cart
    sizes = forms.ChoiceField(required=True, label="",  label_suffix=" ", widget=forms.RadioSelect(), choices=SIZE_CHOICES) # Radio Select Field
    quantity = forms.IntegerField(label=" ",  label_suffix=" ", widget=forms.NumberInput())


# class EntryForm(forms.ModelForm):
#     class Meta:
#         model = Entry
#         fields = ['text']
#         labels = {'text' : ''}
#         widgets = {'text': forms.Textarea(attrs={'cols':80})}