# AI Chatbot

Welcome to **AI Chatbot**! This gem provides a simple and efficient way to integrate chatbot functionality into your Ruby application.

---

## 🚀 Installation

### Add to Your Gemfile:
```ruby
bundle add 'ai_chatbot', '~> 0.1.6.4'
```

### Install Manually:
```sh
gem install ai_chatbot
```

---

## 📖 Usage

<<<<<<< HEAD
    $ bundle add gem 'ai_chatbot', '~> 0.1.6.3'
=======
### Asking a Question
Pass a question to the chatbot and get an AI-generated response:
```ruby
AiChatbot::Chatbot.ask_question("How do I create a migration in Rails?")
```
>>>>>>> d28fea59d6d07efc0b6155445cadd0a093fb3ae6

### Training the Model
If the chatbot response is incorrect or missing, you can train it:
```ruby
AiChatbot::Chatbot.train_model("How to rename a column in the table", "rails generate migration RenameOldColumnNameToNewColumnNameInTableName")
```

### Updating an Answer
To modify an existing response:
```ruby
AiChatbot::Chatbot.update_answer("How to rename a column in the table", "UPDATED ANSWER HERE")
```

### Available Methods:
- `AiChatbot::Chatbot.update_answer(existing_question, new_answer)`
- `AiChatbot::Chatbot.update_or_delete_question(existing_question, new_question)`
- *(To delete: `AiChatbot::Chatbot.update_or_delete_question(existing_question)`) *
- `AiChatbot::Chatbot.list_questions()`
- `AiChatbot::Chatbot.list_answers()`

---


## 🔥 Version: ai_chatbot-0.1.6.5.1

### Installation Steps

<<<<<<< HEAD
1) Add gem in your Gem file - ` gem 'ai_chatbot', '~> 0.1.6.3`
=======
1. Install dependencies:
   ```sh
   pip install psycopg2
   pip install dotenv
   ```
2. Set environment variables in `production.rb`:
   ```ruby
   ENV['DB_NAME'] ||= 'YOUR_DB_NAME'
   ENV['DB_USERNAME'] ||= 'XXUSERNAMEXX'
   ENV['DB_PASSWORD'] ||= 'XXXXXXX'
   ENV['DB_HOST'] ||= 'XXXXX.72.125'
   ENV['DB_PORT'] ||= '5432'
   ```
3. Add the latest gem version:
   ```ruby
   gem 'ai_chatbot', '0.1.6.5.1'
   ```
4. Install the gem:
   ```sh
   bundle install
   ```
>>>>>>> d28fea59d6d07efc0b6155445cadd0a093fb3ae6

### 📌 Rails Database Migration
```ruby
class CreateQaData < ActiveRecord::Migration[7.0]
  def change
    create_table :qa_data do |t|
      t.text :question, unique: true, null: false
      t.text :answer, null: false
      t.timestamps
    end
  end
end
```

---

## 🤝 Contributing

Bug reports and pull requests are welcome at **[GitHub Repository](https://github.com/tikhandesanket/ai_chatbot.git)**.

### 📜 Code of Conduct
Contributors must adhere to our [Code of Conduct](https://github.com/tikhandesanket/ai_chatbot/blob/master/CODE_OF_CONDUCT.md).

<<<<<<< HEAD
here are some methods you can use in your application 
`1-AiChatbot::Chatbot.update_answer(existing_question, new_answer)
 2-AiChatbot::Chatbot.update_or_delete_question(existing_question, new_question) // to delete question e.g.  AiChatbot::Chatbot.update_or_delete_question(existing_question, "None") 
 3-AiChatbot::Chatbot.list_questions()
 4-AiChatbot::Chatbot.list_answers()`

To install this gem onto your local machine, run `bundle exec rake install`. To release a new version, update the version number in `version.rb`, and then run `bundle exec rake release`, which will create a git tag for the version, push git commits and the created tag, and push the `.gem` file to [rubygems.org](https://rubygems.org).
=======
---
>>>>>>> d28fea59d6d07efc0b6155445cadd0a093fb3ae6

## 📜 License

This gem is available under the **[MIT License](https://opensource.org/licenses/MIT)**.

---


✨ *Happy Coding!* 🚀

