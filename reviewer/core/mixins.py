import sorl.thumbnail


class ImageMixin:
    @property
    def get_image_300x300(self):
        return self.get_sized_image('300x300')

    def get_sized_image(self, size: str):
        if self.image:
            return sorl.thumbnail.get_thumbnail(
                self.image,
                size,
                crop='center',
                quality=99,
            )
        return sorl.thumbnail.get_thumbnail(
            self.__class__.DEFAULT_IMAGE,
            size,
            crop='center',
            quality=99,
        )
