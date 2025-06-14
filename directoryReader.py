from urllib import response
from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
import os
from dotenv import load_dotenv
import logging
import sys

load_dotenv()

def main(url: str) -> None:
    documents = SimpleDirectoryReader(url).load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    response = query_engine.query("What is this research paper trying to convey, please summarise.")
    print(response)

if __name__ == "__main__":
    main(url="/Users/atharva7/Downloads/Llama Index/data")