from llama_index import (ResponseSynthesizer, StorageContext,
                         load_index_from_storage)
from llama_index.indices.postprocessor import SimilarityPostprocessor
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.retrievers import VectorIndexRetriever


class Retriever:
    """
    this class is used to create an API for custom gpt indexer
    """

    def __init__(self, root_path) -> None:
        """
        this function is used to initialize the class
        """
        index_path = f'{root_path}/storage_deforum'
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_path))

        # configure retriever
        retriever = VectorIndexRetriever(
            index=index,
            similarity_top_k=2,
        )

        # configure response synthesizer
        response_synthesizer = ResponseSynthesizer.from_args(
            node_postprocessors=[
                SimilarityPostprocessor(similarity_cutoff=0.65)
            ]
        )

        # assemble query engine
        self.query_engine = RetrieverQueryEngine(
            retriever=retriever,
            response_synthesizer=response_synthesizer,
        )

    def find_answer(self, question):
        """
        this function is used to find the answer from the index
        :param question: question from the user
        :return: answer from the index
        """
        response = self.query_engine.query(question)
        return response.response
