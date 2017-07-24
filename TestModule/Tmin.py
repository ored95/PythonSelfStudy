def Tmin(arg0, *args):
    _min = arg0
    for arg in args:
        if arg < _min:
            _min = arg
    return _min
