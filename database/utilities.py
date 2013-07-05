def get_or_create(sess, model, **kwargs):
    instance = sess.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        sess.add(instance)
        return instance

