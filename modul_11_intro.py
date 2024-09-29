from pprint import pprint

def introspection_info(obj):
    type_ = type(obj).__name__
    # attribute = getattr(obj, '__dir__')
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    module = obj.__class__.__module__
    info = {'type': type_, 'attributes': attributes, 'methods': methods, 'module': module}
    return info

number_info = introspection_info(42)
# print(number_info)
pprint(number_info)