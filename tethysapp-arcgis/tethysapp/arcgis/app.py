from tethys_sdk.base import TethysAppBase, url_map_maker


class Arcgis(TethysAppBase):
    """
    Tethys app class for ArcGIS Test.
    """

    name = 'ArcGIS Test'
    index = 'arcgis:home'
    icon = 'arcgis/images/mealwithit.jpeg'
    package = 'arcgis'
    root_url = 'arcgis'
    color = '#799e00'
    description = 'Behold the pixelated taco'
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
                url='arcgis',
                controller='arcgis.controllers.home'
            ),
            UrlMap(
                name='shortestroute',
                url='arcgis/shortestroute',
                controller='arcgis.controllers.shortestroute'
            ),
            UrlMap(
                name='areameasure',
                url='arcgis/areameasure',
                controller='arcgis.controllers.areameasure'
            ),
        )



        return url_maps
