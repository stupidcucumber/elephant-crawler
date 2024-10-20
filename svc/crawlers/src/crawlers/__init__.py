import importlib
import importlib.util
import inspect
from pathlib import Path

from src.crawlers.base import BaseCrawler

__all__ = [BaseCrawler]


for module_name in (path.stem for path in Path("src/crawlers").glob("*.py")):

    if module_name != "__init__":

        module = importlib.import_module(name=f"src.crawlers.{module_name}")

        crawlers = []
        for value in module.__dict__.values():
            if (
                inspect.isclass(value)
                and issubclass(value, BaseCrawler)
                and value != BaseCrawler
            ):
                __all__.append(value)
