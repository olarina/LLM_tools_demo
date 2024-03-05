#%%
import dotenv
import os
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import AzureChatOpenAI

"""
The file /configs/.env should contain:
AZURE_OPENAI_API_KEY = ""
AZURE_OPENAI_ENDPOINT = ""
"""
dotenv.load_dotenv(os.path.join("configs", ".env"))

loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
docs = loader.load()

llm = AzureChatOpenAI(
    temperature=0,
    azure_deployment="gpt-35-turbo-1106",
    openai_api_version="2024-02-15-preview"
)

chain = load_summarize_chain(llm, chain_type="stuff")

results = chain.run(docs)
print(results)
# %%
