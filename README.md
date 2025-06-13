# AiChatbot

**AiChatbot** is a lightweight Ruby gem that provides a simple AI-based chatbot using TF-IDF vectorization and Naive Bayes classification. It supports learning new Q&A pairs and predicting answers based on cosine similarity.

---

## 🔧 Gem Installation

Add this line to your Gemfile:

```ruby
gem 'ai_chatbot', '0.1.6.5.2'
```

And then execute:

```bash
bundle install
```

Or install it directly:

```bash
gem install ai_chatbot
```

---

## 🚀 Usage Example

```ruby
require 'ai_chatbot'

chatbot = AiChatbot::Bot.new

# Predict an answer
puts chatbot.predict("How to create a model in Rails?")

# Add new training data
chatbot.train("How to upload a dish in hotel?", "Use the admin panel under 'Menu Upload' to add a dish.")
```

---

## 💡 Features

- ✅ TF-IDF Vectorizer for understanding query intent
- ✅ Cosine Similarity for matching confidence
- ✅ Naive Bayes Classifier for predictions
- ✅ Add / Update / Delete Q&A pairs
- ✅ CLI Support

---

## 📁 CLI Usage

```bash
ruby chatbot.rb predict "How to add a route?"
ruby chatbot.rb train_model "What is RubyGems?" "A package manager for Ruby libraries."
```

---

## 📦 Development

To build and install locally:

```bash
bundle install
gem build ai_chatbot.gemspec
gem install ./ai_chatbot-x.y.z.gem
```

To release:

```bash
rake release
```

---

## 🔐 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Sanket Tikhande**  
[GitHub: @tikhandesanket](https://github.com/tikhandesanket)
