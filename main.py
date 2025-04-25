from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Simple API Example")

class InputParams(BaseModel):
    param1: str
    param2: int

class OutputParams(BaseModel):
    result1: str
    result2: int

@app.get("/")
async def root():
    return {"message": "Welcome to Simple API"}    

@app.post("/process", response_model=OutputParams)
async def process_params(input_data: InputParams):
    """
    Process two input parameters and return two output parameters.
    
    Args:
        input_data: InputParams containing param1 (str) and param2 (int)
    
    Returns:
        OutputParams containing result1 (str) and result2 (int)
    """
    # Example processing logic
    result1 = f"Processed {input_data.param1}"
    result2 = input_data.param2 * 2
    
    return OutputParams(result1=result1, result2=result2)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) 