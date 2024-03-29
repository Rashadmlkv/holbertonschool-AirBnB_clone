"""
    Base class for all other classes
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ class """

    def __init__(self, *args, **kwargs):
        """ initilize instance """

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    pass
                else:
                    if (key == 'created_at' or key == 'updated_at'):
                        setattr(self, key, datetime.strptime
                                (value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            from . import storage

            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ print formatted """

        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ update updated_at attribute """
        from . import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ convert to dictionary """

        dct = self.__dict__.copy()
        for key, value in dct.items():
            if type(value) is datetime:
                dct[key] = value.isoformat()
        dct['__class__'] = type(self).__name__
        return dct
