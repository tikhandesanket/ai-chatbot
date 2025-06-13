Gem::Specification.new do |spec|
  spec.name          = "ai_chatbot"
  # Require the version file to access AiChatbot::VERSION
  require_relative "lib/ai_chatbot/version"
  spec.version       = AiChatbot::VERSION
  spec.authors       = ["Sanket"]
  spec.email         = ["sanket.tikhande@gmail.com"]

  spec.summary       = "Fix: Added high accuracy"
  spec.description   = "fixed model error. Version 0.1.6.5.1 Details on Git."

  spec.homepage      = "https://github.com/tikhandesanket/ai-chatbot"
  spec.metadata['source_code_uri'] = 'https://github.com/tikhandesanket/ai-chatbot'
  spec.license       = "MIT"

  spec.files         = Dir["lib/**/*"]
  spec.require_paths = ["lib"]

  spec.add_dependency "open3"
end
