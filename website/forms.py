from django.forms import ModelForm, TextInput

# from .models import CommitteeMember
from authentication.models import Profile
from website.models import Apartment, Facility


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


class FacilityForm(ModelForm):


    class Meta:
        model = Facility
        fields = (
            "title",
            "details",
            "price",
            "meta",
            "booked",
        )

        widgets = {
            "title": TextInput(
                attrs={"class": "form-control", "placeholder": "title"}
            ),
            "details": TextInput(
                attrs = {
                    "class": "form-control",
                    "placeholder": "details"
                }
            ),
            "price": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "price",
                }
            ),
            "meta": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "meta"
                }
            ),
            "booked": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "booked"
                }
            ),
        }