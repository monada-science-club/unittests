from unittest.mock import MagicMock, patch, call

from application import generators as GENERATORS


@patch.object(GENERATORS, 'ascii_uppercase', 1)
@patch.object(GENERATORS, 'ascii_lowercase', 2)
def test_generate_random_image():

    GENERATORS.randint = MagicMock(return_value=3)
    GENERATORS.Image.new = MagicMock(return_value=4)
    GENERATORS.choice = MagicMock(return_value=5)

    result_of_the_call_GENERATORS_str_method = MagicMock()
    GENERATORS.str = MagicMock(return_value=result_of_the_call_GENERATORS_str_method)
    result_of_the_call_GENERATORS_str_method.join = MagicMock(return_value=6)

    GENERATORS.ImageFont.truetype = MagicMock(return_value=7)

    result_of_the_call_GENERATORS_ImageDraw_Draw_method = MagicMock()
    GENERATORS.ImageDraw.Draw = MagicMock(return_value=result_of_the_call_GENERATORS_ImageDraw_Draw_method)
    result_of_the_call_GENERATORS_ImageDraw_Draw_method.text = MagicMock()

    counter = 0
    for image in GENERATORS.generate_random_image():

        assert image == 4

        assert GENERATORS.randint.call_count == 10
        expected_calls_for_GENERATORS_randint = [call(0, 255), call(0, 255), call(0, 255), call(100, 300),
                                                 call(100, 300), call(1, 15), call(10, 20), call(0, 255),
                                                 call(0, 255), call(0, 255)]
        assert GENERATORS.randint.call_args_list == expected_calls_for_GENERATORS_randint
        GENERATORS.randint.reset_mock()

        GENERATORS.Image.new.assert_called_once_with('RGB', (3, 3), color=(3, 3, 3))
        GENERATORS.Image.new.reset_mock()

        assert GENERATORS.choice.call_count == 3
        expected_calls_for_GENERATORS_choice = [call(1)] + 2 * [call(2)]
        assert GENERATORS.choice.call_args_list == expected_calls_for_GENERATORS_choice
        GENERATORS.choice.reset_mock()

        assert GENERATORS.str.call_count == 1
        assert result_of_the_call_GENERATORS_str_method.join.call_count == 1
        expected_calls_for_result_of_the_call_GENERATORS_str_method_join = [call(2 * [5])]
        assert result_of_the_call_GENERATORS_str_method.join.call_args_list == expected_calls_for_result_of_the_call_GENERATORS_str_method_join
        GENERATORS.str.reset_mock()
        result_of_the_call_GENERATORS_str_method.join.reset_mock()

        GENERATORS.ImageFont.truetype.assert_called_once_with("arial.ttf", 3)
        GENERATORS.ImageFont.truetype.reset_mock()

        GENERATORS.ImageDraw.Draw.assert_called_once_with(4)
        result_of_the_call_GENERATORS_ImageDraw_Draw_method.text.assert_called_once_with((0, 0), 5 + 6, fill=(3, 3, 3),
                                                                                         font=7)
        GENERATORS.ImageDraw.Draw.reset_mock()
        result_of_the_call_GENERATORS_ImageDraw_Draw_method.text.reset_mock()

        counter += 1
        if counter == 3:
            break


def test_yield_file_lines():

    result_of_the_call_GENERATORS_open_method = MagicMock()
    GENERATORS.open = MagicMock(return_value=result_of_the_call_GENERATORS_open_method)

    result_of_the_call_GENERATORS_read_method = MagicMock()
    result_of_the_call_GENERATORS_open_method.read = MagicMock(return_value=result_of_the_call_GENERATORS_read_method)

    sample_line_of_the_specified_file = MagicMock()
    result_of_the_call_GENERATORS_read_method.split = MagicMock(
        return_value=[sample_line_of_the_specified_file, sample_line_of_the_specified_file])
    sample_line_of_the_specified_file.capitalize = MagicMock(return_value=1)

    expected_result_of_the_yield_file_lines_function_call = [1, 1]
    received_result = [line for line in GENERATORS.yield_file_lines(2)]
    assert expected_result_of_the_yield_file_lines_function_call == received_result

    GENERATORS.open.assert_called_once_with(2, 'r')

    assert result_of_the_call_GENERATORS_open_method.read.call_count == 1

    result_of_the_call_GENERATORS_read_method.split.assert_called_once_with('\n')

    assert sample_line_of_the_specified_file.capitalize.call_count == len(
        expected_result_of_the_yield_file_lines_function_call)
