"""
Library to draw a graph onto a pygame screen
"""
import pygame
import random

"""
TO DO:
- Add dual axis line graph
- Add legend
- Add custom axis scale
"""


def line_graph(data, dims, axis_titles=(None, None), custom_margins=None, colours=()):
    """
    Function to draw a line graph on a pygame surface.

    Data is passed in as a list containing lists of x values and y values:
    [[x_1, x_2,..., x_n], [y1_1, y1_2,..., y1_n], [y2_1, y2_2,..., y2_n]]
    If multiple sets of y values are passed in, all lines will be plotted on the same set of axis to the same scale.

    Returns a pygame surface containing the graph.

    :param data:
    :param dims:
    :param axis_titles:
    :param custom_margins:
    :param colours:
    :return graph:
    """
    margins = [10, 10, 10, 10] if custom_margins is None else custom_margins
    if len(colours) == 0:
        colours = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)]
    graph = _draw_axes(dims, axis_titles, margins)

    scale_max_x = max(data[0])
    scale_max_y = max(data[1])
    for i in range(1, len(data)):
        if max(data[i]) > scale_max_y:
            scale_max_y = max(data[i])

    if scale_max_x == 0:
        scale_max_x = 1
    if scale_max_y == 0:
        scale_max_y = 1

    # Add points to graph (scaled to axes)
    for i in range(1, len(data)):
        display_points = []
        for j in range(len(data[0])):
            display_points.append([margins[3]+round(((dims[0]-(margins[3]+margins[1]))*data[0][j])/scale_max_x, 2),
                                   dims[1]-margins[2]-round(((dims[1]-(margins[0]+margins[2]))*data[i][j])/scale_max_y, 2)])
        if i <= len(colours):
            line_colour = colours[i-1]
        else:
            line_colour = _random_colour()

        if len(display_points) > 1:
            pygame.draw.lines(graph, line_colour, False, display_points)

    # Return graph as a surface
    return graph


def _draw_axes(dims, axis_titles=(None, None), margins=None, num_y_axes=1):
    """
    Function to draw the axes of a graph.

    Returns a pygame surface containing the blank axes for the graph.

    :param dims:
    :param axis_titles:
    :param margins:
    :param num_y_axes:
    :return surf:
    """
    surf = pygame.Surface(dims, flags=pygame.SRCALPHA)
    surf.fill((0, 0, 0, 155))

    axis_font = pygame.font.SysFont("Helvetica", 20)

    if axis_titles[0] is not None:
        x_title = axis_font.render(str(axis_titles[0]), False, (255, 255, 255))
        surf.blit(x_title, (((dims[0] / 2) - (x_title.get_width() / 2)), dims[1]-x_title.get_height()))
        margins[2] += x_title.get_height()
    if axis_titles[1] is not None:
        y_title = axis_font.render(str(axis_titles[1]), False, (255, 255, 255))
        y_title = pygame.transform.rotate(y_title, 90)
        surf.blit(y_title, (0, (dims[1]/2)-(y_title.get_height()/2)))
        margins[3] += y_title.get_width()

    # Draw axes
    pygame.draw.line(surf, (255, 255, 255), (margins[3], margins[0]), (margins[3], dims[1] - margins[2]), width=10)
    pygame.draw.line(surf, (255, 255, 255), (margins[3] - 4, dims[1] - margins[2]),
                     (dims[0] - margins[1], dims[1] - margins[2]), width=10)

    return surf


def _random_colour():
    colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    return colour
