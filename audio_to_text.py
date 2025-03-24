from fastapi import FastAPI, File, UploadFile
import whisper
import os

app = FastAPI()

# Load Whisper Model (use "base" or change as needed)
model = whisper.load_model("base")

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Transcribe audio
    result = model.transcribe(file_path)
    os.remove(file_path)  # Clean up temp file

    return {"text": result["text"]}
