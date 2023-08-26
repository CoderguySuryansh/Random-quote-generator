import random

def generate_random_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
        "In the middle of every difficulty lies opportunity. - Albert Einstein",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The best way to predict the future is to create it. - Peter Drucker",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs"
    ]
    
    return random.choice(quotes)

# Generate and display a random quote
print(generate_random_quote())
