from langchain_community.document_loaders import CSVLoader as csv_loader

loader = csv_loader(file_path = 'daily_routine.csv')

docs = loader.load()

print(docs[0].page_content)

print(docs[0].metadata)

print(type(docs))
print(len(docs))

# In this way we can extract data from 'csv' file with help of 'csv_loader' in Langchain
# we can seperately extract the metadata and page_content of docs object
