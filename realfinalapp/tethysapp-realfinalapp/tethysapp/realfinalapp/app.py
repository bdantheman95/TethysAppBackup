from tethys_sdk.base import TethysAppBase, url_map_maker


class Realfinalapp(TethysAppBase):
    """
    Tethys app class for Realfinalapp.
    """

    name = 'Realfinalapp'
    index = 'realfinalapp:home'
    icon = 'realfinalapp/images/icon.gif'
    package = 'realfinalapp'
    root_url = 'realfinalapp'
    color = '#5b3b26'
    description = 'Place a brief description of your app here.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='realfinalapp',
                controller='realfinalapp.controllers.home'
            ),
        )

        return url_maps
