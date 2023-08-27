#Complex Word Math Problem Solver App
import streamlit as st
from langchain import OpenAI, LLMMathChain
import os

os.environ["OPENAI_API_KEY"] = "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"
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


