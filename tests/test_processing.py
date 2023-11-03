import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def test_data():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

def test_filter_by_state(test_data):
    state = "EXECUTED"
    expected_output = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    assert filter_by_state(test_data, state) == expected_output


def test_sort_by_date():
    data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    sorted_data_asc = sort_by_date(data, order="asc")
    assert sorted_data_asc[0]["date"] == "2018-06-30T02:08:58.425572"
    assert sorted_data_asc[-1]["date"] == "2019-07-03T18:35:29.512364"

    sorted_data_desc = sort_by_date(data, order="desc")
    assert sorted_data_desc[0]["date"] == "2019-07-03T18:35:29.512364"
    assert sorted_data_desc[-1]["date"] == "2018-06-30T02:08:58.425572"