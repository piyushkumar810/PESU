import streamlit as st
import pickle


# ======================================================
# LOAD SAVED FILES
# ======================================================

model = pickle.load(open(r"C:/ai_ml_project/model.pkl", "rb"))

vectorizer = pickle.load(open(r"C:/ai_ml_project/vectorizer.pkl", "rb"))

encoder = pickle.load(open(r"C:/ai_ml_project/encoder.pkl", "rb"))


# ======================================================
# PAGE TITLE
# ======================================================

st.title("AI-Based Learning & MCQ Generation System")

st.write("Enter AIML-related text and get topic prediction + MCQs")


# ======================================================
# USER INPUT
# ======================================================

user_input = st.text_area(
    "Enter your text here"
)


# ======================================================
# PREDICTION BUTTON
# ======================================================

if st.button("Predict Topic"):

    if user_input.strip() != "":

        # TEXT TO VECTOR
        transformed_text = vectorizer.transform([user_input])

        # PREDICTION
        prediction = model.predict(transformed_text)

        # DECODE LABEL
        predicted_topic = encoder.inverse_transform(prediction)

        # DISPLAY TOPIC
        st.success(f"Predicted Topic: {predicted_topic[0]}")


        # ======================================================
        # EXPLANATIONS
        # ======================================================

        if predicted_topic[0] == "Supervised Learning":

            st.subheader("Explanation")

            st.write("""
            Supervised Learning is a machine learning technique
            where the model learns from labeled data.

            Example:
            Regression and Classification
            """)

            st.subheader("MCQs")

            st.write("""
            1. Which algorithm belongs to supervised learning?

            A. K-Means
            B. Linear Regression ✅
            C. Apriori
            D. PCA
            """)


        elif predicted_topic[0] == "Unsupervised Learning":

            st.subheader("Explanation")

            st.write("""
            Unsupervised learning finds hidden patterns
            from unlabeled data.

            Example:
            Clustering
            """)

            st.subheader("MCQs")

            st.write("""
            1. K-Means is used for?

            A. Classification
            B. Clustering ✅
            C. Regression
            D. Reinforcement
            """)


        elif predicted_topic[0] == "Reinforcement Learning":

            st.subheader("Explanation")

            st.write("""
            Reinforcement Learning learns using rewards
            and punishments.
            """)

            st.subheader("MCQs")

            st.write("""
            1. Reinforcement learning is based on?

            A. Labels
            B. Rewards ✅
            C. Clustering
            D. Regression
            """)


        elif predicted_topic[0] == "Deep Learning":

            st.subheader("Explanation")

            st.write("""
            Deep Learning uses neural networks with
            multiple hidden layers.
            """)

            st.subheader("MCQs")

            st.write("""
            1. Deep learning mainly uses?

            A. Trees
            B. Neural Networks ✅
            C. K-Means
            D. Apriori
            """)


        else:

            st.subheader("Explanation")

            st.write("""
            Artificial Intelligence enables machines
            to simulate human intelligence.
            """)

            st.subheader("MCQs")

            st.write("""
            1. AI stands for?

            A. Artificial Intelligence ✅
            B. Automatic Input
            C. Advanced Internet
            D. None
            """)

    else:

        st.warning("Please enter some text")