import streamlit as st
import pickle
import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Load the saved model
model_filename = "bert_model.pkl"
with open(model_filename, "rb") as file:
    model = pickle.load(file)

# Load the tokenizer (ensure you use the same tokenizer as during training)
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Define a function for making predictions
def predict(text):
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=1).item()
    return predictions

# Streamlit UI
st.title("BERT Text Classification")
st.write("Enter a sentence below to get a prediction:")

user_input = st.text_area("Enter text here", "")
if st.button("Predict"):
    if user_input.strip():
        prediction = predict(user_input)
        st.write(f"Prediction: {'Positive' if prediction == 1 else 'Negative'}")
    else:
        st.write("Please enter some text for prediction.")