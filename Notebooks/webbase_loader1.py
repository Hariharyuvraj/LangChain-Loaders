from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY='Paste your openai api key'

model = ChatOpenAI(model = 'gpt-4-turbo', api_key = OPENAI_API_KEY)

prompt = PromptTemplate(
    template='answer the following question \n {question} from the following text \n {text}',
    input_variables=['question', 'text']
)

parser = StrOutputParser

url = 'https://www.flipkart.com/frontech-ultima-series-55-88-cm-22-inch-full-hd-led-backlit-va-panel-monitor-mon-0079c/p/itm222dc80082352?pid=MONH3H7XYMMSJBCB&lid=LSTMONH3H7XYMMSJBCBCQNQPE&marketplace=FLIPKART&q=monitor&store=6bo%2Fg0i%2F9no&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=6ff45b55-11b0-4a26-afb4-068f48f1bb9a.MONH3H7XYMMSJBCB.SEARCH&ppt=None&ppn=None&ssid=kmctapx41c0000001757125679738&qH=08b5411f848a2581'

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'question': 'what is product we are talking about?', 'text':docs[0].page_content}))

# in this code we can extract the data using "webbase_loader" but we can make model to interact wit model
