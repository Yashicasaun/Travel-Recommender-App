import openai
import requests

# Set up OpenAI API credentials
openai.api_key = "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"

# Define user preferences
user_budget = 1000
user_destination = "Paris"
user_interests = ["museums", "food", "shopping"]
user_duration = 2

# Generate prompt for GPT-3 API
prompt = f"Recommend me a travel itinerary for {user_destination} with a budget of {user_budget} and interests in {', '.join(user_interests)}."

prompt2 = f"Recommend me a travel itinerary for {user_destination} for a duration of {user_duration} days and interests in {', '.join(user_interests)}."

# Call GPT-3 API to generate travel recommendations
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt2,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Extract recommended itinerary from GPT-3 response
itinerary = response.choices[0].text.strip()

# Use travel APIs to fetch additional information about the recommended itinerary
# For example, you could use the TripAdvisor API to fetch ratings and reviews for each recommended attraction or restaurant

# Present the recommended itinerary to the user
print("Here are your recommended travel plans:")
print(itinerary)
