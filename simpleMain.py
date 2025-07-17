from transformers.pipelines import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain.prompts import PromptTemplate

# import torch

# Check of the GPU is available
# print(torch.cuda.is_available())
# print(torch.cuda.get_device_name(0))

model = pipeline(task="text-generation", 
                model="mistralai/Mistral-7B-Instruct-v0.1", 
                device="cpu",
                max_length=256,
                truncation=True)


llm = HuggingFacePipeline(pipeline=model)

# Create prompt template
template = PromptTemplate.from_template("Explain {topic} in detail for a {age} year old to understand")

chain = template | llm
topic = input("Topic: ")
age = input("Age: ")

# Execute the chain
response = chain.invoke({"topic": topic, "age": age})
print(response)
