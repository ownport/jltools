

import json

from dataset import Dataset

from packages.sqlitedict import SqliteDict


def inner_join(ds_left, left_field, ds_right, right_field):
    ''' selects all rows from both datasets (left and right) as long as there
        is a match between the fields in both datasets.

        http://www.w3schools.com/sql/sql_join_inner.asp
    '''
    ds_right.index_by(right_field)

    # find rows which are present in left and right datasets only
    for left_row_id, left_row in ds_left.scan():
        left_field_value = left_row.get(left_field)
        if left_field_value and left_field_value in ds_right.index(right_field):
            for right_row_id in ds_right.index(right_field).get(left_field_value):
                left_row.update(ds_right.get_by(right_row_id))
                yield left_row
        else:
            yield left_row
