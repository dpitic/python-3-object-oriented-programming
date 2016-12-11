from PIL import Image


"""
Demonstration of the strategy pattern.

The strategy pattern is an example of abstraction in OOP. It implements
different solutions in different objects, all having the same abstraction
interface. The client code can choose the most appropriate implementation
dynamically at runtime.

This example implements a desktop wallpaper manager which uses different
strategies to display the image on the desktop background. The strategy objects
accept two inputs, the image to be displayed and a tuple of the width and height
of the display. They each return a new image the size of the screen, with the
image manipulated to fit according to the given strategy.
"""


class TiledStrategy:
    def make_background(self, img_file, desktop_size):
        """
        Tile the image on the screen.
        :param img_file: image to display on the desktop background.
        :param desktop_size: tuple (width, height) of the screen.
        :return: new image corresponding to the size of the screen.
        """
        in_img = Image.open(img_file)
        out_img = Image.new('RGB', desktop_size)
        # Calculate the number of input images that would fit over the width
        # height of the screen.
        num_tiles = [
            o // i + 1 for o, i in zip(out_img.size, in_img.size)
        ]
        # Copy the image into each tiled location.
        for x in range(num_tiles[0]):
            for y in range(num_tiles[1]):
                out_img.paste(
                    in_img,
                    (
                        in_img.size[0] * x,
                        in_img.size[1] * y,
                        in_img.size[0] * (x + 1),
                        in_img.size[1] * (y + 1)
                    )
                )
        return out_img


class CentredStrategy:
    def make_background(self, img_file, desktop_size):
        """
        Centre the image on the screen.
        :param img_file: image to display on the desktop background.
        :param desktop_size: tuple (width, height) of the screen.
        :return: new image corresponding to the size of the screen.
        """
        in_img = Image.open(img_file)
        out_img = Image.new('RGB', desktop_size)
        # Calculate the top left location in order to centre the image on the
        # screen.
        left = (out_img.size[0] - in_img.size[0]) // 2
        top = (out_img.size[1] - in_img.size[1]) // 2
        out_img.paste(
            in_img,
            (
                left,
                top,
                left + in_img.size[0],
                top + in_img.size[1]
            )
        )
        return out_img


class ScaledStrategy:
    """
    Scale the image on the screen.
    :param img_file: image to display on the desktop background.
    :param desktop_size: tuple (width, height) of the screen.
    :return: new image corresponding to the size of the screen.
    """
    def make_background(self, img_file, desktop_size):
        in_img = Image.open(img_file)
        # Scale the image to the desktop size; ignoring image aspect ratio.
        out_img = in_img.resize(desktop_size)
        return out_img


# Demonstrate the API
def main():
    img_filename = 'Benson.jpg'
    desktop_size = (1024, 768)
    # List of tuples containing strategy objects and corresponding output files
    strategies = [
        (TiledStrategy(), 'tiled.jpg'),
        (CentredStrategy(), 'centred.jpg'),
        (ScaledStrategy(), 'scaled.jpg')
    ]
    # Create output files based on the strategies.
    for strategy, filename in strategies:
        image = strategy.make_background(img_filename, desktop_size)
        try:
            image.save(filename)
        except IOError:
            print('Error saving the file {}'.format(filename))


if __name__ == '__main__':
    main()
