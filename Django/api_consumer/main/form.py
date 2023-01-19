from django import forms

class ApiForm(forms.Form):
    Term = forms.IntegerField(initial=84)
    NoEmp = forms.IntegerField(initial=45)
    NewExist = forms.FloatField(initial=1.0)
    CreateJob = forms.IntegerField(initial=0)
    RetainedJob = forms.IntegerField(initial=0)
    UrbanRural = forms.IntegerField(initial=0)
    RevLineCr = forms.CharField(initial='N')
    LowDoc = forms.CharField(initial='N')
    DisbursementGross = forms.IntegerField(initial=17000)
    BalanceGross = forms.IntegerField(initial=17000)
    GrAppv = forms.IntegerField(initial=127500)