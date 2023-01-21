class BaseTableException(Exception):
    pass


class NotEnoughSeats(BaseTableException):
    def __init__(self):
        super().__init__("not enough seats ")


class AlreadyReserved(BaseTableException):
    def __init__(self):
        super().__init__("table already reserved")


class ReleaseException(BaseTableException):
    def __init__(self):
        super().__init__("table already released")
