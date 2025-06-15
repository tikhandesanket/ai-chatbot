import sys
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics.pairwise import cosine_similarity

DATA_FILE = "qa_model.pkl"

# Globals
questions = []
answers = []
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# ------------------- Load or Initialize ------------------- #
def load_data():
    global questions, answers
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "rb") as f:
            model_data = pickle.load(f)
            questions = model_data.get('questions', [])
            answers = model_data.get('answers', [])
            # print(f" Loaded {len(questions)} Q&A pairs.")
    else:
        # Default seed data
        questions.extend([
            "How to create a new model in Rails?",
            "What is migration?",
            "How to add a route?"
        ])
        answers.extend([
            "You can create a model using 'rails generate model'.",
            "Migration is a database schema change.",
            "You can add a route in the config/routes.rb file."
        ])
        print(" No existing model found, using default seed data.")

    retrain_model()

def save_data():
    with open(DATA_FILE, "wb") as f:
        pickle.dump({'questions': questions, 'answers': answers}, f)

def retrain_model():
    if questions and answers:
        model.fit(questions, answers)

# ------------------- Core Actions ------------------- #
def get_prediction(query):
    query_vec = model.named_steps['tfidfvectorizer'].transform([query])
    question_vecs = model.named_steps['tfidfvectorizer'].transform(questions)
    similarities = cosine_similarity(query_vec, question_vecs)
    max_similarity = similarities.max()

    #print(f"🔍 Similarity Score: {max_similarity:.2f}")

    threshold = 0.65
    if max_similarity < threshold:
        return " No good match found. You may need to train the model with this question."
    else:
        prediction = model.predict([query])
        return prediction[0]

def train_model(new_question, new_answer):
    questions.append(new_question)
    answers.append(new_answer)
    retrain_model()
    save_data()
    return f"Model updated with: '{new_question}'"

def update_answer(existing_question, new_answer):
    if existing_question in questions:
        idx = questions.index(existing_question)
        answers[idx] = new_answer
        retrain_model()
        save_data()
        return f" Answer updated for: '{existing_question}'"
    return " Question not found."

def update_or_delete_question(existing_question, new_question=None):
    if existing_question in questions:
        idx = questions.index(existing_question)
        if new_question:
            questions[idx] = new_question
            action = f"Question updated to: '{new_question}'"
        else:
            questions.pop(idx)
            answers.pop(idx)
            action = f"🗑️ Question '{existing_question}' deleted."
        retrain_model()
        save_data()
        return action
    return " Question not found."

def list_questions():
    return "\n".join([f"{i+1}. {q}" for i, q in enumerate(questions)])

def list_answers():
    return "\n".join([f"{i+1}. {a}" for i, a in enumerate(answers)])

# ------------------- CLI Entry ------------------- #
def main(action, query=None, answer=None):
    load_data()

    if action == "predict":
        return get_prediction(query)
    elif action == "train_model":
        return train_model(query, answer)
    elif action == "update_answer":
        return update_answer(query, answer)
    elif action == "update_or_delete_question":
        return update_or_delete_question(query, answer)
    elif action == "list_questions":
        return list_questions()
    elif action == "list_answers":
        return list_answers()
    else:
        return " Unknown action. Try: predict, train_model, update_answer, list_questions, list_answers"

if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else None
    question = sys.argv[2] if len(sys.argv) > 2 else None
    answer = sys.argv[3] if len(sys.argv) > 3 else None
    print(main(action, question, answer))
