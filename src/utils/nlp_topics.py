from collections import Counter
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)


class TopicExtractor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def extract_keywords(self, texts):
        """Top words as topics."""
        all_text = ' '.join(texts).lower()
        words = nltk.word_tokenize(all_text)
        filtered = [w for w in words if w.isalpha()
                    and w not in self.stop_words]
        return Counter(filtered).most_common(20)
