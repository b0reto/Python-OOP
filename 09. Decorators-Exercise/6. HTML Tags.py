def tags (t):
    def add_tag (f):
        def wrapper (*args):
            return f"<{t}>{f(*args)}</{t}>"
        return wrapper
    return add_tag