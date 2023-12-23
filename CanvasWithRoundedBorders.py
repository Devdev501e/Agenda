from tkinter import *


class CanvasWithRoundedBorders(Canvas):

    def __init__(self, master=None, width=None, height=None, **kwargs):

        Canvas.__init__(self, master, width=width, height=height, **kwargs)
        self.width = width
        self.height = height

    def set_height(self, height):
        self.height = height
        self.config(height = height)

    def round_polygon(self, x, y, sharpness, **kwargs):

        # The sharpness here is just how close the sub-points
        # are going to be to the vertex. The more the sharpness,
        # the more the sub-points will be closer to the vertex.
        # (This is not normalized)
        if sharpness < 2:
            sharpness = 2

        ratio_multiplier = sharpness - 1
        ratio_dividend = sharpness

        # Array to store the points
        points = []

        # Iterate over the x points
        for i in range(len(x)):
            # Set vertex
            points.append(x[i])
            points.append(y[i])

            # If it's not the last point
            if i != (len(x) - 1):
                # Insert sub_multiples points. The more the sharpness, the more these points will be
                # closer to the vertex.
                points.append((ratio_multiplier * x[i] + x[i + 1]) / ratio_dividend)
                points.append((ratio_multiplier * y[i] + y[i + 1]) / ratio_dividend)
                points.append((ratio_multiplier * x[i + 1] + x[i]) / ratio_dividend)
                points.append((ratio_multiplier * y[i + 1] + y[i]) / ratio_dividend)
            else:
                # Insert sub_multiples points.
                points.append((ratio_multiplier * x[i] + x[0]) / ratio_dividend)
                points.append((ratio_multiplier * y[i] + y[0]) / ratio_dividend)
                points.append((ratio_multiplier * x[0] + x[i]) / ratio_dividend)
                points.append((ratio_multiplier * y[0] + y[i]) / ratio_dividend)
                # Close the polygon
                points.append(x[0])
                points.append(y[0])

        return self.create_polygon(points, **kwargs, smooth=TRUE)

    def create_canvas_rounded(self):
        self.round_polygon([5, self.width, self.width, 5],
                           [5, 5, self.height, self.height], 10, width=1,
                           outline="black", fill="#fff")
        self.pack()
