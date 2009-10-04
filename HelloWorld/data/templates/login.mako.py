from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1254670587.1819761
_template_filename='/home/iekhingthio/pylons_pet_project/HelloWorld/helloworld/templates/login.mako'
_template_uri='/login.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">\n<html><head>\n<meta content="text/html; charset=ISO-8859-1" http-equiv="content-type"><title>login</title>\n</head>\n  <body>\n    <form method="post" action="/login/verify" name="login">\n\t<label> User id :</label> \n\t<input name="userId">\n  \t<br/>\n        <label>password :</label>\n\t <input name="password" type="password">\n\t <br><input type="submit" value="Send me your name!"><br>\n    </form>\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


