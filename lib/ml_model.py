import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

# Load or initialize the dataset
if os.path.exists("qa_model.pkl"):
    with open("qa_model.pkl", "rb") as f:
        model_data = pickle.load(f)
        questions = model_data['questions']
        answers = model_data['answers']
else:
    questions = [
        "How to create a new model in Rails?",
        "What is migration?",
        "How to add a route?"
    ]
    answers = [
        "You can create a model using 'rails generate model'.",
        "Migration is a database schema change.",
        "You can add a route in the config/routes.rb file."
    ]

# Create a pipeline (TF-IDF + MultinomialNB)
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(questions, answers)

# Function to predict or retrain the model
def main(action, query=None, new_answer=None):
    if action == "predict":
        return get_prediction(query)
    elif action == "train":
        return train_model(query, new_answer)
    elif action == "update":
        return update_answer(query, new_answer)
    elif action == "list":
        return list_questions()

# Function to predict the response with confidence check
def get_prediction(query):
    query_vec = model.named_steps['tfidfvectorizer'].transform([query])
    question_vecs = model.named_steps['tfidfvectorizer'].transform(questions)

    # Calculate cosine similarity between query and known questions
    similarities = cosine_similarity(query_vec, question_vecs)
    max_similarity = similarities.max()

    threshold = 0.70
    if max_similarity < threshold:
        return "No good match found. Please provide the correct answer."
    else:
        prediction = model.predict([query])
        return prediction[0]

# Function to train the model with a new question and answer
def train_model(new_question, new_answer):
    global questions, answers

    # Append new question-answer pair to the dataset
    questions.append(new_question)
    answers.append(new_answer)

    # Retrain the model with updated data
    model.fit(questions, answers)

    # Save the updated model and data
    with open("qa_model.pkl", "wb") as f:
        pickle.dump({"questions": questions, "answers": answers}, f)

    return f"Model retrained with the new question: '{new_question}' and answer: '{new_answer}'"

def update_answer(existing_question, new_answer):
    global questions, answers

    if existing_question in questions:
        # Find the index of the existing question
        index = questions.index(existing_question)
        # Update the answer
        answers[index] = new_answer
        # Retrain the model with updated data
        model.fit(questions, answers)
        # Save the updated model and data
        with open("qa_model.pkl", "wb") as f:
            pickle.dump({"questions": questions, "answers": answers}, f)
        return f"Answer updated for the question: '{existing_question}'"
    else:
        return "Question not found. Please provide a valid question."    

def list_questions():
    global questions
    return questions

if __name__ == "__main__":
    # Expecting action (predict/train), question, and answer (if training)
    action = sys.argv[1]
    question = sys.argv[2] if len(sys.argv) > 2 else None
    answer = sys.argv[3] if len(sys.argv) > 3 else None
    print(main(action, question, answer))
