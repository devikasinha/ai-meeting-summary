# 🤖 Automated Meeting Transcript & MOM Generator

This project is a full-stack web application designed to automate the process of creating Minutes of Meeting (MOM). It takes a video or audio recording of a meeting, generates a full transcript, and then uses a Large Language Model (LLM) to create a structured, editable summary with key discussions, decisions, and action items.

---

### ## ✨ Key Features

-   **Video/Audio Upload**: Simple interface to upload meeting recordings.
-   **AI-Powered Transcription**: Utilizes **Deepgram's** API for fast and accurate speech-to-text conversion.
-   **Automated MOM Generation**: Leverages the **Groq API** with the Llama 3.1 model to intelligently summarize the transcript into a professional MOM format.
-   **Editable Content**: Both the transcript and the generated MOM can be reviewed and manually edited in the browser.
-   **PDF Export**: Download the finalized MOM as a clean, formatted PDF with a single click.

---

### ## 🔧 Tech Stack

-   **Frontend**: HTML, CSS, JavaScript (with `jsPDF` for PDF generation)
-   **Backend**: Python with **FastAPI**
-   **Transcription API**: [Deepgram](https://deepgram.com/)
-   **LLM API**: [Groq](https://groq.com/) (serving Llama 3.1)
-   **Deployment**: Backend on [Render](https://render.com/), Frontend on [Netlify](https://www.netlify.com/).

---

### ## 🚀 Setup & Installation

Follow these steps to run the project locally.

#### Prerequisites

-   Git
-   Python 3.10+
-   A web browser

#### Backend Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd mom-generator-project/backend
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up API Keys:**
    Create a file named `.env` inside the `backend` folder and add your API keys:
    ```
    DEEPGRAM_API_KEY="YOUR_DEEPGRAM_API_KEY"
    GROQ_API_KEY="YOUR_GROQ_API_KEY"
    ```

5.  **Run the server:**
    ```bash
    uvicorn main:app --reload
    ```
    The backend will be running at `http://127.0.0.1:8000`.

#### Frontend Setup

1.  Navigate to the `frontend` folder.
2.  Open the `index.html` file in your web browser.
3.  Ensure the `backendURL` constant in the `<script>` section points to your backend server's address.

---

### ## 🔑 API Keys

This project requires API keys from the following services:

-   **Deepgram**: For speech-to-text transcription. Get your key from the [Deepgram Console](https://console.deepgram.com/).
-   **Groq**: For AI-powered text generation. Get your key from the [Groq Console](https://console.groq.com/).