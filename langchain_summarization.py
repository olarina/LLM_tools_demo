#%%
%pip install --upgrade --quiet  langchain-openai tiktoken chromadb langchain

#%%
import dotenv
import os


openai_api_key_se = os.getenv("OPENAI_API_KEY_SE")
openai_api_base_se = os.getenv("API_BASE_4_SE")

os.environ["AZURE_OPENAI_API_KEY"] = openai_api_key_se
os.environ["AZURE_OPENAI_ENDPOINT"] = openai_api_base_se
# %%
