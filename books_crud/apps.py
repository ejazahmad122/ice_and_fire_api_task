from django.apps import AppConfig


class BooksCrudConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'books_crud'

    def ready(self) -> None:
        import books_crud.signals
        return super().ready()
