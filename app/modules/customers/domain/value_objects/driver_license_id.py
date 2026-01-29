class DriverLicenseId:
    _value: str

    def __init__(self, value: str) -> None:
        if len(value) != 16:
            raise Exception

        self._value = value

    @property
    def value(self) -> str:
        return self._value
