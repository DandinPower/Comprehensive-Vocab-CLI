from rich.console import Console
from rich.markdown import Markdown

class MarkdownViewer:
    console = Console()

    @classmethod
    def view(cls, content: str) -> None:
        print("\n\n\n")
        md = Markdown(content)
        cls.console.print(md)
        print("\n\n\n")