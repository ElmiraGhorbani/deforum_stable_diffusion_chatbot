import os

import openai
from langchain import OpenAI
from llama_index import (GPTVectorStoreIndex, LLMPredictor, PromptHelper,
                         SimpleDirectoryReader)


class DocIndexer:
    def __init__(self, root_path):
        """
        this function is used to initialize the class
        """
        self.root_path = root_path
        self.data_path = f'{self.root_path}/resource/data/deforum'

    def construct_index_runner(self):
        """
        this function is used to construct the index for the custom dataset using llama index library
        :return: None
        """
        # set model name
        model_name = os.getenv("EMBEDDING_MODEL", "text-davinci-002")

        # set maximum input size
        max_input_size = 4096
        # set number of output tokens
        num_outputs = 700
        # set maximum chunk overlap
        max_chunk_overlap = 0.5
        # set chunk size limit
        chunk_size_limit = 600

        # define language model predictor for the index
        llm_predictor = LLMPredictor(
            llm=OpenAI(
                temperature=0,
                model_name=model_name,
                max_tokens=num_outputs
            )
        )
        # define prompt helper for the index
        prompt_helper = PromptHelper(
            max_input_size,
            num_outputs,
            max_chunk_overlap,
            chunk_size_limit=chunk_size_limit
        )
        # load data from the directory
        documents = SimpleDirectoryReader(self.data_path).load_data()
        # construct index
        index = GPTVectorStoreIndex.from_documents(
            documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper
        )
        # persist index
        index.storage_context.persist(f'{self.root_path}/storage_deforum')
