import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV
import pickle
from harvard_src.utils import logger  # Importing the custom logger
from harvard_src.processing.preprocessor import Preprocessor
from harvard_src.utils.util import get_config

class Trainer:
    def __init__(self):
        """ Initialize the Trainer with no vectorizer or matrix set up. """
        self.vectorizer = None
        self.tfidf_matrix = None
        self.preprocessor=Preprocessor()
    
    def fit(self, combined_text):
        """
        Fit the TF-IDF vectorizer to the combined text with hyperparameter tuning.

        Parameters:
        combined_text (pd.Series): Combined text data to vectorize.
        """
        # Define the parameter grid for hyperparameter tuning of the TF-IDF vectorizer
        parameters = {
            'max_df': (0.5, 0.75, 1.0),
            'min_df': (1, 2, 3),
            'ngram_range': ((1, 1), (1, 2)),  # testing both unigrams and bigrams
        }

        logger.info("Initializing the TF-IDF vectorizer for hyperparameter tuning.")
        tfidf = TfidfVectorizer()

        try:
            # Use GridSearchCV to find the best parameters for the vectorizer
            grid_search = GridSearchCV(tfidf, param_grid=parameters, n_jobs=-1, cv=5, verbose=1)
            grid_search.fit(combined_text)

            # Retrieve the best TF-IDF vectorizer
            self.vectorizer = grid_search.best_estimator_
            self.tfidf_matrix = self.vectorizer.transform(combined_text)
            logger.info("TF-IDF vectorizer fitted successfully with the best parameters.")

        except Exception as e:
            logger.error(f"Failed during the TF-IDF fitting process: {e}")
            raise
    
    def save_model(self):
        try:
            vector_path=get_config('paths', 'model_path')
            matrix_path=get_config('paths', 'matrix_path')
            with open(vector_path, 'wb') as f:
                pickle.dump(self.vectorizer, f)
            with open(matrix_path, 'wb') as f:
                pickle.dump(self.tfidf_matrix, f)
            logger.info(f"Model saved successfully")
        except Exception as e:
            logger.error(f"Error saving the model: {e}")
            raise

    def trigger_pipeline(self, data_path):
        try:
            logger.info("Embeding creation process started.")
            df = self.preprocessor.load_data(data_path)
            df = self.preprocessor.preprocess_text(df)
            df = self.preprocessor.remove_stop_words(df)
            self.fit(df['combined_text'])
            self.save_model()
            logger.info("Embedings successufly created and saved")
            return evaluation_results
        except Exception as e:
            logger.error(f"Error in train and evaluate process: {e}")
            raise

if __name__ == "__main__":
    product_data_path = get_config('paths', 'train_set_path')
    trainer = Trainer()
    evaluation_results = trainer.trigger_pipeline(product_data_path)
