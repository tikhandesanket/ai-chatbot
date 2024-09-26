# Ai_Chatbot

TODO: Delete this and the text below, and describe your gem

Welcome to your new gem! In this directory, you'll find the files you need to be able to package up your Ruby library into a gem. Put your Ruby code in the file `lib/ai_chatbot`. To experiment with that code, run `bin/console` for an interactive prompt.

## Installation

TODO: Replace `ai_chatbot` with your gem name right after releasing it to RubyGems.org. Please do not do it earlier due to security reasons. Alternatively, replace this section with instructions to install your gem from git if you don't plan to release to RubyGems.org.

Install the gem and add to the application's Gemfile by executing:

    $ bundle add gem 'ai_chatbot', '~> 0.1.6.2'

If the bundler is not being used to manage dependencies, install the gem by executing:

    $ gem install ai_chatbot

## Usage

TODO: Write usage instructions here

## Development

After checking out the repo, run `bin/setup` to install dependencies. You can also run `bin/console` for an interactive prompt that will allow you to experiment.

Steps to install 

1) Add gem in your Gem file - ` gem 'ai_chatbot', '~> 0.1.6.2`

2) How to use it - pass your question in the question variable   `AiChatbot::Chatbot.ask_question(question)`

3) If the answer doesn't match or does not exist train your model to match 

  `AiChatbot::Chatbot.train_model("How to rename column in table","rails generate migration RenameOldColumnNameToNewColumnNameInTableName..")`

4) If you want tu update answer `AiChatbot::Chatbot.update_answer("How to rename column in table"," ADD UPDATED ANSWER HERE")` 

make sure you have a machine with Python3 also install scikit-learn by  pip install scikit-learn `Python3 also install scikit-learn by  pip install scikit-learn`

here are some methods you can use in your application 
`1-AiChatbot::Chatbot.update_answer(existing_question, new_answer)

 2-AiChatbot::Chatbot.update_or_delete_question(existing_question, new_question) // to delete question e.g.  AiChatbot::Chatbot.update_or_delete_question(existing_question)
 
 3-AiChatbot::Chatbot.list_questions()

 4-AiChatbot::Chatbot.list_answers()`

To install this gem onto your local machine, run `bundle exec rake install`. To release a new version, update the version number in `version.rb`, and then run `bundle exec rake release`, which will create a git tag for the version, push git commits and the created tag, and push the `.gem` file to [rubygems.org](https://rubygems.org).

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/tikhandesanket/ai_chatbot.git. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [code of conduct](https://github.com/tikhandesanket/ai_chatbot.git).

## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

## Code of Conduct

Everyone interacting in the AiChatbot project's codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/[USERNAME]/ai_chatbot/blob/master/CODE_OF_CONDUCT.md).
# ai_chatbot
