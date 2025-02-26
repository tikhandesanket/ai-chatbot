import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

# Cache to store previously asked questions
cache = {}

# Load or initialize the dataset
if os.path.exists("qa_model.pkl"):
    with open("qa_model.pkl", "rb") as f:
        model_data = pickle.load(f)
        questions = model_data.get("questions", [])
        answers = model_data.get("answers", [])
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

# Populate cache with known questions and answers
for q, a in zip(questions, answers):
    cache[q.lower()] = a

# Function to predict or retrain the model
def main(action, query=None, new_answer=None):
    if action == "predict":
        return get_prediction(query)
    elif action == "train_model":
        return train_model(query, new_answer)
    elif action == "update_answer":
        return update_answer(query, new_answer)
    elif action == "update_or_delete_question":
        return update_or_delete_question(query, new_answer)
    elif action == "list_questions":
        return list_questions()
    elif action == "list_answers":
        return list_answers()

# Function to predict the response with caching
def get_prediction(query):
    query_lower = query.lower()

    # **Check cache first**
    if query_lower in cache:
        return cache[query_lower]

    query_vec = model.named_steps['tfidfvectorizer'].transform([query])
    question_vecs = model.named_steps['tfidfvectorizer'].transform(questions)

    # Calculate cosine similarity
    similarities = cosine_similarity(query_vec, question_vecs)
    max_similarity = similarities.max()

    threshold = 0.65
    if max_similarity < threshold:
        return "No good match found. Please provide the correct answer."
    else:
        prediction = model.predict([query])[0]
        
        # **Store in cache for faster future retrieval**
        cache[query_lower] = prediction
        
        return prediction

# Function to train the model with a new question and answer
def train_model(new_question, new_answer):
    global questions, answers

    # Append new question-answer pair
    questions.append(new_question)
    answers.append(new_answer)

    # Retrain the model
    model.fit(questions, answers)

    # **Update cache**
    cache[new_question.lower()] = new_answer

    # Save the updated model
    with open("qa_model.pkl", "wb") as f:
        pickle.dump({"questions": questions, "answers": answers}, f)

    return f"Model retrained with: '{new_question}' -> '{new_answer}'"

# Function to update an answer
def update_answer(existing_question, new_answer):
    global questions, answers

    if existing_question in questions:
        index = questions.index(existing_question)
        answers[index] = new_answer

        # Retrain the model
        model.fit(questions, answers)

        # **Update cache**
        cache[existing_question.lower()] = new_answer

        # Save the model
        with open("qa_model.pkl", "wb") as f:
            pickle.dump({"questions": questions, "answers": answers}, f)
        
        return f"Answer updated for: '{existing_question}'"
    
    return "Question not found."

# Function to update or delete a question
def update_or_delete_question(existing_question, new_question):
    global questions, answers

    if existing_question in questions:
        index = questions.index(existing_question)

        if new_question:
            questions[index] = new_question
            # **Update cache**
            cache[new_question.lower()] = answers[index]
        else:
            # Delete the question
            del questions[index]
            del answers[index]

        # Retrain the model
        model.fit(questions, answers)

        # **Remove from cache if deleted**
        if not new_question:
            cache.pop(existing_question.lower(), None)

        # Save the model
        with open("qa_model.pkl", "wb") as f:
            pickle.dump({"questions": questions, "answers": answers}, f)

        return f"Updated question: '{existing_question}' -> '{new_question}'" if new_question else f"Deleted: '{existing_question}'"

    return "Question not found."

def list_questions():
    return questions

def list_answers():
    return answers

if __name__ == "__main__":
    action = sys.argv[1]
    question = sys.argv[2] if len(sys.argv) > 2 else None
    answer = sys.argv[3] if len(sys.argv) > 3 else None
    print(main(action, question, answer))
