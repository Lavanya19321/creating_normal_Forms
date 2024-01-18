from django import forms

class schoolform(forms.Forms):
    uname=forms.CharField()
    sname=forms.CharField()
    slocation=forms.CharField()
    sprincipal=forms.CharField()