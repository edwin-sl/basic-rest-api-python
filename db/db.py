from db.users import data as collections_users
from db.todos import data as collections_todos

collections = {
    'users': collections_users,
    'todos': collections_todos
}


def get_last_id(collection):
    data = collections[collection]
    last_obj = data[len(data) - 1] or {'id': 0}
    return last_obj['id']


# representa un SELECT de SQL
def select(collection, select_id=None, filters=dict):
    data = collections[collection]
    if select_id is not None:
        for e in data:
            if e['id'] == select_id:
                return e
    else:
        # [e for e in data if ]

        return data
    return {}


# representa un INSERT de SQL
def insert(collection, new_object):
    last_id = get_last_id(collection)
    new_object['id'] = last_id + 1
    # if(validateObject(object, collections[collection].schema)) {
    collections[collection].append(new_object)
    return new_object
    # }
    # return null


# representa un UPDATE de SQL
def update(collection, new_object):
    update_id = new_object['id']
    data = collections[collection]
    for e in data:
        if e['id'] == update_id:
            e.update(new_object)
            return e
    return {}


# representa un DELETE de SQL
def delete(collection, delete_id):
    data = collections[collection]
    for e in data:
        if e['id'] == delete_id:
            data.remove(e)
            return e
    return {}