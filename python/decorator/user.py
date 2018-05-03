class User(object):

    all_users = set()

    def __init__(self, name, val, is_maker=False):
        self.name = name
        self._is_maker = is_maker
        self.val = val

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_val):
        self._name = new_val

    @property
    def is_maker(self):
        return self._is_maker

    def __str__(self):
        return '%s, with val %2s, status of %7s' % (self.name, self.val, 'maker' if self.is_maker else 'regular')

    @classmethod
    def add_to_database(cls, user):
        if not isinstance(user, User):
            raise TypeError('expected %s got %s' % (User, type(user)))
        cls.all_users.add(user)

    @classmethod
    def get_usernames(cls):
        return [x.name for x in cls.all_users]
