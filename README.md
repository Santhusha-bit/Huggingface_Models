# 🤗 Huggingface_Models

A collection of ready-to-use Hugging Face Transformer models and usage examples, showcasing text, vision, and audio pipelines for easy experimentation and prototyping.

---

## 📦 Contents

- `simpleMain.py` – Pre-downloaded or referenced Hugging Face model checkpoints  
- `complexmain.py` – Python scripts demonstrating how to use each model  
- `requirements.txt` – Python dependencies  

---

## 🚀 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/Santhusha-bit/Huggingface_Models.git
cd Huggingface_Models
pip install -r requirements.txt
````

(Optional) Use a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate 
pip install -r requirements.txt
```

---

## 🧪 Usage Examples

Each example shows how to use a model via Hugging Face pipelines.

### Text Generation

```bash
python simpleMain.py \
  --Topic: 
  --Age: 
```

### Text Summarizer + Question answering

```bash
python complexMain.py \
  --Enter text to summarize: 
  --Enter the length (short/medium/long):
  --Ask a question about the summary (or type 'exit' to stop)

```

---

## 🔧 Customization

You can change model identifiers to any compatible Hugging Face model, such as:

* `"facebook/bart-large-cnn"` for summarization
* `"facebook/bart-large"` for refinement
* `"deepset/roberta-base-squad2"` for question answering 
* * `"mistralai/Mistral-7B-Instruct-v0.1"` for text generation

---

## 🧠 Contributions

Contributions are welcome! You can:

* Add more task examples (e.g., translation, feature extraction, text classification)
* Add support for multi-modal tasks
* Submit issues and pull requests to improve this repo

---

## 📚 Resources

* [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers)
* [Hugging Face Model Hub](https://huggingface.co/models)

---

## 🙋 About

Maintained by [Santhusha Mudannayaka](https://github.com/Santhusha-bit)

Explore, learn, and build with transformers!
