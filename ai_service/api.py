"""FastAPI application for math problem solving service.

This module provides a REST API endpoint for solving math problems
from text or image inputs.
"""
from typing import Optional

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from ai_service import solve_math_problem

app = FastAPI(title="Math Solver API")

# WARNING: Allow all origins is not secure for production.
# In production, replace "*" with specific allowed origins.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Restrict to specific origins in production
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/solve")
async def solve(
    text: Optional[str] = Form(None), image: Optional[UploadFile] = File(None)
) -> dict[str, str]:
    """Solve a math problem from text or image input.

    Args:
        text: Optional text description of the math problem.
        image: Optional image file containing the math problem.

    Returns:
        dict: Dictionary containing the solution.

    Raises:
        HTTPException: If neither text nor image is provided.
    """
    if not text and not image:
        raise HTTPException(
            status_code=400, detail="Cần cung cấp đề bài dạng chữ hoặc ảnh."
        )

    image_data = None
    if image:
        image_data = await image.read()

    solution = solve_math_problem(text, image_data)
    return {"solution": solution}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)