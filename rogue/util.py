from rogue.models import Entity, Character
from math         import floor

class Viewport(object):
    x1, y1 = (0, 0)
    x2, y2 = (100, 100)
    def __init__(self, centerx, centery, width_x, width_y):
        try:
            centerx, centery, width_x, width_y = int(centerx), int(centery), int(width_x), int(width_y)
        except TypeError:
            raise TypeError("Viewport couldn't be initialized")

        def _get_delta_from_width(width):
            """ Tuple of two values to add to the center """
            if width % 2 == 0:
                delta = width / 2
                return (-delta, delta)
            else:
                delta = floor(width / 2)
                return (-delta, delta + 1)

        self.x1, self.x2 = map(sum, zip(_get_delta_from_width(width_x), (center_x, center_x)))
        self.y1, self.y2 = map(sum, zip(_get_delta_from_width(width_y), (center_y, center_y)))

    def get_all_entities(self):
        return Entity.objects.filter(
            x__gte=self.x1
            y__gte=self.y1,
            x__lte=self.x2,
            y__lte=self.y2
        )
