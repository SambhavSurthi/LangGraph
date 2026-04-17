# import all the necessary libraries

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from pydantic import BaseModel,Field
from dotenv import load_dotenv
from typing import TypedDict,Optional,Literal,List,Annotated
import operator

from langgraph.graph import StateGraph,START,END

load_dotenv()


# define the State for the graph

class AgentState(TypedDict):
    user_query:str
    enhanced_query:str
    classify_query:Literal['technical','informational','Analytical']
    research_response:Annotated[List[str],operator.add]
    example_response:Annotated[List[str],operator.add]
    summary_response:Annotated[List[str],operator.add]
    final_response:Annotated[List[str],operator.add]
    evaluator_response:Annotated[List[Literal['approved','need_improvement']],operator.add]
    iteration:1
    
    
    
# define required objects for the classes
