import builtins
import functools
import json

orig_print = builtins.print


def indent4(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        print('')
        return f(json.dumps(*args, **kwargs, indent=4))

    return wrapped

@indent4
def print_(*args, **kwargs):
    return orig_print(*args, **kwargs)

class CheckClassIncaps:

    def __init__(self) -> None:
        self.test_ver = 0

    @property
    def value_2 (self):
        print('***property_operation***')
        return self.test_ver

    @value_2.setter
    def value_2 (self, n_val):
        self.test_ver = n_val
        print('***setter_operation***')

instance_my = CheckClassIncaps()

print_(instance_my.value_2)

print_(instance_my.test_ver)
instance_my.value_2 = 2
print_(instance_my.value_2)
print_(instance_my.test_ver)





