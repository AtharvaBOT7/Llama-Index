# from llama_index.readers.web.beautiful_soup_web.base import BeautifulSoupWebReader
# from llama_index.llms.openai import OpenAI
# from llama_index.core import VectorStoreIndex
# import llama_index
# import os
# from dotenv import load_dotenv

# load_dotenv()

# def main(url: str) -> None:
#     document = BeautifulSoupWebReader(html_to_text=True).load_data(urls=[url])
#     index = VectorStoreIndex.from_documents(documents=document)
#     query_engine = index.as_query_engine()
#     response = query_engine.query("What is history of generative AI?")
#     print(response)

# if __name__ == "__main__":
#     main(url = "https://medium.com/@social_65128/the-comprehensive-guide-to-understanding-generative-ai-c06bbf259786")

from llama_index.readers.web.beautiful_soup_web.base import BeautifulSoupWebReader
from llama_index.llms.openai import OpenAI
from llama_index.core import VectorStoreIndex
import os
from dotenv import load_dotenv

load_dotenv()

def main(url: str) -> None:
    document = BeautifulSoupWebReader().load_data(urls=[url])
    index = VectorStoreIndex.from_documents(documents=document)
    query_engine = index.as_query_engine()
    response = query_engine.query("What is history of generative AI?")
    print(response)

if __name__ == "__main__":
    main(url="https://medium.com/@social_65128/the-comprehensive-guide-to-understanding-generative-ai-c06bbf259786")
