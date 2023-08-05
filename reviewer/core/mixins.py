import sorl.thumbnail


class ImageMixin:
    @property
    def get_image_300x300(self) -> str:
        return self.get_sized_image('300x300').url

    def get_sized_image(self, size: str):
        if self.image:
            return sorl.thumbnail.get_thumbnail(
                self.image,
                size,
                crop='center',
                quality=99,
            )
        return sorl.thumbnail.get_thumbnail(
            self.DEFAULT_IMAGE,
            size,
            crop='center',
            quality=99,
        )


class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {}
        if hasattr(self.__class__, 'Meta'):
            if hasattr(self.__class__.Meta, 'placeholders'):
                placeholders = self.__class__.Meta.placeholders
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
            field.field.widget.attrs['placeholder'] = placeholders.get(
                field.name,
                '',
            )


class SearchViewMixin:
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
