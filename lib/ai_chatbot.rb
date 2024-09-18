require 'open3'

module AiChatbot
  class Chatbot
    # Method to ask a question and get prediction from Python
    def self.ask_question(question)
      stdout, stderr, status = Open3.capture3("python3", "#{__dir__}/ml_model.py", "predict", question)

      if status.success?
        return stdout.strip
      else
        raise "Error: #{stderr}"
      end
    end

    # Method to train the model with a new question-answer pair
    def self.train_model(new_question, new_answer)
      stdout, stderr, status = Open3.capture3("python3", "#{__dir__}/ml_model.py", "train", new_question, new_answer)

      if status.success?
        return stdout.strip
      else
        raise "Error: #{stderr}"
      end
    end
  end
end
