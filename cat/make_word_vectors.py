""" Embedding training
"""
from preprocessing.tokenizers import spacy_split_all
from preprocessing.cleaners import spacy_tag_punct
from preprocessing.spelling import CustomSpellChecker, SpacySpellChecker
from preprocessing.spacy_pipe import SpacyPipe
from preprocessing.iterators import EmbMimicCSV
from gensim.models import Word2Vec
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class WordEmbedding(object):
    """ Calculate word embeddings for a dataset
    """
    def __init__(self):
        self.model = None


    def make_vectors(self, iter_data):
        self.model = Word2Vec(iter_data, window=10, min_count=20, workers=8, size=300, iter=2)