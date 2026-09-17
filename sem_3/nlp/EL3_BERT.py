"""
============================================================
BERT CONTEXTUAL WORD EMBEDDINGS - BEGINNER NOTES + CODE
============================================================

WHAT ARE WE LEARNING?
---------------------
This program teaches us how to use BERT to create
CONTEXTUAL WORD EMBEDDINGS.

Example:

    "I deposited money in the bank."
    "I sat near the bank of the river."

The word "bank" appears in both sentences, but its meaning
is different.

BERT understands the surrounding words and therefore gives
the word "bank" a context-dependent representation.

This is the main idea we are learning.

============================================================
1. WHAT IS NLP?
============================================================

NLP = Natural Language Processing.

NLP is a branch of Artificial Intelligence that helps
computers work with human language.

Examples:
    - Sentiment analysis
    - Text classification
    - Machine translation
    - Chatbots
    - Question answering
    - Named Entity Recognition
    - Text summarization
    - Search engines

A computer cannot directly understand a sentence as humans do.
Therefore, text is converted into numerical representations.

That is where TOKENIZATION and EMBEDDINGS become important.

============================================================
2. WHAT IS AN EMBEDDING?
============================================================

An embedding is a numerical representation of text.

For example, conceptually:

    "king" -> [0.21, -0.52, 0.73, 0.11, ...]

The numbers are called a VECTOR.

A vector is simply a list of numbers.

Machine learning models can work with these numerical
representations much more easily than raw text.

============================================================
3. STATIC VS CONTEXTUAL EMBEDDINGS
============================================================

Older word-embedding techniques such as Word2Vec generally
give a word one learned representation.

For example:

    bank -> Vector A

But the word "bank" can have multiple meanings.

    "I deposited money in the bank."
                        ^
                        financial institution

    "I sat near the bank of the river."
                     ^
                     side of a river

BERT creates CONTEXTUAL representations.

Therefore:

    bank + financial context -> Representation A
    bank + river context     -> Representation B

The same word can therefore have different representations
depending on the surrounding words.

============================================================
4. WHAT IS BERT?
============================================================

BERT stands for:

    Bidirectional Encoder Representations from Transformers

BERT is a pre-trained language model developed by Google.

The important word here is BIDIRECTIONAL.

BERT considers context from both directions.

For example:

    The bank is near the river.

BERT uses information from words before and after "bank"
to build its representation.

BERT is based on the TRANSFORMER encoder architecture.

============================================================
5. WHAT IS HUGGING FACE?
============================================================

Hugging Face is an organization and platform that provides
tools and pre-trained machine-learning models.

For NLP, one of its most important libraries is:

    transformers

The Transformers library lets us easily use models such as:

    - BERT
    - RoBERTa
    - DistilBERT
    - GPT-family models
    - T5
    - and many others

Instead of implementing BERT from scratch, we can download
a pre-trained BERT model and use it directly.

============================================================
6. WHAT IS "bert-base-uncased"?
============================================================

We use:

    "bert-base-uncased"

This identifies a particular pre-trained BERT model.

    bert       -> model family
    base       -> base-sized BERT
    uncased    -> does not distinguish uppercase/lowercase

For example:

    "BANK"
    "Bank"
    "bank"

are treated without case distinction by an uncased tokenizer.

============================================================
7. INSTALLATION
============================================================

Install the required libraries:

    pip install transformers torch

If you are using Google Colab, you can run:

    !pip install transformers torch

============================================================
8. IMPORTS
============================================================
"""

# Import BERT tokenizer and BERT model from Hugging Face Transformers.
from transformers import BertTokenizer, BertModel

# PyTorch is the deep-learning framework used by the BERT model.
import torch


"""
============================================================
9. LOAD THE BERT TOKENIZER
============================================================

A TOKENIZER converts human-readable text into tokens and
then into numerical token IDs that BERT can process.

Example:

    "I deposited money in the bank."

might become tokens similar to:

    [CLS] i deposited money in the bank . [SEP]

Special tokens such as [CLS] and [SEP] are added by BERT's
tokenizer.

[CLS] -> special token placed at the beginning
[SEP] -> special token used to mark the end/separation

The exact tokenization can vary because BERT uses WordPiece
tokenization.
============================================================
"""

# Load the pre-trained BERT tokenizer.
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")


"""
============================================================
10. LOAD THE BERT MODEL
============================================================

This downloads/loads the pre-trained BERT neural network.

The first time you run this code, Hugging Face may download
the model files.

One of the main files is model.safetensors.

For bert-base-uncased, the model weights are roughly
hundreds of megabytes in size.

These weights contain what BERT learned during pre-training.

IMPORTANT:

    Model weights != your sentence

The weights are the learned parameters of the neural network.
============================================================
"""

# Load the pre-trained BERT model.
model = BertModel.from_pretrained("bert-base-uncased")


"""
============================================================
11. INPUT SENTENCES
============================================================

We intentionally use two sentences containing the same word:

    "bank"

But "bank" has different meanings in the two sentences.

This lets us demonstrate CONTEXTUAL EMBEDDINGS.
============================================================
"""

# Store the sentences that we want BERT to process.
sentences = [
    "I deposited money in the bank.",
    "I sat near the bank of the river."
]


"""
============================================================
12. PROCESS EACH SENTENCE
============================================================

We use a for loop because we want to process both sentences
one by one.
============================================================
"""

# Process each sentence separately.
for sentence in sentences:

    """
    ========================================================
    13. TOKENIZE THE SENTENCE
    ========================================================

    return_tensors="pt" means:

        pt = PyTorch

    The tokenizer converts the text into tensors containing
    information such as:

        input_ids
        attention_mask

    input_ids:
        Numerical IDs representing the tokens.

    attention_mask:
        Tells BERT which positions contain real input tokens
        and which positions are padding when padding is used.
    ========================================================
    """

    # Convert the sentence into PyTorch tensors.
    inputs = tokenizer(sentence, return_tensors="pt")


    """
    ========================================================
    14. SEND THE INPUT THROUGH BERT
    ========================================================

    model(**inputs) sends the tokenized information to BERT.

    The ** operator unpacks the dictionary.

    Conceptually, this is similar to:

        model(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"]
        )

    BERT processes the tokens through its Transformer layers.
    ========================================================
    """

    # Pass the tokenized sentence through the BERT model.
    outputs = model(**inputs)


    """
    ========================================================
    15. GET THE TOKENS
    ========================================================

    input_ids contains numbers.

    Example conceptually:

        [101, 1045,  ... , 102]

    We convert those IDs back into readable token strings.

    [0] selects the first sentence from the batch because
    the tokenizer created a batch containing one sentence.
    ========================================================
    """

    # Convert token IDs back into readable BERT tokens.
    tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])


    """
    ========================================================
    16. GET THE CONTEXTUAL EMBEDDINGS
    ========================================================

    last_hidden_state contains a representation for every
    token after BERT has processed the complete sentence.

    BERT-base uses a hidden size of 768.

    Therefore, every token gets a vector containing
    768 numerical values.

    The [0] selects the first sentence from the batch.

    So:

        outputs.last_hidden_state[0]

    gives:

        one 768-dimensional vector for each token.
    ========================================================
    """

    # Extract the contextual embedding for every token.
    embeddings = outputs.last_hidden_state[0]


    """
    ========================================================
    17. PRINT THE RESULT
    ========================================================

    We do NOT print all 768 values because that would produce
    a very large output.

    Instead, embedding[:10] prints only the first 10 values.

    IMPORTANT:

        The complete embedding still has 768 values.

        We are only displaying the first 10.
    ========================================================
    """

    # Print the sentence being processed.
    print("\nSentence:", sentence)

    # Pair each token with its corresponding embedding.
    for token, embedding in zip(tokens, embeddings):

        # Print the token.
        print("Token:", token)

        # Print only the first 10 values of its 768-dimensional vector.
        print("First 10 values:", embedding[:10].detach().numpy())

        print()


"""
============================================================
18. UNDERSTANDING THE OUTPUT
============================================================

You may see output similar to:

    Sentence: I deposited money in the bank.

    Token: [CLS]
    First 10 values: [...]

    Token: i
    First 10 values: [...]

    Token: deposited
    First 10 values: [...]

    ...

    Token: bank
    First 10 values: [...]

BERT has produced an embedding for every token.

The actual vector has 768 values.

We print only the first 10 values for easy viewing.

============================================================
19. WHY DOES "BANK" MATTER?
============================================================

Our two sentences are:

    1. I deposited money in the bank.

    2. I sat near the bank of the river.

In sentence 1, "bank" is related to money.

In sentence 2, "bank" is related to a river.

BERT uses the surrounding context to create contextual
representations.

This is the main NLP concept demonstrated by this program.

============================================================
20. WHAT DOES THE SHAPE MEAN?
============================================================

If we inspect:

    outputs.last_hidden_state.shape

we might get:

    torch.Size([1, 9, 768])

for the first sentence.

This means:

    1   -> number of sentences in the batch
    9   -> number of tokens
    768 -> embedding size

For another sentence, the number of tokens can be different.

For example:

    torch.Size([1, 11, 768])

means:

    1   -> one sentence
    11  -> eleven tokens
    768 -> 768-dimensional embedding for each token

============================================================
21. IMPORTANT PYTHON CONCEPTS USED
============================================================

1. LIST

    sentences = ["sentence 1", "sentence 2"]

2. FOR LOOP

    for sentence in sentences:

3. FUNCTION

    tokenizer(sentence, return_tensors="pt")

4. DICTIONARY

    inputs["input_ids"]

5. ** UNPACKING

    model(**inputs)

6. SLICING

    embedding[:10]

7. ZIP

    zip(tokens, embeddings)

8. NUMPY CONVERSION

    embedding.detach().numpy()

============================================================
22. WHY USE detach()?
============================================================

BERT uses PyTorch tensors.

A tensor may be connected to PyTorch's computation graph.

We are only printing the values; we are not training BERT.

detach() gives us a tensor separated from the computation
graph, which can then be converted to NumPy.

So:

    embedding.detach().numpy()

means approximately:

    PyTorch tensor
          ↓
    detach from graph
          ↓
    convert to NumPy array

============================================================
23. WHY ARE WE NOT TRAINING BERT?
============================================================

In this program, we are only using BERT to generate
embeddings.

This is called using a PRE-TRAINED MODEL for inference.

We are NOT updating BERT's weights.

The basic idea is:

    Text
      ↓
    Tokenizer
      ↓
    Token IDs
      ↓
    Pre-trained BERT
      ↓
    Contextual Embeddings

============================================================
24. COMPLETE FLOW
============================================================

                    RAW TEXT
                       |
                       v
              +----------------+
              |    Tokenizer   |
              +----------------+
                       |
                       v
             Tokens + Token IDs
                       |
                       v
                PyTorch Tensors
                       |
                       v
              +----------------+
              |   BERT Model   |
              |  Transformer   |
              |    Encoder     |
              +----------------+
                       |
                       v
             Contextual Embeddings
                       |
                       v
              last_hidden_state
                       |
                       v
             One vector per token
                       |
                       v
          768-dimensional vectors
          for BERT-base tokens

============================================================
25. EXAM-FOCUSED QUESTIONS
============================================================

Q1. What is BERT?

Answer:
BERT stands for Bidirectional Encoder Representations from
Transformers. It is a pre-trained language model based on
the Transformer encoder architecture and produces
contextual representations of text.

------------------------------------------------------------

Q2. What is a tokenizer?

Answer:
A tokenizer converts text into tokens and numerical token IDs
that can be processed by a language model.

------------------------------------------------------------

Q3. What is an embedding?

Answer:
An embedding is a numerical vector representation of text,
such as a word or token, that captures useful linguistic
information.

------------------------------------------------------------

Q4. What is a contextual embedding?

Answer:
A contextual embedding is a representation whose value
depends on the surrounding context of the word or token.

Example:
The word "bank" can have different representations in
financial and river-related contexts.

------------------------------------------------------------

Q5. What is Hugging Face?

Answer:
Hugging Face provides tools, libraries, and pre-trained
machine-learning models. Its Transformers library makes it
easy to use models such as BERT.

------------------------------------------------------------

Q6. What is bert-base-uncased?

Answer:
It is a pre-trained base-sized BERT model that uses an
uncased vocabulary, meaning it does not distinguish
uppercase and lowercase text.

------------------------------------------------------------

Q7. What does return_tensors="pt" mean?

Answer:
It tells the tokenizer to return the tokenized data as
PyTorch tensors.

------------------------------------------------------------

Q8. What is input_ids?

Answer:
input_ids are numerical IDs representing the tokens in
the input text.

------------------------------------------------------------

Q9. What is attention_mask?

Answer:
attention_mask indicates which token positions should be
considered by the model, especially when padding is used.

------------------------------------------------------------

Q10. What is last_hidden_state?

Answer:
last_hidden_state contains the contextual representations
produced by the final BERT layer for each input token.

------------------------------------------------------------

Q11. What is the embedding size of BERT-base?

Answer:
BERT-base has a hidden size of 768, so each token gets a
768-dimensional contextual representation.

------------------------------------------------------------

Q12. Why do we use two sentences containing "bank"?

Answer:
To demonstrate contextual embeddings. The word "bank" has
different meanings in the two sentences, so BERT can produce
different contextual representations based on the surrounding
words.

============================================================
26. VERY IMPORTANT EXAM POINTS
============================================================

Remember these:

    BERT
      -> Bidirectional Encoder Representations from Transformers

    Architecture
      -> Transformer Encoder

    Tokenizer
      -> Text to tokens/token IDs

    input_ids
      -> Numerical token representations

    attention_mask
      -> Indicates relevant input positions

    BERT-base hidden size
      -> 768

    last_hidden_state
      -> Contextual representation of every token

    Contextual embedding
      -> Representation depends on surrounding context

    Hugging Face Transformers
      -> Library used to load/use pre-trained models

    bert-base-uncased
      -> Base BERT model with uncased vocabulary

============================================================
27. ONE-MINUTE REVISION
============================================================

If the examiner asks:

"What are you doing in this program?"

Say:

    "We are using a pre-trained BERT model from Hugging Face
    to generate contextual embeddings for the tokens in two
    sentences. We tokenize the sentences, convert them into
    PyTorch tensors, pass them through BERT, and extract the
    last_hidden_state. BERT-base produces a 768-dimensional
    contextual representation for each token. We use the word
    'bank' in two different contexts to demonstrate that BERT
    generates context-dependent representations."

============================================================
28. FINAL MEMORY TRICK
============================================================

Remember:

    TEXT
      ↓
    TOKENIZE
      ↓
    TOKEN IDs
      ↓
    TENSOR
      ↓
    BERT
      ↓
    CONTEXT
      ↓
    EMBEDDING

Short form:

    Text -> Tokenizer -> BERT -> Embeddings

============================================================
END
============================================================
"""

# The actual executable code starts below.
# The large documentation above is intentionally included
# so that this file can also be used as beginner study notes.

from transformers import BertTokenizer, BertModel
import torch

# Load the pre-trained BERT tokenizer.
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Load the pre-trained BERT model.
model = BertModel.from_pretrained("bert-base-uncased")

# Two sentences are used to demonstrate contextual meaning.
sentences = [
    "I deposited money in the bank.",
    "I sat near the bank of the river."
]

# Process each sentence one at a time.
for sentence in sentences:

    # Convert text into PyTorch tensors.
    inputs = tokenizer(sentence, return_tensors="pt")

    # Pass the tokenized input through BERT.
    outputs = model(**inputs)

    # Convert numerical token IDs into readable tokens.
    tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

    # Get the contextual embedding of every token.
    embeddings = outputs.last_hidden_state[0]

    # Print the sentence.
    print("\nSentence:", sentence)

    # Print every token and only the first 10 embedding values.
    for token, embedding in zip(tokens, embeddings):
        print("Token:", token)
        print("First 10 values:", embedding[:10].detach().numpy())
        print()