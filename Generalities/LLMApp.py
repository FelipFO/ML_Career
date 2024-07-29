# run the app with the command: streamlit run app_openai.py

import json
import openai
import streamlit as st
import csv


# Carga la clave API desde un archivo JSON
with open('keys.json', 'r') as file:
    config = json.load(file)

API_KEY = config['api_key']

documentation = """
Eres un asistente que nos ayuda a entender la tecnología de Large Language Models. Sos experto en LLM. Respondenos con un tono amigable con la intención de ayudarnos a entender nuestras dudas." 
"""


menu = ["Home", "Documentation", "Contact Us"]
choice = st.sidebar.selectbox("Select an option", menu)
if choice == "Home":
    openai.api_key = API_KEY

    # app UI
    image = "image.jfif"
    st.image(image, width= 300)
    st.title("ChatGPT integration")
    st.header(":genie: ¿Cómo puedo ayudar?")
    text = st.empty()
    prompt = st.text_input("Escribe tu mensaje aquí:", value="Escribe tu mensaje aquí...", label_visibility="collapsed")


    # API request
    response = openai.chat.completions.create(
    model="gpt-4",
    messages=[
            {"role": "system", "content":  documentation},
            {"role": "user", "content": prompt},
        ],
    max_tokens=200
    )

    response = response.choices[0].message.content
    st.markdown(response)

    # save prompts and answers
    csvrow = [prompt,response]
    def append_list_as_row(file_name, list_of_elem):
        # Open file in append mode
        with open(file_name, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = csv.writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(list_of_elem)


    append_list_as_row('historic_prompts.csv', csvrow)




