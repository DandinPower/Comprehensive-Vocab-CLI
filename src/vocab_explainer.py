from langchain.prompts import PromptTemplate
from .llm_handler import GeminiProHandler

class VocabExplainer:
    def __init__(self):
        self.vocab_explaination_template = PromptTemplate(
            input_variables=["word"],
            template="Please provide a comprehensive explanation of the term '{word}', including its synonym, English parts of speech, and other parts of speech. Additionally, furnish its translation in 繁體中文 and subsequently present a few illustrative sentences in both English and 繁體中文(always English sentence first). after that, if you have any additional information about this word, please also show.I'll give you an example : **Term:** Hacker\n**Synonym:** Cracker\n**English Parts of Speech:**\n1. Noun: A person who has a deep understanding of computer systems and networks and uses that knowledge to explore and manipulate them.\n2. Verb: To use one's knowledge of computer systems and networks to explore and manipulate them, especially in an unauthorized way.\n**Other Parts of Speech:**\n1. Adjective: Relating to or characteristic of a hacker.\n2. Adverb: In a manner characteristic of a hacker.\n**繁體中文翻譯:**\n1.名詞：黑客\n2.動詞：駭客\n**Illustrative Sentences:**\n1. He is a skilled hacker who can break into any system. 他是一名能夠攻破任何系統的熟練黑客。\n2. She was accused of hacking into the company's computer network. 她被控入侵公司電腦網路。\n3. The website was hacked and the user data was stolen. 該網站被駭客入侵，使用者數據被盜取。\n4. The hacker used a botnet to launch a DDoS attack on the website. 駭客使用殭屍網路對該網站發動 DDoS 攻擊。\n5. The hacker was able to bypass the security measures and gain access to the sensitive information. 駭客能夠繞過安全措施，獲取敏感資訊。"
        )
        self.llm_handler = GeminiProHandler()

    def explain(self, word):
        prompt = self.vocab_explaination_template.format(word=word)
        result = self.llm_handler.invoke(prompt)
        return result