import nbformat

def create_notebook(file_name, explanation, imports, code, pros_cons, application):
    # Create a new notebook
    notebook = nbformat.v4.new_notebook()

    # Add cells
    notebook.cells.append(nbformat.v4.new_markdown_cell(explanation))
    notebook.cells.append(nbformat.v4.new_code_cell(imports))
    notebook.cells.append(nbformat.v4.new_code_cell(code))
    notebook.cells.append(nbformat.v4.new_markdown_cell(pros_cons))
    notebook.cells.append(nbformat.v4.new_markdown_cell(application))

    # Write the notebook to a file
    with open(file_name, 'w') as f:
        nbformat.write(notebook, f)

# Define content for each notebook
notebooks = [
    {
        "file_name": "INTRO.ipynb",
        "explanation": "# Introduction\nThis notebook explains the importance of tokenization in NLP.",
        "imports": "# No imports required for this notebook.",
        "code": "# No code required for this notebook.",
        "pros_cons": "### Pros and Cons\n- **Pros**: Sets the foundation for understanding tokenization.\n- **Cons**: No practical implementation.",
        "application": "### Applications\n- Understanding the basics of tokenization."
    },
    {
        "file_name": "CHARACTER_LEVEL.ipynb",
        "explanation": "# Character-Level Tokenization\nThis notebook demonstrates character-level tokenization.",
        "imports": "# No external libraries required.",
        "code": "text = \"Tokenization is the process of breaking text into smaller pieces.\"\ntokens = list(text)\nprint(\"Character-level tokens:\", tokens)",
        "pros_cons": "### Pros and Cons\n- **Pros**: Simple and language-agnostic.\n- **Cons**: Results in very large token sequences.",
        "application": "### Applications\n- Useful for languages without clear word boundaries."
    },
    {
        "file_name": "WORD_LEVEL.ipynb",
        "explanation": "# Word-Level Tokenization\nThis notebook demonstrates word-level tokenization.",
        "imports": "import re",
        "code": "text = \"Tokenization is the process of breaking text into smaller pieces.\"\ntokens = re.findall(r'\\b\\w+\\b', text)\nprint(\"Word-level tokens:\", tokens)",
        "pros_cons": "### Pros and Cons\n- **Pros**: Intuitive and easy to implement.\n- **Cons**: Struggles with out-of-vocabulary words.",
        "application": "### Applications\n- Common in traditional NLP pipelines."
    },
    {
        "file_name": "SENTENCE_LEVEL.ipynb",
        "explanation": "# Sentence-Level Tokenization\nThis notebook demonstrates sentence-level tokenization.",
        "imports": "import re",
        "code": "text = \"Tokenization is the first step in NLP. It is important for preprocessing.\"\nsentences = re.split(r'(?<!\\w\\.\\w.)(?<![A-Z][a-z]\\.)(?<=\\.|\\?)\\s', text)\nprint(\"Sentence-level tokens:\", sentences)",
        "pros_cons": "### Pros and Cons\n- **Pros**: Useful for sentence-level analysis.\n- **Cons**: Requires language-specific rules.",
        "application": "### Applications\n- Summarization and translation tasks."
    },
    {
        "file_name": "BERT.ipynb",
        "explanation": "# BERT Tokenization\nThis notebook demonstrates tokenization using the BERT tokenizer.",
        "imports": "from transformers import AutoTokenizer",
        "code": "tokenizer = AutoTokenizer.from_pretrained(\"bert-base-uncased\")\ntext = \"Tokenization is the process of breaking text into smaller pieces.\"\ntokens = tokenizer.tokenize(text)\nprint(\"BERT tokens:\", tokens)",
        "pros_cons": "### Pros and Cons\n- **Pros**: Handles subwords effectively.\n- **Cons**: Requires pre-trained models.",
        "application": "### Applications\n- Preprocessing for BERT-based models."
    },
    {
        "file_name": "T5.ipynb",
        "explanation": "# T5 Tokenization\nThis notebook demonstrates tokenization using the T5 tokenizer.",
        "imports": "from transformers import AutoTokenizer",
        "code": "tokenizer = AutoTokenizer.from_pretrained(\"t5-small\")\ntext = \"Tokenization is the process of breaking text into smaller pieces.\"\ntokens = tokenizer.tokenize(text)\nprint(\"T5 tokens:\", tokens)",
        "pros_cons": "### Pros and Cons\n- **Pros**: Optimized for T5 models.\n- **Cons**: Requires pre-trained models.",
        "application": "### Applications\n- Preprocessing for T5-based models."
    },
    {
        "file_name": "MINILMLL6.ipynb",
        "explanation": "# MiniLM-L6 Tokenization\nThis notebook demonstrates tokenization using the MiniLM-L6 tokenizer.",
        "imports": "from transformers import AutoTokenizer",
        "code": "tokenizer = AutoTokenizer.from_pretrained(\"microsoft/MiniLM-L6-H384-uncased\")\ntext = \"Tokenization is the process of breaking text into smaller pieces.\"\ntokens = tokenizer.tokenize(text)\nprint(\"MiniLM-L6 tokens:\", tokens)",
        "pros_cons": "### Pros and Cons\n- **Pros**: Lightweight and efficient.\n- **Cons**: Limited to specific tasks.",
        "application": "### Applications\n- Preprocessing for MiniLM-based models."
    },
    {
        "file_name": "E5BASE.ipynb",
        "explanation": "# E5-Base Tokenization\nThis notebook demonstrates tokenization using the E5-Base tokenizer.",
        "imports": "from transformers import AutoTokenizer",
        "code": "tokenizer = AutoTokenizer.from_pretrained(\"intfloat/e5-base\")\ntext = \"Tokenization is the process of breaking text into smaller pieces.\"\ntokens = tokenizer.tokenize(text)\nprint(\"E5-Base tokens:\", tokens)",
        "pros_cons": "### Pros and Cons\n- **Pros**: Optimized for embedding tasks.\n- **Cons**: Requires pre-trained models.",
        "application": "### Applications\n- Preprocessing for E5-based models."
    }
]

# Create all notebooks
for notebook in notebooks:
    create_notebook(
        notebook["file_name"],
        notebook["explanation"],
        notebook["imports"],
        notebook["code"],
        notebook["pros_cons"],
        notebook["application"]
    )

print("All notebooks created successfully!")