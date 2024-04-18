import pickle
from sklearn.metrics.pairwise import cosine_similarity
from harvard_src.utils import logger

class InferenceEngine:
    def __init__(self, vectorizer_path='tfidf_vectorizer.pkl', matrix_path='tfidf_matrix.pkl'):
        """Initialize the Inference Engine by loading the TF-IDF vectorizer and matrix."""
        try:
            with open(vectorizer_path, 'rb') as f:
                self.vectorizer = pickle.load(f)
                logger.info(f"Vectorizer loaded successfully from {vectorizer_path}.")
            with open(matrix_path, 'rb') as f:
                self.tfidf_matrix = pickle.load(f)
                logger.info(f"TF-IDF matrix loaded successfully from {matrix_path}.")
        except FileNotFoundError as e:
            logger.error(f"File not found: {e}")
            raise
        except Exception as e:
            logger.error(f"An error occurred while loading the model: {e}")
            raise

    def get_top_products(self, query, product_df, top_n=10):
        """Retrieve top N products for a given query based on TF-IDF similarity."""
        try:
            query_vector = self.vectorizer.transform([query])
            cosine_similarities = cosine_similarity(query_vector, self.tfidf_matrix).flatten()
            top_product_indices = cosine_similarities.argsort()[-top_n:][::-1]
            top_products = product_df.iloc[top_product_indices]
            logger.info(f"Top products retrieved successfully for query: {query}")
            return top_products
        except Exception as e:
            logger.error(f"Error during product retrieval for query '{query}': {e}")
            raise

