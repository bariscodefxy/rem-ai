from chatbot import Chat, register_call
import wikipedia

class MessagingManager():

    def __init__(self, rem):
        self.rem = rem

    @register_call("whoIs")
    def who_is(self, session, query):
        try:
            return wikipedia.summary(query)
        except Exception:
            for new_query in wikipedia.search(query):
                try:
                    return wikipedia.summary(new_query)
                except Exception:
                    pass
        return "I don't know about "+query

    def run(self):
        first_question="Hi, how are you?"
        Chat("./Chats/chat.template").converse(first_question)
