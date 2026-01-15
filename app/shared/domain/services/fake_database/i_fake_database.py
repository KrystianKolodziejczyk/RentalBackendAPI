from abc import ABC, abstractmethod


class IFakeDatabase(ABC):
    @abstractmethod
    def get_json_list(path) -> list[dict]: ...

    @abstractmethod
    def save_json_list(path) -> None: ...
