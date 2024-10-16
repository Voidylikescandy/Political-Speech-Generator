from deccan_scrapper import DeccanWebScraper
from hindu_state_scrapper import HinduStateScraper

slogans = """
Bari Bari Sab Ki Bari, Ab Ki Bari Atal Bihari
This was BJP's slogan when it came to power for the first time for a 13 day rule. The slogan was chanted at Lucknow election rally, in March 1996.

Sonia Nahi Yeh Aandhi Hai, Doosri Indira Gandhi Hai
In 2009, this slogan was coined by the Congress party to popularize Sonia Gandhi as the second Indira Gandhi.

UP Mein Hai Dum, Kyunki Jurm Hai Yahan Kam
The slogan was projected by Amitabh Bachchan where he gave a clean chit to Samajwadi Party by suggesting that criminal records are comparatively low in the Uttar Pradesh, during 2007 elections.

UP Mein Tha Dam, Lekin Kahan Pahuch Gaye Hum
Here, Congress targeted the Samajwadi Party and also replied to Amitabh Bachchan's advertisement with this slogan.

Bachcha Bachcha Ram ka, Janmabhoomi Ke Kaam ka
Such slogan was coined by Vishwa Hindu Parishad (VHP) sending the message of Hindutva, during election campaigns dividing country on a communal basis.

Jab Tak Rahega Samose Mein Aloo, Tab Tak Rahega Bihar Mein Lalu
This is one of the funniest election campaigns where Lalu Prasad Yadav was projected as the original leader of Bihar.

Jab Tak Sooraj Chand Rahega, Indira Tera Naam Rahega
This election slogan was coined by the Congress for 1984 elections after Indira Gandhi's assassination which led to a massive victory of the party.

Indira Hatao, Desh Bachao
Jayaprakash Narayan's Janata Party played this slogan for Indira Gandhi's campaign.

Bidi Mein Tambaku Hai, Congress-Wala Daaku Hai
In the elections of 1967, Bhartiya Jan Sangh asked the voters to reject both Congress and tobacco.

Abki Bar Modi Sarkar
Known for promoting, "Acche Din", this was one of the most popular election slogans that spread like wildfire and resulted in the massive victory of Bhartiya Janata Party, being Narendra Modi elected as the Prime Minister of India in 2014.
"""

opening = """
"What makes a country truly great? Is it the power of its leaders or the strength of its people? Today, I stand before you, not just as a voice but as a reflection of your dreams, your struggles, and your unwavering spirit. Together, we will shape the future we all deserve."

"They say power lies with the people. So, if you had the power to change one thing about our country, what would it be? As I look out at this sea of hope and resilience, I know that we are ready to make those changes, together."

"Leadership isnt about holding a position; its about holding a vision for the future. And today, as I stand here, it is your vision, your dreams that guide me. Thank you for allowing me the privilege of walking this path with you."

"Do you ever wonder why you should listen to any leader at all? Well, it's not just about listening—it's about being heard. And today, I am here because your voice is what truly matters. Lets make sure the future reflects that."
"""

farmer_stories = """
EXAMPLE FARMER STORIES:

[Story 1 Style - Conversation between Leader and the Farmer]:
I still remember the day I met Bhairav Singh, a farmer like many of you, standing in his dry, cracked field. His face was lined with worry, and his voice heavy with frustration. He looked at me and said, “Saab, every year I work my land, but the weight of loans, corrupt officials, and unfair policies crush me. Ive lost faith. This government doesnt care about farmers like us.”
His words broke my heart, because I knew he wasnt alone. Many of you have faced the same struggles—endless loans, lost land, and corrupt systems blocking your progress. I promised Bhairav that day, “If given the chance, I will fight for you. I will end this corruption and bring justice to the farmers.”
And today, I stand before you, after bringing those promises to life. We introduced fair loan schemes, land reforms, and crushed the corrupt systems that once strangled your livelihoods.
Last week, I visited Bhairav again. This time, his fields were green, and his face shone with joy. He fell to his knees, tears in his eyes, and said, “Saab, you saved us. My family eats, my land thrives, and my debt is gone. You gave us back our dignity.”
That happiness, that pride, is what I promised to every farmer. We are no longer bound by broken promises. Together, we have created a future where our farmers stand tall again.
[End of Story 1]

"""

humour = """

"""

scientific_facts = """

"""


# List of South Indian states in lowercase and hyphenated
south_states = [
    "tamil-nadu",
    "kerala",
    "karnataka",
    "andhra-pradesh",
    "telangana"
]

# List of all Indian states excluding the South Indian states
north_states = [
    "jammu-and-kashmir",
    "himachal-pradesh",
    "punjab",
    "uttarakhand",
    "haryana",
    "uttar-pradesh",
    "rajasthan",
    "chandigarh",
    "madhya-pradesh",
    "chhattisgarh",
    "bihar",
    "jharkhand",
    "west-bengal",
    "odisha",
    "sikkim",
    "assam",
    "arunachal-pradesh",
    "manipur",
    "meghalaya",
    "mizoram",
    "nagaland",
    "tripura",
    "ladakh",
    "goa"
]

class SpeechGenerator:
    def __init__(self, querier, translator, sentiment_analyzer, liwc_analyzer):
        self.querier = querier
        self.translator = translator
        self.sentiment_analyzer = sentiment_analyzer
        self.liwc_analyzer = liwc_analyzer

    def generate_base_speech(self,speech, requirements, state):
        prompt = """Read the instructions carefully to generate the output with tone, facial expressions, and emotions that aptly suit each statement.\n\n"""
        prompt += requirements
        prompt += "\n\n"
        prompt += f"""Generate the speech based on the given context and requirements.
            1. Introductory Statements in Local Language (Emotional and Cultural Bridge):
                Begin with a culturally resonant greetings. use regional dialects to trigger
                familiarity and trust. 
            3. Express how proud the speaker is to be able to communicate with the audience, express gratitude towards them. 
            4. For each statement, add annotations for tone, facial expressions, and emotions in parentheses. Add annotations wherever necessary - in the beginning of a sentence, in between, at the end, so on. For example: 'Ladies and gentlemen[Cheerful tone, hands opened towards the audience], my friends of Tamil Nadu, it's truly an honor to stand before you[moving right hand from up to down] here in Chennai today, as we prepare for the crucial MP elections! [Warm smile, hands clasped together, short pause]'
           """
        # prompt += opening
        # prompt += "\n\nSpeech:\n"
        # prompt += speech
        prompt += "\n\n"
        # prompt += """Incorporate a single catchy, proactive catchphrase. This is to build the bridge between the leader and the audience. Make the slogan rhyming to make it catchy. Print the slogans in English only. 
        # First, understand the context of the speech. Generate a slogan which matches the context of the speech given and integrate it smoothly into the opening.
        # And use it 
        #     1. In the speech in the beginning
        #     2. In between few paragraphs 
        #     3. And at the end.
        # Use it in places where it makes most sense which provide strength to the slogan. 
        # Here are some example slogans, generate a new slogan based on these."""
        # prompt += "\n\nExample Slogans:\n"
        # prompt += slogans
        # prompt += "\n\nYour response must be an annotated speech only following the given requirements as well as a catchy slogan embedded within the speech at few places."
        return self.querier.query(prompt)
    
    def include_a_story(self, speech):
        prompt = """Append a compelling and heart touching story to the speech given.
        1. Ensure that the story is integrated seamlessly in between, just for a short paragraph, enhancing the speech without disrupting its structure.
        2. Blend the story into the speech seamlessly, it is fine if the speech is elongated, a comprehensive speech is good.
        3. Make the story resonate with the audience, make them relate, make the speech sound human.
        Here is an example story, create similar ones or improve the examples."""
        prompt += "\n\n"
        prompt += farmer_stories
        prompt += "\n\nYour response must be an annotated speech following the given requirements. Make sure the base speech is inherited in your response."
        return self.querier.query(prompt)
        
    
    def append_web_scraped_data(self, speech, web_scraped_data):
      prompt = """You have been provided with some web-scraped data and a base speech. There are 7 tasks.
      1. Your task is to include some parts of the web-scraped data into the base speech in such a way that the flow of the speech remains smooth and natural.
      2. Ensure that the data is integrated seamlessly, enhancing the speech without disrupting its structure.
      3. Blend the web-scraped data into the final speech seamlessly, it is fine if the speech is elongated, a comprehensive speech is good.
      4. Do not include data which feels out of place and cannot be merged into the speech.
      5. Do not include too much statistical information, 5-6 instances of them are enough, choose the ones which best fit the context and have a stronger effect on the audience.
      6. Do not present statistical data starting with "Recent reports", "Recent times", "Recent studies", "Regarding" etc. Weave them into the speech like they are a part of the story.
      7. Group related information paragraphs together to ensure the flow is not broken.
      
      Base Speech:
      """
      prompt += speech
      prompt += "\n\nWeb-Scraped Data:\n"
      prompt += web_scraped_data
      prompt += "\n\nYour response must be a speech embedded with web scraped data."

      return self.querier.query(prompt)
    
    def final_check(self, speech):
        prompt = """Alright, here is the final speech after appending webscraped data. 
        Now what I would like to do is do one final check.
        1. Check if the speech is strong and captivating.
        2. Make necessary improvements in vocabulary or sentence phrasing if it makes the speech better.
        3. Do not change core of the speech. The speech is supposed to be annotated, mixed with webscraped data and the speech should sound human.
        4. In case there are sentences which do not fit the context or there are paragraphs where a smooth transition from previous paragraph is missing, enhance the speech in these areas.
        5. In case no enhancement is able to keep the speech smooth, remove such information, but keep removal to a minimum.
        6. In case there are named entities in the speech (for example, states like Andhra Pradesh, Telangana or people) ensure that the information regarding them is properly integrated into the speech in a smooth fashion. Don't make the paragraphs look disjoint.
        8. The stories involved should have a fulfilling ending matching the context of the speech.
        9. Any additions made to the speech should be annotated properly.
        10. At last, make the speech perfect."""
        prompt += "\n\nSpeech:\n"
        prompt += speech
        prompt += "\nYour response should be an enhanced speech, with human touch, captivating, heart touching, retaining most of the previous structure, annotations and information."

        return self.querier.query(prompt)


#     def get_metrics(self, speech):
#         prompt = """You need to assess the following 5 personality traits from the below speech by giving it a score of 1 to 10 (discrete values) where 10 is the highest score and 1 is the lowest score (use floor value):
#     (Agreeableness, Conscientiousness, Extraversion, Emotional range, Openness). Output should only be the scores with no extra text or information. Then regenerate the speech to improve the metrics and also sound more human.\n\n"""
#         prompt += speech
#         return self.querier.query(prompt)

#     def enhance_eq_score(self, speech):
#         sentiment = self.sentiment_analyzer.get_sentiment(speech)
#         emotional_quotient = self.sentiment_analyzer.get_emotional_quotient(speech)
#         prompt = """You are provided with speech and its Sentiment and Emotional Quotient. Add words to the speech such that the emotional quotient improves. Regenerate the speech accordingly.\n\n"""
#         prompt += speech
#         prompt += f"\nSentiment: {sentiment}\nEmotional Quotient: {emotional_quotient}"
#         return self.querier.query(prompt)

#     def enhance_liwc_metrics(self, speech):
#         filtered_categories = self.liwc_analyzer.get_categories(speech)
#         prompt = """You need to improvise the given speech text based on the provided information of Linguistic Inquiry and Word Count (LIWC).\n\n The Speech is: \n"""
#         prompt += speech
#         prompt += "\nLIWC information: \n\n"
#         prompt += str(filtered_categories)
#         return self.querier.query(prompt)

#     def prime_speech(self, speech):
#         prompt = """You need to assess the following speech for primings namely Issue Priming, Candidate Attributes Priming, Mood and Emotional Priming, Social Identity Priming, Economic Priming, Value-Based Priming, Repetition and Consistency, Visual and Symbolic Priming, Use of Surrogates and Endorsements, Framing and Issue Association, Contextual Priming. Give a rating for each metric on the scale of 10. 1 is the lowest and 10 is the highest.
# Then, regenerate the speech by improving those metrics and make it sound more human. Output should only consist of the regenerated speech and nothing else. Do not even give any heading as Regenerated Speech, output should only be the regenerated speech itself.\n\n"""
#         prompt += speech
#         return self.querier.query(prompt)

    def strip_text(self, speech):
        lines = speech.split("\n")
        filtered_lines = [line for line in lines if len(line.split()) > 1]
        filtered_text = "\n".join(filtered_lines)
        return filtered_text

    def translate_speech(self, speech, language):
        return self.translator.translate(speech, language)

    def generate_speech(self, speech, requirements, newspaper, state, language="en"):

        base_speech = self.generate_base_speech(speech, requirements, state)
        print('*' * 80)
        print(base_speech)
        print('*' * 80)

        # story_included_speech = self.include_a_story(base_speech)
        # print('*' * 80)
        # print(story_included_speech)
        # print('*' * 80)

        # words = ['bjp', 'modi']
        # state = state.lower().replace(" ", "-")
        # print(state)
        # print(words)

        # if newspaper == "Deccan Chronicle":
        #     url="https://www.deccanchronicle.com/location/india/"+state
        #     scraper = DeccanWebScraper(
        #         base_url=url,
        #         keywords=words,
        #         num_pages_to_scrape=15
        #     )
        #     headlines_data = scraper.extract_headlines_from_multiple_pages()
        #     filtered_headlines = scraper.filter_headlines_by_keywords(headlines_data)
        #     text_content = scraper.extract_information_from_headlines(filtered_headlines)
        #     data_filtered_text_content = scraper.extract_sentences_with_numerical_data(text_content)
        #     scraper.save_to_file(data_filtered_text_content, "web_scraped_data.txt")
        #     web_scraped_data = "\n".join(data_filtered_text_content)
        # elif newspaper == "The Hindu (States)":
        #     url = "https://www.thehindu.com/news/national/" + state
        #     scraper = HinduStateScraper(
        #         base_url=url,
        #         keywords=words,
        #         num_pages_to_scrape=9
        #     )
        #     headlines_data = scraper.extract_headlines_from_multiple_pages()
        #     filtered_headlines = scraper.filter_headlines_by_keywords(headlines_data)
        #     text_content = scraper.extract_information_from_headlines(filtered_headlines)
        #     data_filtered_text_content = scraper.extract_sentences_with_numerical_data(text_content)
        #     scraper.save_to_file(data_filtered_text_content, "web_scraped_data.txt")

        # web_scraped_data_integrated_speech = self.append_web_scraped_data(base_speech, web_scraped_data)
        # print('*' * 80)
        # print(web_scraped_data_integrated_speech)
        # print('*' * 80)

        # final_speech = self.final_check(base_speech)
        # print('*' * 80)
        # print(final_speech)
        # print('*' * 80)

        filtered_speech = self.strip_text(base_speech)
        print('*' * 80)
        print(filtered_speech)
        print('*' * 80)


        if language != "en":
            translated_speech = self.translate_speech(filtered_speech, language)
            return translated_speech

        return filtered_speech
