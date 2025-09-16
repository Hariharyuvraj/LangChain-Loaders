from langchain_community.document_loaders import TextLoader
loader = TextLoader('cricket.txt', encoding='utf-8')
docs = loader.load()

print(docs[0].page_content) # we can print 'metadata' and 'page_content' seperatly.

print(docs[0].metadata)

print(type(docs))  # can check 'type' of 'docs'

print(len(docs))   # we can see the 'len' of docs

