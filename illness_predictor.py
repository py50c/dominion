import os
import google.generativeai as genai
genai.configure(api_key="AIzaSyBw9SjE2EFS_-cFUIR6bXCTbQ5LD9_QZYk")
# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.7,
  "top_k": 40,
  "max_output_tokens": 2000,
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
 generation_config=generation_config,
  system_instruction="You are an illness predictor, and your job is to generate a list of possible illnesses from the symptoms passed to you.\ninput would be passed as a string but you should return output as plain text.\n\nmake sure the possible illness you give are close enough to the symptoms\nAlso ask further questions like a doctor that would help narrow down what the illness is \nmake your resonse not more than 60 words, give possible illness then ask precise questions to get the accurate illness like a doctor would\n",
)
chat_session = model.start_chat(
  history=[
  ]
)
response = chat_session.send_message("I am having a stomach pain and headach")
user_input = input("enter your symptoms? ")
response = chat_session.send_message(user_input)
print(response.text)



response = chat_session.send_message(user_input)
print(response.text)
patience_input2 = input()
response = chat_session.					send_message(patience_input2)
print(response.text)



patience_input3 = input()
response = chat_session.send_message(patience_input3)
print(response.text)
patience_input4 = input()
response = chat_session.send_message(patience_input2)
print(response.text)


	
	
