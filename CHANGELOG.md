## [Unreleased]

## [0.1.0] - 2024-09-15

- Initial release

## [ 0.1.6.4] - 2025-02-26
### Fixed
- Added caching mechanism to ChatbotService to improve response speed.
- Updated `.gemspec` to reflect the fix.

## [ 0.1.6.5] - 2025-02-26
### Fixed
- Added postgres DB for better storage.
- Updated `.gemspec` to reflect the fix.
- add following infpr mation in enviroment.rb file

      ENV['DB_NAME'] ||= 'jio_hotel_development1'
      ENV['DB_USERNAME'] ||= 'postgres'
      ENV['DB_PASSWORD'] ||= 'XXXXX'
      ENV['DB_HOST'] ||= 'your host'
      ENV['DB_PORT'] ||= '5432'

## [ 0.1.6.5.1] - 2025-02-26
### Key Fixes & Changes
-Used make_pipeline(TfidfVectorizer(), MultinomialNB()) to create a proper ML model.
-Fixed the train_model, update_answer, and delete_question functions to retrain pipeline.
-Ensured the model trains only if questions exist.
-Added validation checks for update_answer and delete_question to avoid errors.
