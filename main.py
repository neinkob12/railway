import os
from routellm.controller import Controller
from routellm.openai_server import app

# Set environment variables (Railway will override these with your actual secrets)
os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY", "")
os.environ["GROQ_API_KEY"] = os.environ.get("GROQ_API_KEY", "")

# Initialize RouteLLM controller
controller = Controller(
    routers=["mf"],
    strong_model="openai/gpt-4",
    weak_model="groq/llama3-8b-8192"
)

# The app variable is imported from routellm.openai_server
# This is a FastAPI application that's already configured to use your controller

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
