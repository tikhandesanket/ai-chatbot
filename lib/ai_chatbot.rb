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
      stdout, stderr, status = Open3.capture3("python3", "#{__dir__}/ml_model.py", "train_model", new_question, new_answer)

      if status.success?
        return stdout.strip
      else
        raise "Error: #{stderr}"
      end
    end


       # Method to train the model with a new question-answer pair
    def self.update_answer(existing_question, new_answer)
      stdout, stderr, status = Open3.capture3("python3", "#{__dir__}/ml_model.py", "update_answer", existing_question, new_answer)

      if status.success?
        return stdout.strip
      else
        raise "Error: #{stderr}"
      end
    end

    def self.update_or_delete_question(existing_question, new_question=nil)
         stdout, stderr, status = new_question == nil ? Open3.capture3("python3", "#{__dir__}/ml_model.py", "update_or_delete_question", existing_question,"None") : Open3.capture3("python3", "#{__dir__}/ml_model.py", "update_or_delete_question", existing_question, new_question)

      if status.success?
        return stdout.strip
      else
        raise "Error: #{stderr}"
      end
    end

    def self.list_questions
      stdout, stderr, status = Open3.capture3("python3", "#{__dir__}/ml_model.py", "list_questions")

      if status.success?
        return stdout.strip
      else
        raise "Error: #{stderr}"
      end
    end

    def self.list_answers
      stdout, stderr, status = Open3.capture3("python3", "#{__dir__}/ml_model.py", "list_answers")

      if status.success?
        return stdout.strip
      else
        raise "Error: #{stderr}"
      end
    end


  end
end
