from langchain.prompts import PromptTemplate
from abc import ABC, abstractmethod

class PromptFormator(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def format(self, vocab:str) -> str:
        pass

class DefaultPromptFormator(PromptFormator):
    def __init__(self):
        super().__init__()
        self.prompt_template = PromptTemplate(
            input_variables=["vocab"],
            template= """
Please provide a complete explanation of the term {vocab} in Markdown format. For each section, use **emphasized** formatting and present the information in either bullet points or a numbered list. Additionally, ensure that after completing each section, you move on to a new line. For the explanation, include its synonym, parts of speech, and other related parts of speech. Please remember to show the alternate vocabulary word if there are other parts of speech. Additionally, furnish term translation in 繁體中文 and subsequently present a few illustrative sentences in both English and 繁體中文(always English sentence first). after that, if you have any additional information about this word, please also show. But remember don't necessary to have whole part of Traditional Chinese. In conclusion, you need to provide following section : 1.term 2. synonym 3. parts of speech  4. related parts of speech 5. Illustrative Sentences 6. Additional Information. Additionally, from part 1 to part 5, please remember to have 繁體中文 translation follow english explaination. Don't need to provide conclusion or summary. Following is my example : **Term:** Apple 蘋果

**Synonym:**

- Pippin 蘋果點心
- Granny Smith 青蘋果
- Macintosh 麥金塔
- Honeycrisp 蜜蘋果
- Gala 嘉樂蘋果

**English Parts of Speech:**

1. apple (Noun) 蘋果: A round fruit with a sweet or tart taste, typically red, green, or yellow in color, and containing seeds.

**Other Parts of Speech:**

1. None 

**Illustrative Sentences:**

1. The apple fell from the tree and landed on my head. 蘋果從樹上掉下來砸到我的頭。
2. I like to eat apples because they are sweet and crunchy. 我喜歡吃蘋果，因為它們又甜又脆。
3. Apple pie is my favorite dessert. 蘋果派是我最喜歡的甜點。
4. I am allergic to apples, so I cannot eat them. 我對蘋果過敏，所以我不能吃它們。
5. The apple tree in my backyard is full of ripe apples. 我家後院的蘋果樹上結滿了成熟的蘋果。

**Additional Information:**

- Apples are a good source of vitamins, minerals, and antioxidants.
- Apples are used in a variety of dishes, including pies, cakes, and cider.
- Apples are a symbol of knowledge and temptation in many cultures.
- The apple is the national fruit of the United States.
"""
        )

    def format(self, vocab:str) -> str:
        return self.prompt_template.format(vocab=vocab)