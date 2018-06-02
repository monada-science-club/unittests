from unittest.mock import MagicMock, patch, call

from application import generators as GENERATORS


@patch.object(GENERATORS, 'ImageDraw')
@patch.object(GENERATORS, 'ImageFont')
@patch.object(GENERATORS, 'Image')
def test_generate_random_image(image_func, imagefont_func, imagedraw_func):

    rand_func = MagicMock(return_value=1)
    string_func = MagicMock(return_value=2)
    signs_of_string = 'a'

    image_func.new = MagicMock(return_value=3)
    imagefont_func.truetype = MagicMock(return_value=4)

    result_imagedraw_draw = MagicMock()
    imagedraw_func.Draw = MagicMock(return_value=result_imagedraw_draw)
    result_imagedraw_draw.text = MagicMock()

    expected_result = 3
    counter = 0
    for image in GENERATORS.generate_random_image(rand_func, string_func, signs_of_string):

        recived_result = image
        assert expected_result == recived_result
        counter += 1
        if counter == 3:
            break

    assert rand_func.call_count == 3 * 10

    assert image_func.new.call_count == 3
    assert image_func.new.call_args_list == 3 * [call('RGB', (1, 1), color=(1, 1, 1))]

    assert string_func.call_count == 3
    assert string_func.call_args_list == 3 * [call(1, 'a')]

    assert imagefont_func.truetype.call_count == 3
    assert imagefont_func.truetype.call_args_list == 3 * [call("arial.ttf", 1)]

    assert imagedraw_func.Draw.call_count == 3
    assert imagedraw_func.Draw.call_args_list == 3 * [call(3)]

    assert result_imagedraw_draw.text.call_count == 3
    assert result_imagedraw_draw.text.call_args_list == 3 * [call((0, 0), 2, fill=(1, 1, 1), font=4)]


@patch.object(GENERATORS, "capitalize_sting")
@patch.object(GENERATORS, "open")
def test_yield_file_lines(open_method, capitalize_method):

    result_open = MagicMock()
    open_method.return_value = result_open

    result_read = MagicMock()
    result_open.read = MagicMock(return_value=result_read)

    result_read.split = MagicMock(return_value=['a', 'a'])
    capitalize_method.return_value = 1

    expected_result = [1, 1]
    received_result = [line for line in GENERATORS.yield_file_lines(2)]
    assert expected_result == received_result

    open_method.assert_called_once_with(2, 'r')

    assert result_open.read.call_count == 1

    result_read.split.assert_called_once_with('\n')

    assert capitalize_method.call_count == 2
    assert capitalize_method.call_args_list == 2 * [call('a')]


@patch.object(GENERATORS, "capitalize_sting")
@patch.object(GENERATORS, "choice")
def test_get_random_string(choice_method, capitalize_method):

    number_of_characters = 2
    signs_of_string = 'abc'
    choice_method.return_value = 'a'

    capitalize_method.return_value = 1

    expected_result = 1
    recived_result = GENERATORS.get_random_string(number_of_characters, signs_of_string)
    assert expected_result == recived_result

    assert choice_method.call_count == 2
    assert choice_method.call_args_list == 2 * [call('abc')]

    capitalize_method.assert_called_once_with('aa')


def test_capitalize_string():

    argument = MagicMock()
    argument.capitalize = MagicMock(return_value=1)

    expected_result = 1
    recived_result = GENERATORS.capitalize_sting(argument)
    assert expected_result == recived_result

    argument.capitalize.assert_called_once_with()
