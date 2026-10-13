from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
import re
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


# Initialize FastAPI app
app = FastAPI(
    title="Text Summarization API",
    description="An API for text summarization using T5 model",
    version="1.0.0"
)


# Load model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("./saved_summary_model")
tokenizer = T5Tokenizer.from_pretrained("./saved_summary_model")


# Select device
if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

model.to(device)
model.eval()


# Jinja2 templates
templates = Jinja2Templates(directory=".")


# Input schema
class DialogueInput(BaseModel):
    dialogue: str


# Clean input text
def clean_data(text: str) -> str:
    text = re.sub(r"\r\n", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"<.*?>", " ", text)
    text = text.strip().lower()
    return text


# Summarization function
def summarize_dialogue(dialogue: str) -> str:

    # Clean dialogue
    dialogue = clean_data(dialogue)

    # Tokenize
    inputs = tokenizer(
        dialogue,
        padding="max_length",
        max_length=512,
        truncation=True,
        return_tensors="pt"
    )

    # Move tensors to selected device
    inputs = {key: value.to(device) for key, value in inputs.items()}

    # Generate summary
    with torch.no_grad():
        targets = model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=150,
            num_beams=4,
            early_stopping=True
        )

    # Decode generated tokens
    summary = tokenizer.decode(
        targets[0],
        skip_special_tokens=True
    )

    return summary


# API endpoint
@app.post("/summarize/")
async def summarize(dialogue_input: DialogueInput):
    summary = summarize_dialogue(dialogue_input.dialogue)

    return {
        "summary": summary
    }


# Home page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )
