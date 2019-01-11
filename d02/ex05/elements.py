from elem import Elem, Text


class Html(Elem):
    def __init__(self, content=None):
        super(Html, self).__init__(tag="html", content=content)


class Head(Elem):
    def __init__(self, content=None):
        super(Head, self).__init__(tag="head", content=content)


class Body(Elem):
    def __init__(self, content=None):
        super(Body, self).__init__(tag="body", content=content)


class Title(Elem):
    def __init__(self, content=None):
        super(Title, self).__init__(tag="title", content=content)


class Meta(Elem):
    def __init__(self, attr={}):
        super(Meta, self).__init__(tag="meta", attr=attr, tag_type='simple')


class Img(Elem):
    def __init__(self, attr={}):
        super(Img, self).__init__(tag="img", attr=attr, tag_type='simple')


class Table(Elem):
    def __init__(self, attr={}, content=None):
        super(Table, self).__init__(tag="table", attr=attr, content=content)


class Th(Elem):
    def __init__(self, attr={}, content=None):
        super(Th, self).__init__(tag="th", attr=attr, content=content)


class Tr(Elem):
    def __init__(self, attr={}, content=None):
        super(Tr, self).__init__(tag="tr", attr=attr, content=content)


class Td(Elem):
    def __init__(self, attr={}, content=None):
        super(Td, self).__init__(tag="td", attr=attr, content=content)


class Ol(Elem):
    def __init__(self, attr={}, content=None):
        super(Ol, self).__init__(tag="ol", attr=attr, content=content)


class Ul(Elem):
    def __init__(self, attr={}, content=None):
        super(Ul, self).__init__(tag="ul", attr=attr, content=content)


class Li(Elem):
    def __init__(self, attr={}, content=None):
        super(Li, self).__init__(tag="li", attr=attr, content=content)


class H1(Elem):
    def __init__(self, attr={}, content=None):
        super(H1, self).__init__(tag="h1", attr=attr, content=content)


class H2(Elem):
    def __init__(self, attr={}, content=None):
        super(H2, self).__init__(tag="h2", attr=attr, content=content)


class P(Elem):
    def __init__(self, attr={}, content=None):
        super(P, self).__init__(tag="p", attr=attr, content=content)


class Div(Elem):
    def __init__(self, attr={}, content=None):
        super(Div, self).__init__(tag="div", attr=attr, content=content)


class Span(Elem):
    def __init__(self, attr={}, content=None):
        super(Span, self).__init__(tag="span", attr=attr, content=content)


class Hr(Elem):
    def __init__(self, attr={}):
        super(Hr, self).__init__(tag="hr", attr=attr, tag_type='simple')


class Br(Elem):
    def __init__(self):
        super(Br, self).__init__(tag="br", tag_type='simple')


if __name__ == "__main__":
    print(Html([Head(Title(Text("Hello ground!"))), Body([H1(content=Text("Oh no, not again!")),\
                                                    Img({'src': "http://i.imgur.com/pfp3T.jpg" })])]))
