from django import forms
from django.contrib.auth.forms import (
    PasswordChangeForm,
    UserChangeForm,
    UserCreationForm,
)
from django.contrib.auth.models import User
from django.forms import TextInput

from website.models import Apartment, Building, Flat

from .models import Profile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"


class EditProfileForm(UserChangeForm):

    username = forms.CharField(
        # max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
        max_length=100,
        widget=forms.TextInput(),
    )
    password = None

    class Meta:
        model = User
        fields = ("username",)


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ["username"]


class UpdateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", "")
        apartment_id, building_id, flat_id = None, None, None
        for i in kwargs:
            if kwargs[i].apartment_id:
                apartment_id = kwargs[i].apartment_id
            if kwargs[i].building_id:
                building_id = kwargs[i].building_id
            if kwargs[i].flat_id:
                flat_id = kwargs[i].flat_id

        super(UpdateProfileForm, self).__init__(*args, **kwargs)

        self.fields["apartment"] = forms.ModelChoiceField(
            queryset=Apartment.objects.all()
        )
        if apartment_id:
            self.fields["building"] = forms.ModelChoiceField(
                queryset=Building.objects.filter(apartment_id=apartment_id)
            )
        else:
            self.fields["building"] = forms.ModelChoiceField(
                queryset=Building.objects.all()
            )

        if apartment_id:
            self.fields["flat"] = forms.ModelChoiceField(
                queryset=Flat.objects.filter(apartment_id=apartment_id)
            )
        else:
            self.fields["flat"] = forms.ModelChoiceField(
                queryset=Flat.objects.all()
            )

    class Meta:
        model = Profile
        fields = (
            "name",
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


# class UpdateProfileForm(forms.ModelForm):
#     name = forms.CharField(max_length=100,required=True)
#     status = forms.CharField(max_length=100,required=True)
#     phone_regex = RegexValidator(
#         regex=r"^\+?1?\d{9,15}$",
#         message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
#     )
#     contact_number = forms.CharField(validators=[phone_regex],max_length=17)
#     emergency_contact_number = forms.CharField(validators=[phone_regex],max_length=17)
#     blood_group = forms.CharField(max_length=50)
#     family_members = forms.CharField()

#     class Meta:
#         model = Profile
#         fields = ['name', 'status', 'contact_number', 'emergency_contact_number','blood_group', 'family_members']


class PasswordChangedForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "type": "password"}
        )
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "type": "password"}
        )
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "type": "password"}
        )
    )

    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")
