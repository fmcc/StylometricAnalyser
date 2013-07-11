from log import log
def get_or_create(sess, model, **kwargs):
    instance = sess.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        sess.add(instance)
        return instance
"""
Ensure a consistent ordering of section objects.
"""
def order_sections(id_one, id_two):
    if id_one > id_two:
        id_one, id_two = id_two, id_one
        return id_one, id_two
    return id_one, id_two

