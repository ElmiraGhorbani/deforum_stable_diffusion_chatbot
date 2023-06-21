"""
this script is used to create an API Deforum for the chatbot
"""
import asyncio
import os

import openai
from fastapi import FastAPI, HTTPException

from .create_index import DocIndexer
from .retriever import Retriever
from .utils import check_if_file_exists, get_project_root

# set openai api key for llama index to work
KEY = os.getenv("OPENAI_API_KEY",
                "")
openai.api_key = KEY
os.environ["OPENAI_API_KEY"] = KEY


root_path = get_project_root()

indexer = DocIndexer(root_path=root_path)

if not check_if_file_exists():
    indexer.construct_index_runner()

query_engine = Retriever(root_path=root_path)

app = FastAPI()


def ask_runner(question):
    """
    this function is used to run the ask function
    :param question: question from the user
    :return: answer from the index
    """
    return query_engine.find_answer(question)


@app.post("/ask")
async def ask(
    question: str = "",
):
    """
    This endpoint is used to question the index for the custom dataset.
    :param question: question from the user
    :return: answer from the index
    """
    try:
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            ask_runner,
            question,
        )
        result = {"bot_response": response,
                  "status": "success", "you_asked": f"{question}"}
        return result
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"{e}")
