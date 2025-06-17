Gem::Specification.new do |spec|
  spec.name          = "ai_chatbot"
  # Require the version file to access AiChatbot::VERSION
  require_relative "lib/ai_chatbot/version"
  spec.version       = AiChatbot::VERSION
  spec.authors       = ["Sanket"]
  spec.email         = ["sanket.tikhande@gmail.com"]

  spec.summary       = "Added new pkg-rapidfuzz for more accuracy"
  spec.description   = "Fixed the model error in version 0.1.6.5.4. Details are available on Git. Also added a new package rapidfuzz. Please make sure to run pip install rapidfuzz."

  spec.homepage      = "https://github.com/tikhandesanket/ai-chatbot"
  spec.metadata['source_code_uri'] = 'https://github.com/tikhandesanket/ai-chatbot'
  spec.license       = "MIT"

  spec.files         = Dir["lib/**/*"]
  spec.require_paths = ["lib"]

  spec.add_dependency "open3"
end
