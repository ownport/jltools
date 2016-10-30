
from jltools import join
from jltools import Dataset

from jltools.packages.sqlitedict import SqliteDict


LEFT_ROWS1 = [
    '{"left-k11": "v11", "left-k12": "left-v12", "left-k13": "left-v13", "left-k14": "left-v14"}',
    '{"left-k31": "v31", "left-k32": "left-v32", "left-k33": "left-v33", "left-k34": "left-v34"}',
    '{"left-k21": "v21", "left-k22": "left-v22", "left-k23": "left-v23", "left-k24": "left-v24"}',
    '',
    '{"left-k41": "v41", "left-k42": "left-v42", "left-k43": "left-v43", "left-k44": "left-v44"}',
    '{"left-k41": "v41", "left-k42": "left-v42", "left-k43": "left-v43", "left-k44": "left-v44"}',
]

RIGHT_ROWS1 = [
    '{"right-k11": "v11", "right-k12": "right-v12", "right-k13": "right-v13", "right-k14": "right-v14"}',
    '{"right-k31": "v31", "right-k32": "right-v32", "right-k33": "right-v33", "right-k34": "right-v34"}',
    '{"right-k21": "v21", "right-k22": "right-v22", "right-k23": "right-v23", "right-k24": "right-v24"}',
    '',
    '{"right-k41": "v41", "right-k42": "rightt-v42", "right-k43": "right-v43", "right-k44": "right-v44"}',
    '{"right-k41": "v41", "right-k42": "rightt-v42", "right-k43": "right-v43", "right-k44": "right-v44"}',
]

LEFT_ROWS2 = [
    '{"lk1": "v1", "lk2": "lv2", "lk3": "lv3"}',
    '{"lk1": "v2", "lk2": "lv2", "lk3": "lv3"}',
    '{"lk1": "v3", "lk2": "lv2", "lk3": "lv3"}',
]

RIGHT_ROWS2 = [
    '{"rk1": "v4", "rk2": "rv2", "rk3": "rv3"}',
    '{"rk1": "v2", "rk2": "rv2", "rk3": "rv3"}',
    '{"rk1": "v1", "rk2": "rv2", "rk3": "rv3"}',
]

def test_inner_join():

    ds_left = Dataset(LEFT_ROWS2)
    ds_right = Dataset(RIGHT_ROWS2)

    assert list(join.inner_join(ds_left, 'lk1', ds_right, 'rk1')) == [
        {"lk1": "v1", "lk2": "lv2", "lk3": "lv3", "rk1": "v1", "rk2": "rv2", "rk3": "rv3"},
        {"lk1": "v2", "lk2": "lv2", "lk3": "lv3", "rk1": "v2", "rk2": "rv2", "rk3": "rv3"},
    ]

def test_inner_join_overwrite_values():

    ds_left = Dataset([
        '{"lk1": "v1", "lk2": "lv2", "lk3": "lv3"}',
    ])
    ds_right = Dataset([
        '{"lk1": "v1", "lk2": "lv3", "lk3": "lv4"}',
    ])
    assert list(join.inner_join(ds_left, 'lk1', ds_right, 'lk1')) == [
        {"lk1": "v1", "lk2": "lv3", "lk3": "lv4"}
    ]


def test_full_outer_join():

    ds_left = Dataset(LEFT_ROWS2)
    ds_right = Dataset(RIGHT_ROWS2)

    assert list(join.full_outer_join(ds_left, 'lk1', ds_right, 'rk1')) == [
        {"lk1": "v1", "lk2": "lv2", "lk3": "lv3", "rk1": "v1", "rk2": "rv2", "rk3": "rv3"},
        {"lk1": "v2", "lk2": "lv2", "lk3": "lv3", "rk1": "v2", "rk2": "rv2", "rk3": "rv3"},
        {"lk1": "v3", "lk2": "lv2", "lk3": "lv3"},
        {"rk1": "v4", "rk2": "rv2", "rk3": "rv3"},
    ]

def test_left_outer_join():

    ds_left = Dataset(LEFT_ROWS2)
    ds_right = Dataset(RIGHT_ROWS2)

    assert list(join.left_outer_join(ds_left, 'lk1', ds_right, 'rk1')) == [
        {"lk1": "v1", "lk2": "lv2", "lk3": "lv3", "rk1": "v1", "rk2": "rv2", "rk3": "rv3"},
        {"lk1": "v2", "lk2": "lv2", "lk3": "lv3", "rk1": "v2", "rk2": "rv2", "rk3": "rv3"},
        {"lk1": "v3", "lk2": "lv2", "lk3": "lv3"},
    ]

def test_right_outer_join():

    ds_left = Dataset(LEFT_ROWS2)
    ds_right = Dataset(RIGHT_ROWS2)

    assert list(join.right_outer_join(ds_left, 'lk1', ds_right, 'rk1')) == [
        {"lk1": "v1", "lk2": "lv2", "lk3": "lv3", "rk1": "v1", "rk2": "rv2", "rk3": "rv3"},
        {"lk1": "v2", "lk2": "lv2", "lk3": "lv3", "rk1": "v2", "rk2": "rv2", "rk3": "rv3"},
        {"rk1": "v4", "rk2": "rv2", "rk3": "rv3"},
    ]
