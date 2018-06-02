from random import randint, choice
from string import ascii_lowercase

from PIL import Image, ImageDraw, ImageFont

def capitalize_sting(string):
    """
    Arguments:
        string - string provided by the user
    Returns:
         capitalized string
    """
    return string.capitalize()

def get_random_string(number_of_characters, signs):
    """
        This function creates a capitalized string with a specified length (number_of_characters),
        consisting of signs from the provided string (signs)
    """

    random_string = ''
    for i in range(number_of_characters):
        random_string += choice(signs)

    random_string = capitalize_sting(random_string)
    return random_string


def generate_random_image(rand_func=randint, string_func=get_random_string, signs_of_string=ascii_lowercase):
    """
        The function generates an image with random color and shape, then
        generates a string that has between 1 and 15 characters.
        All letters of the string are randomly selected, string begins with an upper letter.
        Color and font size of the string are random.
        Generated string is saved on the image.
    """

    while True:
        # Based on the basic colors, generate a random color of the image
        red_color = rand_func(0, 255)
        green_color = rand_func(0, 255)
        blue_color = rand_func(0, 255)

        # Generate a random size of the image
        # The width and height range is between 100 and 300 pixels.
        width = rand_func(100, 300)
        height = rand_func(100, 300)

        image = Image.new('RGB', (width, height), color=(red_color, green_color, blue_color))

        # Generate the length of the string
        number_of_string_characters = rand_func(1, 15)

        # Generate random string
        string_inside_image = string_func(number_of_string_characters, signs_of_string)

        # Generate a random font size of the string
        # The string font size range is between 10 and 20 points.
        string_font_size = rand_func(10, 20)
        font = ImageFont.truetype("arial.ttf", string_font_size)

        #  Based on the basic colors, generate a random color of the string
        image_red_color = rand_func(0, 255)
        image_green_color = rand_func(0, 255)
        image_blue_color = rand_func(0, 255)

        add_text_to_an_image = ImageDraw.Draw(image)
        add_text_to_an_image.text((0, 0), string_inside_image,
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
        result = capitalize_sting(line)
        yield result
