from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1254670588.7820139
_template_filename='/home/iekhingthio/pylons_pet_project/HelloWorld/helloworld/templates/welcome.mako'
_template_uri='/welcome.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = ['head_tags']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n<h1>My Controller</h1>\n\n<p>\n\n')
        # SOURCE LINE 11
        if c.loginStatus:
            # SOURCE LINE 12
            __M_writer(u'\twelcome ')
            __M_writer(unicode(c.userId))
            __M_writer(u'!!!!\t\n')
            # SOURCE LINE 13
        else:
            # SOURCE LINE 14
            __M_writer(u'\tfailed to login\t\t\t\t\t\n')
        # SOURCE LINE 16
        __M_writer(u'\n\t\t\n\n</p>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n  <!-- add some head tags here -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


