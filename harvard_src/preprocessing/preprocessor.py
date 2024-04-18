from harvard_src.utils import logger
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
# Download stopwords from NLTK
nltk.download('stopwords')

class Preprocessor:
    def __init__(self, config):
        # Initialize the preprocessor with a configuration dictionary.
        self.config = config
        logger.info("Preprocessor initialized with configuration.")

    def load_data(self, filepath):
        """
        Load the dataset into a pandas DataFrame.
        Parameters:
            file_path: str
                The path to the Excel file.
        Returns:
            pd.DataFrame: The loaded data.
        """
        try:
            df = pd.read_csv(filepath)
            logger.info(f"Data loaded successfully from {filepath}")
            return df
        except Exception as e:
            logger.error(f"Failed to load data from {filepath}: {e}")
            raise

    def handle_nulls(self, df):
        # Fill any missing values in the DataFrame with empty strings.
        try:
            df.fillna('', inplace=True)
            logger.info("Missing values filled with empty strings.")
            return df
        except Exception as e:
            logger.error(f"Data cleaning failed: {e}")
            raise

    def preprocess_text(self, text):
        """
        Preprocesses text by combining, lowercasing, removing numbers, punctuations, and extra spaces.

        Args:
            df (pandas.DataFrame): DataFrame with text data.
            text (str): text description

        Returns:
            pandas.DataFrame: The DataFrame with processed text.
        """
        try:
            # Convert text to lowercase.
            processed_text = text.lower()
            # Remove punctuation.
            processed_text = re.sub(r'[^\w\s]', '', processed_text)
            # Remove stopwords.
            stop_words = set(stopwords.words('english'))
            processed_text = ' '.join([word for word in processed_text.split() if word not in stop_words])
            logger.debug(f"Processed text: {processed_text}")
            return processed_text
        except Exception as e:
            logger.error(f"Text preprocessing failed: {e}")
            raise

    def transform_data(self, df):
        # Apply preprocessing to each relevant column of the DataFrame.
        try:
            # Apply text preprocessing to 'product_description' column.
            df['product_description'] = df['product_description'].apply(self.preprocess_text)
            logger.info("Data transformation completed.")
            return df
        except Exception as e:
            logger.error(f"Data transformation failed: {e}")
            raise

    
