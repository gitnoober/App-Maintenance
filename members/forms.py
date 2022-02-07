from django import forms

from .models import CommitteeMember


class CommitteMemberModelForm(forms.ModelForm):
    class Meta:
        model = CommitteeMember
        fields = "__all__"
