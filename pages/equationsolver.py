#Complex Word Math Problem Solver App
import streamlit as st
from langchain import OpenAI, LLMMathChain
from apikey import apikey
import os

os.environ["OPENAI_API_KEY"] = apikey
llm = OpenAI(temperature=0)
llm_math = LLMMathChain.from_llm(llm, verbose=True)


st.title("Complex Word Math Solver")
#input form
query = st.text_input("Enter your Math query:")
execute_button = st.button("Execute")
if execute_button:
    #Perform query and display results
    result = llm_math.run(query)
    st.write("Result:",result)


