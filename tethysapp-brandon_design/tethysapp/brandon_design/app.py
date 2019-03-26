from tethys_sdk.base import TethysAppBase, url_map_maker


class BrandonDesign(TethysAppBase):
    """
    Tethys app class for Brandon Design.
    """

    name = 'Brandon Design'
    index = 'brandon_design:home'
    icon = 'brandon_design/images/watercycle.jpg'
    package = 'brandon_design'
    root_url = 'brandon-design'
    color = '#55afb2'
    description = 'See the progression of the #Nerdalicious app!'
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
                url='brandon-design',
                controller='brandon_design.controllers.home'
            ),
            UrlMap(
                name='example',
                url='brandon-design/example',
                controller='brandon_design.controllers.example'
            ),
            UrlMap(
                name='proposal',
                url='brandon-design/proposal',
                controller='brandon_design.controllers.proposal'
            ),
            UrlMap(
                name='mockup',
                url='brandon-design/mockup',
                controller='brandon_design.controllers.mockup'
            ),
        )

        return url_maps
