from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from trainer import Trainer
from harvard_src.trainingin import InferenceEngine
import logging
from harvard_src.utils import logger
from harvard_src.processing.preprocessor import Preprocessor
from harvard_src.utils.util import get_config

app = FastAPI()

data_path=get_config('path','product_dataset_path')
preprocessor=Preprocessor()
product_df=preprocessor.load_data(data_path)

class Query(BaseModel):
    """
    A Pydantic model that defines the structure of the query request.
    It expects a string text which will be used to search for top products.
    """
    text: str


# Initialize the Inference Engine
try:
    inference_engine = InferenceEngine()
    logging.info("Inference engine initialized successfully.")
except Exception as e:
    logging.error(f"Failed to initialize the inference engine: {e}")
    raise

@app.post("/search/")
async def search(query: Query):
    """
    FastAPI endpoint to search for top N products based on the query text.
    This function uses the InferenceEngine to find and return the most relevant products.

    Args:
    query (Query): A Pydantic model that takes a single 'text' attribute.

    Returns:
    dict: A dictionary list of the top N products matching the query.
    """
    try:
        logging.info(f"Searching for top products for query: {query.text}")
        top_products = inference_engine.get_top_products(query.text, product_df, top_n=10)
        product_list = top_products.to_dict(orient='records')  # Converts DataFrame to list of dicts
        logging.info(f"Search successful for query: {query.text}")
        return product_list
    except Exception as e:
        logging.error(f"Search failed for query '{query.text}': {e}")
