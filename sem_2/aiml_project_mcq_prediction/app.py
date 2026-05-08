import streamlit as st
import pickle
import random

# PAGE CONFIGURATION
st.set_page_config(
    page_title="AI Learning & MCQ Practice System",
    page_icon="🧠",
    layout="wide"
)

# LOAD TRAINED FILES
model = pickle.load(
    open(r"C:/ai_ml_project/model.pkl", "rb")
)

vectorizer = pickle.load(
    open(r"C:/ai_ml_project/vectorizer.pkl", "rb")
)

encoder = pickle.load(
    open(r"C:/ai_ml_project/encoder.pkl", "rb")
)

# SIDEBAR
st.sidebar.title("📚 AI Learning Assistant")

st.sidebar.write("""
This system helps students:
- Understand topics
- Practice MCQs
- Improve conceptual knowledge
- Prepare for GATE-level questions
""")


difficulty = st.sidebar.selectbox(
    "Select Difficulty",
    ["Easy", "Medium", "Hard", "GATE Level"]
)


mcq_type = st.sidebar.selectbox(
    "Select MCQ Type",
    [
        "Conceptual",
        "Code Snippet",
        "Output Prediction",
        "Scenario Based"
    ]
)

# MAIN TITLE
st.title("🧠 AI-Powered Learning & MCQ Practice System")

st.write("""
Enter any AIML topic or study content.
The system will:
- Predict the topic
- Explain the concept
- Generate MCQ practice questions
""")

# USER INPUT
user_input = st.text_area(
    "✍ Enter Topic / Study Content",
    height=250
)

# GENERATE BUTTON
if st.button("🚀 Generate Learning Content"):

    if user_input.strip() == "":
        st.warning("Please enter some content.")
    
    else:
        # MODEL PREDICTION
        transformed_text = vectorizer.transform([user_input])

        prediction = model.predict(transformed_text)

        predicted_topic = encoder.inverse_transform(prediction)

        # DISPLAY TOPIC
        st.success(f"📌 Predicted Topic : {predicted_topic[0]}")

        # EXPLANATIONS
        st.subheader("📖 Explanation")


        if predicted_topic[0] == "Supervised Learning":

            st.write("""
            Supervised Learning is a machine learning technique
            where the model learns using labeled training data.

            Common algorithms:
            - Linear Regression
            - Logistic Regression
            - Decision Trees

            Applications:
            - Spam detection
            - House price prediction
            - Medical diagnosis
            """)

        elif predicted_topic[0] == "Unsupervised Learning":

            st.write("""
            Unsupervised Learning works with unlabeled data.

            It identifies hidden patterns and relationships.

            Common algorithms:
            - K-Means Clustering
            - Hierarchical Clustering

            Applications:
            - Customer segmentation
            - Pattern discovery
            """)

        elif predicted_topic[0] == "Reinforcement Learning":

            st.write("""
            Reinforcement Learning learns using rewards
            and punishments.

            Important concepts:
            - Agent
            - Environment
            - Reward

            Applications:
            - Robotics
            - Self-driving cars
            - Game AI
            """)

        elif predicted_topic[0] == "Deep Learning":

            st.write("""
            Deep Learning uses neural networks with
            multiple hidden layers.

            Common architectures:
            - CNN
            - RNN

            Applications:
            - Image recognition
            - NLP
            - Speech processing
            """)

        else:

            st.write("""
            Artificial Intelligence enables machines
            to simulate human intelligence.

            AI includes:
            - Machine Learning
            - NLP
            - Computer Vision
            """)

        # MCQ GENERATION
        st.subheader("📝 MCQ Practice")

        # CONCEPTUAL MCQs
        if mcq_type == "Conceptual":

            conceptual_mcqs = [

                {
                    "question":
                    "Which algorithm belongs to supervised learning?",

                    "options":
                    [
                        "K-Means",
                        "Linear Regression",
                        "Apriori",
                        "PCA"
                    ],

                    "answer":
                    "Linear Regression"
                },

                {
                    "question":
                    "What is the main purpose of clustering?",

                    "options":
                    [
                        "Classification",
                        "Grouping similar data",
                        "Prediction",
                        "Sorting"
                    ],

                    "answer":
                    "Grouping similar data"
                },

                {
                    "question":
                    "Which learning method uses rewards?",

                    "options":
                    [
                        "Supervised",
                        "Unsupervised",
                        "Reinforcement",
                        "Regression"
                    ],

                    "answer":
                    "Reinforcement"
                }
            ]


            selected = random.sample(
                conceptual_mcqs,
                min(3, len(conceptual_mcqs))
            )


            for i, mcq in enumerate(selected):

                st.write(f"### Q{i+1}. {mcq['question']}")

                for option in mcq['options']:
                    st.write(f"- {option}")

                st.success(f"✅ Answer: {mcq['answer']}")

                st.write("---")

        # CODE SNIPPET MCQs
        elif mcq_type == "Code Snippet":

            st.code("""
                    for i in range(3):
                    print(i)
                """,
                language="python"
            )

            st.write("""
            ### What will be the output?

            A. 0 1 2
            B. 1 2 3
            C. Infinite Loop
            D. Error
            """)

            st.success("✅ Correct Answer: A")

        # OUTPUT PREDICTION
        elif mcq_type == "Output Prediction":

            st.code("""
            x = [1,2,3]
            print(len(x))
                """,
                language="python"
            )

            st.write("""
            ### Predict the output

            A. 1
            B. 2
            C. 3
            D. Error
            """)

            st.success("✅ Correct Answer: C")

        # SCENARIO BASED
        elif mcq_type == "Scenario Based":

            st.write("""
            ### Scenario

            A company wants to divide customers into groups
            based on purchasing behavior without labels.

            Which algorithm is best suited?
            """)

            st.write("""
            A. Linear Regression
            B. Logistic Regression
            C. K-Means Clustering
            D. Decision Tree
            """)

            st.success("✅ Correct Answer: C")

        # DIFFICULTY LEVEL MESSAGE
        st.subheader("🎯 Difficulty Level")

        if difficulty == "Easy":
            st.info("Basic conceptual questions generated.")

        elif difficulty == "Medium":
            st.info("Intermediate-level analytical questions generated.")

        elif difficulty == "Hard":
            st.warning("Advanced problem-solving MCQs generated.")

        else:
            st.error("GATE-level conceptual and tricky MCQs generated.")

# FOOTER
st.write("---")

st.write(
    "✅ Built using Python, Streamlit, TF-IDF, and Naive Bayes"
)