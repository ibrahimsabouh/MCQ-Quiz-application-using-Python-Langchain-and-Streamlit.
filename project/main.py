import streamlit as st
import helper as hl

st.title("MCQ (multiple-choice question)")

category = st.text_area("What do you want the topic of your quiz about?", max_chars=15)
questions = st.number_input("Enter the number of questions:", step=1, min_value=1, max_value=10)
submit = st.button("Show Questions")

if submit == True and category != "":
    response = hl.generate_Quiz(category, questions)
    st.text(response["question_format"])

elif submit == True and category == "":
    st.error("Please enter a topic before showing the questions.")
