from googletrans import Translator
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Initialize the Google Translator
translator = Translator()

# Swahili reviews dataset
swahili_reviews = [
    {"title": "Bidhaa bora", "content": "Nimeridhika sana na ubora na utendaji. Imezidi matarajio yangu!", "rating": "5"},
    {"title": "Ubora duni", "content": "Bidhaa ilivunjika baada ya siku mbili tu za matumizi. Nimevunjika moyo.", "rating": "1"},
    {"title": "Si mbaya", "content": "Ni sawa. Sio nzuri sana, lakini sio mbaya pia.", "rating": "3"},
    {"title": "Ninaipenda!", "content": "Huu ni ununuzi bora zaidi ambao nimewahi kufanya. Naipendekeza sana!", "rating": "5"},
    {"title": "Uzoefu mbaya", "content": "Huduma kwa wateja haikusaidia na bidhaa haifai pesa.", "rating": "1"}
]

# Translate and analyze sentiment
for review in swahili_reviews:
    translated_content = translator.translate(review['content'], src='sw', dest='en').text
    sentiment_score = analyzer.polarity_scores(translated_content)
    review['translated_content'] = translated_content
    review['sentiment'] = sentiment_score

# Output the reviews with sentiment analysis
for review in swahili_reviews:
    print(review)
