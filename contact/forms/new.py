from django import forms
from datetime import datetime
from contact import models

class UpdateForm(forms.Form):
    request_no = forms.CharField(max_length=6, label='見積り番号', required=True)
    name = forms.CharField(max_length=100, label='タイトル', required=True)
    message = forms.CharField(max_length=1000, label='コメント', required=False)
    create_date = forms.DateTimeField(label='作成日', required=False)
    update_date = forms.DateTimeField(label='更新日', required=False)

    # service = forms.ModelChoiceField(
    #     queryset=models.Service.objects.values_list("name", flat=True).distinct(),
    #     label="サービス",
    #     empty_label=None
    # )