import importlib.metadata
import pathlib

import anywidget
import traitlets

try:
    __version__ = importlib.metadata.version("ipykonva")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"


class Konva(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "static" / "widget.js"
    _css = pathlib.Path(__file__).parent / "static" / "widget.css"
    color = traitlets.Unicode("#FFD700").tag(sync=True)