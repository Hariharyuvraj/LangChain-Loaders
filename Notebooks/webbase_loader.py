from langchain_community.document_loaders import WebBaseLoader

url = 'https://www.flipkart.com/frontech-ultima-series-55-88-cm-22-inch-full-hd-led-backlit-va-panel-monitor-mon-0079c/p/itm222dc80082352?pid=MONH3H7XYMMSJBCB&lid=LSTMONH3H7XYMMSJBCBCQNQPE&marketplace=FLIPKART&q=monitor&store=6bo%2Fg0i%2F9no&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=6ff45b55-11b0-4a26-afb4-068f48f1bb9a.MONH3H7XYMMSJBCB.SEARCH&ppt=None&ppn=None&ssid=kmctapx41c0000001757125679738&qH=08b5411f848a2581'

loader = WebBaseLoader(url)

docs = loader.load()

print(docs[0].page_content)

print(len(docs[0]))

print(type(docs[0]))

# IN this code we can extract data from "url" with the help of "webBase_loader"
# behind the code it udses "beautifulsoup" library from python
#Need to be install "beautifulsoup"