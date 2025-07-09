import nltk
import regex as re
from nltk.corpus import words

word_list = set(words.words())

def is_dictionary_word(password):
    return password.lower() in word_list

# Example structure for analyze_password
def analyze_password(password):
    strength_score = 0
    suggestions = []

    if len(password) >= 8:
        strength_score += 1
    else:
        suggestions.append("Increase password length (at least 8 characters).")

    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        suggestions.append("Include uppercase letters.")

    # ... (add checks for lowercase, numbers, special chars)

    if not re.search(r'(123|abc|password|qwerty)', password, re.IGNORECASE):
        strength_score += 1
    else:
        suggestions.append("Avoid common patterns and dictionary words.")

    # ... (add check for dictionary word if NLTK is used)

    if not re.search(r'(.)\1{2,}', password):
        strength_score += 1
    else:
        suggestions.append("Avoid repeating characters.")

    # Determine strength level based on score
    if strength_score <= 2:
        strength_feedback = "Very Weak"
    elif strength_score == 3:
        strength_feedback = "Weak"
    elif strength_score == 4:
        strength_feedback = "Moderate"
    elif strength_score == 5:
        strength_feedback = "Strong"
    else:
        strength_feedback = "Very Strong" # More criteria = higher max score

    return strength_feedback, suggestions