from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('ai_note.pdf')

docs = loader.load()

print(docs)

print(len(docs))

print(type(docs))


# in my pdf there is only one page so it shows 1 docs
# every page is converted in to 'document object' It having seperate metadat and page_content
# 'Type' of document is 'list'
# in this loader we can extract the pdf only 
# need to be install "pypdfloader" otherwise codewill not run in vs-code
# we can extract 'metadata', 'page_content' seperatly
## NOTE : In 'pypdf_loader' we can extraxt only texual data not image scaned pdf.