
from jltools import Dataset
from jltools.packages.sqlitedict import SqliteDict

SINGLE_ROW = [
    '{"k1": "v11", "k2": "v12"}',
]

DUPLICATED_ROWS = [
    '{"k1": "v11", "k2": "v12"}',
    '{"k1": "v11", "k2": "v12"}',
]

ROWS = [
    '{"k1": "v11", "k2": "v12"}',
    '{"k1": "v21", "k2": "v22"}',
    '{"k1": "v31", "k2": "v32"}',
    '{"k1": "v41", "k2": "v42"}',
    '{"k1": "v51", "k2": "v52"}',
]

def test_dataset_create():

    ds = Dataset(SINGLE_ROW)
    assert isinstance(ds, Dataset)


def test_dataset_scan():

    ds = Dataset(SINGLE_ROW)
    assert list(ds.scan()) == [(0, {'k1':'v11','k2':'v12'})]


def test_dataset_scan_for_empty_row():

    ds = Dataset(["",])
    assert list(ds.scan()) == []


def test_dataset_get_by():

    ds = Dataset(ROWS)
    assert ds.get_by(1) == {"k1": "v21", "k2": "v22"}


def test_dataset_index_by():

    ds = Dataset(ROWS)
    ds.index_by('k1')

    assert isinstance(ds.index('k1'), SqliteDict)
    assert ds.index('k1').items() == [
        ('v11', [0]), ('v21',[1]), ('v31',[2]), ('v41',[3]), ('v51',[4])
    ]

def test_dataset_index_by_second_attempt():

    ds = Dataset(ROWS)
    ds.index_by('k1')
    assert ds.index('k1').items() == [
        ('v11', [0]), ('v21',[1]), ('v31',[2]), ('v41',[3]), ('v51',[4])
    ]
    ds.index_by('k1')
    assert ds.index('k1').items() == [
        ('v11', [0]), ('v21',[1]), ('v31',[2]), ('v41',[3]), ('v51',[4])
    ]

def test_dataset_index_by_duplicated_rows():

    ds = Dataset(DUPLICATED_ROWS)
    ds.index_by('k1')
    assert ds.index('k1').items() == [('v11', [0,1]),]
