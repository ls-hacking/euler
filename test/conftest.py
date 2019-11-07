import os
import sys


source_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        os.pardir,
    )
)
if source_path not in sys.path:
    sys.path.insert(0, source_path)
