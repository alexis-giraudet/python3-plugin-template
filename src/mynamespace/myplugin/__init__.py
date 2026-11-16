from mynamespace.myproject import AbstractDisplay

__version__ = "1.0.0"


class DisplayExcl(AbstractDisplay):
    @property
    def version(self) -> str:
        return __version__

    def display(self, text: str) -> None:
        print(f"!!!{text}!!!")
