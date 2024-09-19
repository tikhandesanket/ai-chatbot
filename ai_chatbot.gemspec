Gem::Specification.new do |spec|
  spec.name          = "ai_chatbot"
  # Require the version file to access AiChatbot::VERSION
  require_relative "lib/ai_chatbot/version"
  spec.version       = AiChatbot::VERSION
  spec.authors       = ["Sanket"]
  spec.email         = ["sanket.tikhande@gmail.com"]

  spec.summary       = %q{A chatbot for Rails integration with AI model using Python}
  spec.description   = %q{Integrates a chatbot using Python for predictions and training in a Rails application.}
  # You can remove this line if no homepage is available
  spec.homepage      = "https://github.com/tikhandesanket/ai_chatbot"
  # spec.metadata['source_code_uri'] = 'https://github.com/tikhandesanket/ai_chatbot'
  spec.license       = "MIT"

  spec.files         = Dir["lib/**/*"]
  spec.require_paths = ["lib"]

  spec.add_dependency "open3"
end
