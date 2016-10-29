

import json

from packages.sqlitedict import SqliteDict


class Dataset(object):
    ''' JSONLine dataset
    '''

    def __init__(self, rows):

        self._rows = rows
        self._idxs = dict()


    def scan(self):
        ''' scan dataset

        yeild row as dictionary
        '''
        for i, row in enumerate(self._rows):
            if not row:
                continue

            yield i, json.loads(row)


    def get_by(self, row_id):
        ''' return row by id
        '''
        return json.loads(self._rows[row_id])


    def index(self, fieldname):
        ''' return reference to index for specific field name
        '''
        return self._idxs.get(fieldname, None)


    def index_by(self, fieldname):
        ''' index dataset by fieldname
        '''
        if fieldname in self._idxs:
            return

        self._idxs[fieldname] = SqliteDict()

        for i, row in self.scan():
            if fieldname in row.keys():
                value = row[fieldname]

                row_idxs = self._idxs[fieldname].get(value)
                if row_idxs:
                    row_idxs.append(i)
                    self._idxs[fieldname][value] = row_idxs
                else:
                    self._idxs[fieldname][value] = [i,]
