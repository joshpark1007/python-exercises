import sys
import os
import pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from series import Series


class TestSeriesInit:
    def test_series_is_list_subclass(self):
        s = Series([1, 2, 3])
        assert isinstance(s, list)

    def test_series_empty_initialization(self):
        s = Series()
        assert len(s) == 0

    def test_series_initialization_with_values(self):
        s = Series([1, 2, 3, 4])
        assert len(s) == 4
        assert s[0] == 1


class TestSeriesSum:
    def test_sum_returns_sum_of_values(self):
        s = Series([1, 2, 3, 4])
        result = s.sum()
        assert result == 10

    def test_sum_with_floats(self):
        s = Series([1.5, 2.5, 3.0])
        result = s.sum()
        assert result == 7.0


class TestSeriesAverage:
    def test_average_calculates_mean(self):
        s = Series([10, 20, 30])
        result = s.average()
        assert result == 20

    def test_avg_alias_exists(self):
        s = Series([10, 20, 30])
        assert hasattr(s, 'avg')
        assert s.avg == s.average


class TestSeriesApply:
    def test_apply_transforms_values(self):
        s = Series([1, 2, 3])
        result = s.apply(lambda x: x * 2)
        assert isinstance(result, Series)
        # Note: The apply method has a bug - it reassigns self but doesn't modify in place
        # This test documents current behavior
        assert list(result) == [2, 4, 6]

    def test_apply_with_string_function(self):
        s = Series(['hello', 'world'])
        result = s.apply(str.upper)
        assert 'HELLO' in result
        assert 'WORLD' in result

    def test_apply_with_complex_function(self):
        s = Series([1, 2, 3, 4])
        result = s.apply(lambda x: x ** 2)
        assert list(result) == [1, 4, 9, 16]


class TestSeriesListMethods:
    def test_append_works(self):
        s = Series([1, 2, 3])
        s.append(4)
        assert len(s) == 4
        assert s[-1] == 4

    def test_indexing_works(self):
        s = Series(['a', 'b', 'c'])
        assert s[0] == 'a'
        assert s[-1] == 'c'

    def test_slicing_works(self):
        s = Series([1, 2, 3, 4, 5])
        subset = s[1:3]
        assert subset == [2, 3]

    def test_iteration_works(self):
        s = Series([1, 2, 3])
        result = [x * 2 for x in s]
        assert result == [2, 4, 6]