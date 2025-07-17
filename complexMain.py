from huggingface_hub.inference._generated.types import summarization
from transformers.pipelines import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from transformers.utils.logging import set_verbosity_error

set_verbosity_error()

summarization_pipeline = pipeline(task="summarization", model="facebook/bart-large-cnn", device="cpu")
summarizer = HuggingFacePipeline(pipeline=summarization_pipeline)

refinement_pipeline = pipeline(task="summarization", model="facebook/bart-large", device="cpu")
refiner = HuggingFacePipeline(pipeline=refinement_pipeline)

qa_pipeline = pipeline(task="question-answering", model="deepset/roberta-base-squad2", device="cpu")

summary_template = PromptTemplate.from_template("Summarize the following text in a {length} way:\n\n{text}")

summarization_chain = summary_template | summarizer | refiner

text_to_summerize = input("\nEnter text to summarize:\n")

length = input("\nEnter the length (short/medium/long): ")
length_map = {"short": 50, "medium": 150, "long": 300}
max_length = length_map.get(length.lower(), 150)

summary = summarization_chain.invoke({"text": text_to_summerize, "length": max_length})

print("\n ** Generate Summary **")
print(summary)

while True:
    question = input("\nAsk a question about the summary (or type 'exit' to stop):\n")
    if question.lower() == exit:
        break

    qa_result = qa_pipeline(question=question, context=summary)

    print("\n ** Answer **")
    print(qa_result["answer"])