from abc import ABC, abstractmethod
from pathlib import Path

from enums import ExtensionToSave


class BaseExtractor(ABC):
    @abstractmethod
    def extract(self, source: Path, target: Path, extension_to_save: ExtensionToSave) -> None:
        ...