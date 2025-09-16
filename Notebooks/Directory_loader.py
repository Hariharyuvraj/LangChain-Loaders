from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
    path ='books',
    glob = '*.pdf',
    loader_cls= PyPDFLoader
)

docs = loader.load()

print(len(docs))

print(type(docs)) 

# BY using the "Directoryloader" we can extract many pdf from folder
# In this code we have 1 pdf, but we can extract many pdf
