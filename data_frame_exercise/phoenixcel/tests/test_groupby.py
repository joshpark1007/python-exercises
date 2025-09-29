import sys
import os
import pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from groupby import GroupBy
from series import Series


class TestGroupBySum:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.grouped = GroupBy({
            'A': [{'value': 10}, {'value': 20}],
            'B': [{'value': 30}, {'value': 40}]
        })

    def test_sum_aggregates_correctly(self):
        result = self.grouped.sum(on='value')
        assert result['A'] == 30
        assert result['B'] == 70


class TestGroupByAverage:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.grouped = GroupBy({
            'A': [{'value': 10}, {'value': 20}],
            'B': [{'value': 30}, {'value': 40}]
        })

    def test_average_calculates_mean(self):
        result = self.grouped.average(on='value')
        assert result['A'] == 15
        assert result['B'] == 35

    def test_avg_alias_works(self):
        result = self.grouped.avg(on='value')
        assert result['A'] == 15


class TestGroupByCount:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.grouped = GroupBy({
            'A': [{'value': 10}, {'value': 20}],
            'B': [{'value': 30}]
        })

    def test_count_returns_group_sizes(self):
        result = self.grouped.count(on='value')
        assert result['A'] == 2
        assert result['B'] == 1


class TestGroupByMin:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.grouped = GroupBy({
            'A': [{'value': 10}, {'value': 20}],
            'B': [{'value': 30}, {'value': 40}]
        })

    def test_min_returns_minimum_value(self):
        result = self.grouped.min(on='value')
        assert result['A'] == 10
        assert result['B'] == 30


class TestGroupByMax:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.grouped = GroupBy({
            'A': [{'value': 10}, {'value': 20}],
            'B': [{'value': 30}, {'value': 40}]
        })

    def test_max_returns_maximum_value(self):
        result = self.grouped.max(on='value')
        assert result['A'] == 20
        assert result['B'] == 40


class TestGroupBySpread:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.grouped = GroupBy({
            'A': [{'value': 10}, {'value': 20}],
            'B': [{'value': 30}, {'value': 50}]
        })

    def test_spread_calculates_range(self):
        result = self.grouped.spread(on='value')
        assert result['A'] == 10
        assert result['B'] == 20


class TestGroupByAggregate:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.grouped = GroupBy({
            'A': [{'value': 10}, {'value': 20}],
            'B': [{'value': 30}, {'value': 40}]
        })

    def test_aggregate_with_custom_function(self):
        result = self.grouped.aggregate(on='value', using_func=lambda x: sum(x) / len(x))
        assert result['A'] == 15
        assert result['B'] == 35

    def test_aggregate_raises_without_on_parameter(self):
        with pytest.raises(Exception):
            self.grouped.aggregate(using_func=sum)

    def test_aggregate_raises_without_using_func_parameter(self):
        with pytest.raises(Exception):
            self.grouped.aggregate(on='value')


class TestGroupByDescribeWith:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.grouped = GroupBy({
            'A': [{'value': 10}, {'value': 20}],
            'B': [{'value': 30}, {'value': 40}]
        })

    def test_describe_with_multiple_aggregations(self):
        result = self.grouped.describe_with(
            {'agg': 'sum', 'column': 'value'},
            {'agg': 'average', 'column': 'value'}
        )
        assert 'A' in result.keys()
        assert 'B' in result.keys()

    def test_describe_with_custom_function(self):
        def custom_func(values):
            return max(values) - min(values)

        result = self.grouped.describe_with(
            {'agg': 'aggregate', 'column': 'value', 'using_func': custom_func}
        )
        assert isinstance(result, GroupBy)


class TestGroupByPrintCute:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.grouped = GroupBy({
            'A': [{'value': 10}, {'value': 20}],
            'B': [{'value': 30}]
        })

    def test_print_cute_does_not_raise(self):
        # Test that the method runs without error
        try:
            self.grouped.print_cute()
            success = True
        except Exception:
            success = False
        assert success