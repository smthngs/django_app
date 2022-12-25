from django import forms


class FontForm(forms.Form):
    fontstyle = forms.BooleanField(label="yazitipi", )
    def clean(self):
        fontstyle = self.cleaned_data.get("yazitipi")
        return super(FontForm, self).clean()
