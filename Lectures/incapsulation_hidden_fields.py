class Secret:
    public_field = 'this is public'
    _private_field = 'avoid using this please'
    __real_secret = 'I am hidden'

s = Secret()
print(s.public_field)           # this is public
print(s._private_field)         # avoid using this please
print(s._Secret__real_secret)   # I am hidden