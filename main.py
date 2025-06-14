import os
from routellm.controller import Controller
from routellm.openai_server import create_app  # Changed from direct app import
import uvicorn

# Create FastAPI app with router configuration
app = create_app(
    routers=["mf"],  # Explicitly enable MF router
    strong_model="openai/gpt-4",
    weak_model="groq/llama3-8b-8192"
)

# Initialize controller with proper environment variables
@app.on_event("startup")
async def initialize_controller():
    # Get API keys from Railway environment variables
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY", "")
    
    # Initialize controller and attach to app state
    app.state.controller = Controller(
        routers=["mf"],
        strong_model="openai/gpt-4",
        weak_model="groq/llama3-8b-8192"
    )

# Add health check endpoint
@app.get("/health")
async def health_check():
    return {
        "status": "ready",
        "routers": ["mf"],
        "models": ["gpt-4", "llama3-8b-8192"]
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)

