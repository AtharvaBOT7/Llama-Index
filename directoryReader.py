from llama_index.readers.file.base import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
import os
from dotenv import load_dotenv
import logging
import sys

load_dotenv()

