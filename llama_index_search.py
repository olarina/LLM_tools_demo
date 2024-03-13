from llama_index.core.readers.file.base import SimpleDirectoryReader
from llama_index.core.indices.vector_store import VectorStoreIndex
from llama_index.embeddings.azure_openai.base import AzureOpenAIEmbedding
from langchain_openai import AzureChatOpenAI
from llama_index.core import Settings
import dotenv
import os


#%%
# !mkdir -p 'data/paul_graham/'
# !wget 'https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/paul_graham/paul_graham_essay.txt' -O 'data/paul_graham/paul_graham_essay.txt'

#%%
dotenv.load_dotenv(os.path.join("configs", ".env"))

"""
The file /configs/.env should contain:
AZURE_OPENAI_API_KEY = ""
AZURE_OPENAI_ENDPOINT = ""
"""

llm = AzureChatOpenAI(
    temperature=0,
    azure_deployment="gpt-35-turbo-1106",
    openai_api_version="2024-02-15-preview"
)

embed_model = AzureOpenAIEmbedding(
    model="text-embedding-ada-002",
    deployment_name="text-embedding-ada-002",
    api_version="2024-02-15-preview",
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

Settings.llm = llm
Settings.embed_model = embed_model
#%%

documents = SimpleDirectoryReader("data/paul_graham").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)
# %%
