from django.forms import ModelForm, TextInput

# from .models import CommitteeMember
from authentication.models import Profile


class CommitteMemberForm(ModelForm):
    class Meta:
        model = Profile
        fields = (
            "name",
            "user",
            "contact_number",
            "emergency_contact_number",
            "apartment",
            "building",
            "flat",
            "status",
            "blood_group",
            "family_members",
        )

        widgets = {
            "name": TextInput(
                attrs={"class": "form-control", "placeholder": "Full Name"}
            ),
            "user": TextInput(
                attrs={
                    "class": "form-control",
                    "value": "",
                    "id": "unique",
                    "type": "hidden",
                }
            ),
            # 'user': Select(attrs={'class':'form-control'}),
            "contact_number": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Contact Number",
                }
            ),
            "emergency_contact_number": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Emergency Contact Number",
                }
            ),
            "apartment": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Apartment Name",
                }
            ),
            "building": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Building Name",
                }
            ),
            "flat": TextInput(
                attrs={"class": "form-control", "placeholder": "Flat Number"}
            ),
            "status": TextInput(
                attrs={"class": "form-control", "placeholder": "Owner/Tenant"}
            ),
            "blood_group": TextInput(
                attrs={"class": "form-control", "placeholder": "Blood Group"}
            ),
            "family_members": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Number of Family Members",
                }
            ),
        }


class UpdateCommitteMemberForm(ModelForm):
    class Meta:
        model = Profile
        fields = (
            "name",
            "contact_number",
            "emergency_contact_number",
            # "apartment_name",
            # "flat_number",
            "blood_group",
            "family_members",
        )

        widgets = {
            "name": TextInput(
                attrs={"class": "form-control", "placeholder": "Full Name"}
            ),
            "contact_number": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Contact Number",
                }
            ),
            "emergency_contact_number": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Emergency Contact Number",
                }
            ),
            # "apartment_name": TextInput(
            #     attrs={
            #         "class": "form-control",
            #         "placeholder": "Apartment Name",
            #     }
            # ),
            # "flat_number": TextInput(
            #     attrs={"class": "form-control", "placeholder": "Flat Number"}
            # ),
            "blood_group": TextInput(
                attrs={"class": "form-control", "placeholder": "Blood Group"}
            ),
            "family_members": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Number of Family Members",
                }
            ),
        }
