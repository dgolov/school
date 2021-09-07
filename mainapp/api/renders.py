from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer


class CustomBrowsableAPIRenderer(BrowsableAPIRenderer):
    """ Кастомизированный рендер сделанный под стиль DRF """
    def get_default_renderer(self, view):
        return JSONRenderer()
