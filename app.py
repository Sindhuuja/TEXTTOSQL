import os
import sqlite3
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()  # Load all the environment variables

# Configure API key for Google Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini model and provide query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])
    return response.text


# Function to retrieve query from the SQL database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    
    for row in rows:
        print(row)
    
    return rows


# Define your prompt
prompt = [
    """
    You are an AI assistant. Respond to questions based on the following SQL database structure. The user will provide queries, and you will extract the appropriate data from the database.
    """
]

# Streamlit app UI code
st.title("Google Gemini AI with SQL Query")
st.write("Ask a question, and the AI will answer based on the database.")

question = st.text_input("Enter your question:")

if question:
    response = get_gemini_response(question, prompt)
    st.write(f"Response: {response}")


# Example of SQL query execution
query = "SELECT * FROM users"
database = "your_database.db"
sql_result = read_sql_query(query, database)
st.write("SQL Query Result:", sql_result)


