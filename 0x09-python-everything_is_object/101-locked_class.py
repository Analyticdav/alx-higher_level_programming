LockedClass:
    def __setattr__(self, name, value):
        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError("Cannot create instance")
