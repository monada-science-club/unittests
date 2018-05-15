from random import randint, choice
from string import ascii_uppercase, ascii_lowercase

from PIL import Image, ImageDraw, ImageFont


def generate_random_image():
    """
        The function generates an image with random color and shape, then
        generates a string that has between 1 and 15 characters.
        All letters of the string are randomly selected, string begins with an upper letter.
        Color and font size of the string are random.
        Generated string is saved on the image.
    """

    while True:
        # Based on the basic colors, generate a random color of the image
        red_color = randint(0, 255)
        green_color = randint(0, 255)
        blue_color = randint(0, 255)

        # Generate a random size of the image
        # The width and height range is between 100 and 300 pixels.
        width = randint(100, 300)
        height = randint(100, 300)

        image = Image.new('RGB', (width, height), color=(red_color, green_color, blue_color))

        # Generate the length of the string
        number_of_string_characters = randint(1, 15)

        # Choose random string letters
        first_upper_letter = choice(ascii_uppercase)
        lower_letters = str().join([choice(ascii_lowercase) for i in range(1, number_of_string_characters)])

        # Generate a random font size of the string
        # The string font size range is between 10 and 20 points.
        string_font_size = randint(10, 20)
        font = ImageFont.truetype("arial.ttf", string_font_size)

        #  Based on the basic colors, generate a random color of the string
        image_red_color = randint(0, 255)
        image_green_color = randint(0, 255)
        image_blue_color = randint(0, 255)

        add_text_to_an_image = ImageDraw.Draw(image)
        add_text_to_an_image.text((0, 0), first_upper_letter + lower_letters,
                                  fill=(image_red_color, image_green_color, image_blue_color), font=font)

        yield image


def yield_file_lines(path_to_file):
    """
    Arguments:
        path_to_file (string): path to the text file
    Yields:
        capitalized individual lines of the specified file
    """
    lines = open(path_to_file, 'r').read().split('\n')
    for line in lines:
        line = line.capitalize()
        yield line
