import pytest


class TestString:
    def test_plus_concats_strings(self):
        str1 = 'he'
        str2 = 'llo'
        result = 'hello'
        assert str1 + str2 == result

    @pytest.mark.parametrize('string,result,deli', [
        ('', [], None),
        ('hello world', ['hello', 'world'], None),
        ('h e l l o\nw o r l d', ['h e l l o', 'w o r l d'], '\n'),
    ])
    def test_string_split(self, string, result, deli):
        l = string.split(deli) if deli else string.split()
        assert l == result

    def test_string_change_not_allowed(self):
        string = 'abd'
        with pytest.raises(TypeError):
            string[2] = 'c'


class TestInt:
    def test_int_to_string(self):
        assert str(-123) == '-123'

    @pytest.mark.parametrize('integer,result', [
        (-1, 1),
        (0, 0),
        (1, 1),
    ])
    def test_abs(self, integer, result):
        assert abs(integer) == result

    def test_negative_shift_not_allowed(self):
        with pytest.raises(ValueError):
            1 << -1
