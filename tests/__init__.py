import sys
import os
import logging


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
import example
import etl
import batch_infer

logging.getLogger().setLevel(logging.ERROR)
logging.basicConfig(
    filename="log.log",
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
