from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PollsConfig(AppConfig):
    name = 'polls'

    class Meta:
        verbose_name = _('polls')
