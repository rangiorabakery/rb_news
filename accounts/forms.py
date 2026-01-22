from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        # fields = UserCreationForm.Meta.fields + ("age",)
        fields = (
            "username",
            "email",
            "age",
        )


class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        # fields = UserChangeForm.Meta.fields
        fields = (
            "username",
            "email",
            "age",
        )
