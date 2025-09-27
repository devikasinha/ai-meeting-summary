# main.py

import os
from groq import Groq 
from dotenv import load_dotenv
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from deepgram import DeepgramClient, PrerecordedOptions 

# Load environment variables from the .env file
load_dotenv()

# --- API KEY CONFIGURATION ---
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY") 

# Initialize the FastAPI app
app = FastAPI()

# --- CORS Middleware ---
origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://127.0.0.1:5500",
    "null"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the MOM Generator Backend!"}

@app.post("/transcribe")
async def transcribe_video(file: UploadFile = File(...)):
    # --- 1. TRANSCRIPTION WITH DEEPGRAM ---
    try:
        deepgram = DeepgramClient(DEEPGRAM_API_KEY)
        video_data = await file.read()
        payload = {"buffer": video_data}
        options = PrerecordedOptions(model="nova-2", smart_format=True)
        
        print("Sending audio to Deepgram for transcription...")
        dg_response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
        transcript = dg_response.results.channels[0].alternatives[0].transcript
        print("Transcription successful.")
    except Exception as e:
        print(f"Deepgram Error: {e}")
        raise HTTPException(status_code=500, detail="Failed to transcribe video.")

    # --- 2. MOM GENERATION WITH GROQ ---
    if not transcript:
        return {"transcript": "Could not generate a transcript.", "mom": "MOM generation failed because the transcript was empty."}
        
    try:
        print("Sending transcript to Groq for MOM generation...")
        client = Groq(api_key=GROQ_API_KEY)

        prompt = f"""
        Based on the following meeting transcript, please generate the Minutes of Meeting (MOM).
        The MOM should be well-structured and include these sections:
        - **Attendees:** (If not mentioned, write 'Not specified in transcript')
        - **Key Discussions:** (Provide a summary of the main topics discussed)
        - **Decisions:** (List any clear decisions that were made)
        - **Action Items:** (List all tasks assigned to individuals, including who is responsible)

        Here is the transcript:
        ---
        {transcript}
        ---
        """
        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            # --- USING A CONFIRMED MODEL FROM YOUR LIST ---
            model="llama-3.1-8b-instant", 
        )
        
        mom = chat_completion.choices[0].message.content
        print("MOM generation successful with Groq.")

    except Exception as e:
        print(f"Groq Error: {e}")
        mom = "Could not generate MOM due to an error with the AI model."
    
    # --- 3. RETURN BOTH RESULTS ---
    return {"transcript": transcript, "mom": mom}