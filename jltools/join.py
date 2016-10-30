

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



def full_outer_join(ds_left, left_field, ds_right, right_field):
    ''' returns all rows from the left dataset and from the right dataset,
        combines the result of both LEFT and RIGHT joins

        http://www.w3schools.com/sql/sql_join_full.asp
    '''
    ds_left.index_by(left_field)
    ds_right.index_by(right_field)

    for left_row_id, left_row in ds_left.scan():
        left_field_value = left_row.get(left_field)
        if left_field_value and left_field_value in ds_right.index(right_field):
            for right_row_id in ds_right.index(right_field).get(left_field_value):
                left_row.update(ds_right.get_by(right_row_id))
                yield left_row
        else:
            yield left_row

    for right_row_id, right_row in ds_right.scan():
        right_field_value = right_row.get(right_field)
        if right_field_value and right_field_value not in ds_left.index(left_field):
            yield right_row
            
