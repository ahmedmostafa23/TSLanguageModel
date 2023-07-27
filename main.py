from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from TaylorLM import TaylorLM

app = FastAPI()

# this lets the API be accessible from anywhere.
app.add_middleware(
   CORSMiddleware,
   allow_origins=["*"],
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)

model_wrapper = TaylorLM()

@app.get("/")
def home():
    print("home json requested")
    return {"Welcome": "Welcome to my bad taylor language model!"}
    
@app.get("/{sentence}")
def finish_sentence(sentence: str):
    print(f"finish sentence '{sentence}' requested")
    global model_wrapper
    finished = model_wrapper.finish_sentence(sentence)
    return {sentence: finished}

# the `uvicorn.run()` function is used to start the application
# and the `host` parameter is set to `"0.0.0.0"`, which binds to all available network interfaces
# thus allowing the application to be accessible from outsite the container and not just the container's own loopback.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
