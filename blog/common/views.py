class TitleMixin:
    title = None

    def get_context_data(self, **kwargs):
        contex = super(TitleMixin, self).get_context_data()
        contex['title'] = self.title
        return contex