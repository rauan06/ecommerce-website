from django import forms

SIZE_CHOICES = [('xs','XS'),('m','M'), ('xl','XL')]

class Cart(forms.Form):
    sizes = forms.ChoiceField(label="",  label_suffix=" ", widget=forms.RadioSelect(attrs={'class':'btn-check'}), choices=SIZE_CHOICES)
    quantity = forms.IntegerField(label=" ",  label_suffix=" ", widget=forms.NumberInput())




# class EntryForm(forms.ModelForm):
#     class Meta:
#         model = Entry
#         fields = ['text']
#         labels = {'text' : ''}
#         widgets = {'text': forms.Textarea(attrs={'cols':80})}