# -*- coding: utf-8 -*-
from dotenv import load_dotenv
import gradio as gr
import os
import openai

load_dotenv()

openai.api_key = "api-key yaz"

start_sequence = "\nAI:" 
restart_sequence = "\ninsan: "

prompt ="Здравствуйте, я бот, \nсозданный Хадиджой. Спросите меня что угодно, \nно учтите, что я могу допустить ошибки в ответах."

def openai_create(prompt):
    if "кто тебя изобрел" in prompt.lower():
        return "Меня изобрела Хадиджа Тарвердиева, в 2023 году"
    elif "who invented you" in prompt.lower():
        return "I was invented by Khadija Tarverdiyeva, in 2023"
    else:
        response = openai.Completion.create(
#max_tokens negeder soz deye bilerdi
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=200,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Insan:", " AI:"]
    )

    return response.choices[0].text

def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    if "кто тебя изобрел" in input.lower():
        output = openai_create(input)
        history.append((input, output))
        return history, history
    output = openai_create(input)
    history.append((input, output))
    return history, history
#history yatda saxlasin deyedi

block = gr.Blocks()


with block:
    gr.Markdown("""<h1><center>made in Xenjer</center></h1>""")
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("Göndər")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(share=True)