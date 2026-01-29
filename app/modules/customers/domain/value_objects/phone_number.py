class PhoneNumber:
    def __init__(self, value: str) -> None:
        if not value.isdigit() or len(value) != 9:
            raise Exception

        self._value = value

    def __str__(self):
        return self._value

    @property
    def value(self) -> str:
        return self._value
