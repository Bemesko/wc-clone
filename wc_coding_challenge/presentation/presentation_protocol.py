from typing import Protocol, Any

class PresentationProtocol(Protocol):
    def get_arguments(self, arguments: list[str]) -> None:
        ...

    def show(self, result: Any) -> None:
        ...