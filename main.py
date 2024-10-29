import inspect


def introspection_info(obj):
    info = {
        'Type': type(obj).__name__,
        'Attributes': [attr for attr in dir(obj) if not attr.startswith('__')],
        'Methods': [func for func in dir(obj) if callable(getattr(obj, func)) and not func.startswith('__')],
        'Module': inspect.getmodule(obj).__name__ if inspect.ismodule(inspect.getmodule(obj)) else None,
    }

    if isinstance(obj, dict):
        info['Keys'] = list(obj.keys())
    elif isinstance(obj, (list, tuple, set)):
        info['Length'] = len(obj)
    elif hasattr(obj, 'shape'):
        info['Shape'] = obj.shape

    return info


number_info = introspection_info(42)
print(number_info)