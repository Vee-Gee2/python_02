def a(func):
    def wrapped():
        return "<a>" + func() + "</a>"
    return wrapped


def div(func):
    def wrapped():
        return "<div>" + func() + "</div>"
    return wrapped


def p(func):
    def wrapped():
        return "<p>" + func() + "</p>"
    return wrapped


def set_text(func):
    def wrapped():
        func()
        return 'Hello'
    return wrapped
@a
@div
@p
@set_text
def data():
    return 'Something important'


print(data())