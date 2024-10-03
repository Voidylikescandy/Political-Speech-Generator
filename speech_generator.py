from deccan_scrapper import WebScraper

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

class SpeechGenerator:
    def __init__(self, querier, translator, sentiment_analyzer, liwc_analyzer):
        self.querier = querier
        self.translator = translator
        self.sentiment_analyzer = sentiment_analyzer
        self.liwc_analyzer = liwc_analyzer

    def generate_base_speech(self, speech, requirements):
        prompt = """Read the instructions carefully to generate the output with tone, facial expressions, and emotions that aptly suit each statement.\n\n"""
        prompt += requirements
        prompt += "\n\n"
        prompt += "Generate the speech based on the given context and requirements. Express how proud the speaker is to be able to communicate with the audience, express gratitude towards them. For each statement, add annotations for tone, facial expressions, and emotions in parentheses. Add annotations wherever necessary - in the beginning of a sentence, in between, at the end, so on. For example: 'Ladies and gentlemen[Cheerful tone, hands opened towards the audience], my friends of Tamil Nadu, it's truly an honor to stand before you[moving right hand from up to down] here in Chennai today, as we prepare for the crucial MP elections! [Warm smile, hands clasped together, short pause]'"
        prompt += "\n\nSpeech:\n"
        prompt += speech
        prompt += "\n\n"
        prompt += """Incorporate a single catchy, proactive catchphrase. This is to build the bridge between the leader and the audience. Make the slogan rhyming to make it catchy. Print the slogans in English only. First, understand the context of the speech, then generate a catchy slogan and use it in the speech in the beginning, in between few paragraphs and at the end. Use it in places where it makes most sense which provide strength to the slogan. Here are some example slogans, generate a new slogan based on these."""
        prompt += "\n\nExample Slogans:\n"
        prompt += slogans
        prompt += "\n\nYour response must be an annotated speech following the given requirements as well as a catchy slogan embedded within the speech at few places."
        return self.querier.query(prompt)
    
    def append_web_scraped_data(self, speech, web_scraped_data):
      prompt = """You have been provided with some web-scraped data and a base speech. 
      Your task is to include some parts of the web-scraped data into the base speech in such a way that the flow of the speech remains smooth and natural.
      Ensure that the data is integrated seamlessly, enhancing the speech without disrupting its structure.
      Blend the web-scraped data into the final speech seamlessly, it is fine if the speech is elongated, a comprehensive speech is good.
      Do not include data which feels out of place and cannot be merged into the speech.
      Do not include too much statistical information, 3-4 instances of them are enough, choose the ones which best fit the context and have a stronger effect on the audience.
      Do not present statistical data starting with "Recent reports". Wove them into the speech like they are a part of the story.
      
      Base Speech:
      """
      prompt += speech
      prompt += "\n\nWeb-Scraped Data:\n"
      prompt += web_scraped_data
      prompt += "\n\nYour response must be a speech embedded with web scraped data."

      return self.querier.query(prompt)


    def get_metrics(self, speech):
        prompt = """You need to assess the following 5 personality traits from the below speech by giving it a score of 1 to 10 (discrete values) where 10 is the highest score and 1 is the lowest score (use floor value):
    (Agreeableness, Conscientiousness, Extraversion, Emotional range, Openness). Output should only be the scores with no extra text or information. Then regenerate the speech to improve the metrics and also sound more human.\n\n"""
        prompt += speech
        return self.querier.query(prompt)

    def enhance_eq_score(self, speech):
        sentiment = self.sentiment_analyzer.get_sentiment(speech)
        emotional_quotient = self.sentiment_analyzer.get_emotional_quotient(speech)
        prompt = """You are provided with speech and its Sentiment and Emotional Quotient. Add words to the speech such that the emotional quotient improves. Regenerate the speech accordingly.\n\n"""
        prompt += speech
        prompt += f"\nSentiment: {sentiment}\nEmotional Quotient: {emotional_quotient}"
        return self.querier.query(prompt)

    def enhance_liwc_metrics(self, speech):
        filtered_categories = self.liwc_analyzer.get_categories(speech)
        prompt = """You need to improvise the given speech text based on the provided information of Linguistic Inquiry and Word Count (LIWC).\n\n The Speech is: \n"""
        prompt += speech
        prompt += "\nLIWC information: \n\n"
        prompt += str(filtered_categories)
        return self.querier.query(prompt)

    def prime_speech(self, speech):
        prompt = """You need to assess the following speech for primings namely Issue Priming, Candidate Attributes Priming, Mood and Emotional Priming, Social Identity Priming, Economic Priming, Value-Based Priming, Repetition and Consistency, Visual and Symbolic Priming, Use of Surrogates and Endorsements, Framing and Issue Association, Contextual Priming. Give a rating for each metric on the scale of 10. 1 is the lowest and 10 is the highest.
Then, regenerate the speech by improving those metrics and make it sound more human. Output should only consist of the regenerated speech and nothing else. Do not even give any heading as Regenerated Speech, output should only be the regenerated speech itself.\n\n"""
        prompt += speech
        return self.querier.query(prompt)

    def strip_text(self, speech):
        lines = speech.split("\n")
        filtered_lines = [line for line in lines if len(line.split()) > 1]
        filtered_text = "\n".join(filtered_lines)
        return filtered_text

    def translate_speech(self, speech, language):
        return self.translator.translate(speech, language)

    def generate_speech(self, speech, requirements, language="en"):

        base_speech = self.generate_base_speech(speech, requirements)
        print('*' * 80)
        print(base_speech)
        print('*' * 80)

        scraper = WebScraper(
            base_url='https://www.deccanchronicle.com/location/india/southern-states',
            keywords=['bjp', 'women', 'woman', 'farmer', 'farm', 'farming'],
            num_pages_to_scrape=5
        )
        headlines_data = scraper.extract_headlines_from_multiple_pages()
        filtered_headlines = scraper.filter_headlines_by_keywords(headlines_data)
        text_content = scraper.extract_information_from_headlines(filtered_headlines)
        data_filtered_text_content = scraper.extract_sentences_with_numerical_data(text_content)
        web_scraped_data = "\n".join(data_filtered_text_content)

        web_scraped_data_integrated_speech = self.append_web_scraped_data(base_speech, web_scraped_data)
        print('*' * 80)
        print(web_scraped_data_integrated_speech)
        print('*' * 80)


        # personality_improved_speech = self.get_metrics(web_scraped_data_integrated_speech)
        # print('*' * 80)
        # print(personality_improved_speech)
        # print('*' * 80)


        # eq_improved_speech = self.enhance_eq_score(personality_improved_speech)
        # print('*' * 80)
        # print(eq_improved_speech)
        # print('*' * 80)


        # liwc_improved_speech = self.enhance_liwc_metrics(eq_improved_speech)
        # print('*' * 80)
        # print(liwc_improved_speech)
        # print('*' * 80)



        # primed_speech = self.prime_speech(liwc_improved_speech)
        # print('*' * 80)
        # print(primed_speech)
        # print('*' * 80)


        filtered_speech = self.strip_text(web_scraped_data_integrated_speech)
        print('*' * 80)
        print(filtered_speech)
        print('*' * 80)


        if language != "en":
            translated_speech = self.translate_speech(filtered_speech, language)
            return translated_speech

        return filtered_speech
