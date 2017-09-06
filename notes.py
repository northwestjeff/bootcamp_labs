# def make_html(tag, contents):
#     return "<{0}> {1} </{0}>".format(tag, contents)
#     #return "<i> stuff </i>
#
# print(make_html("i", "cats are cool!"))


def print_msg(msg):

    def printer():
        print(msg)
    printer()


print_msg("Hello world.")