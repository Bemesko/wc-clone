from typing import Callable, Any

class CommandLineInterface():

    def get_arguments(self, arguments: list[str]) -> None:
        ...

    def show(self, result: Any) -> None:
        print(result)