from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Membership(models.Model):
    class MembershipStatusChoices(models.TextChoices):
        PENDING = "Pending", _("Pending")
        ACTIVE = "Active", _("Active")
        LAPSED = "Lapsed", _("Lapsed")

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    chapter = models.ForeignKey(
        "chapters.Chapter",
        on_delete=models.CASCADE,
    )
    status = models.CharField(
        max_length=32,
        choices=MembershipStatusChoices.choices,
        null=True,
        blank=True,
    )
