from django.apps import AppConfig


class ManagementConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "management"
    icon = "fa fa-users"

    def ready(self) -> None:
        from . import signals
        return super().ready()