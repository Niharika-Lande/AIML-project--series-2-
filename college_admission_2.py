class AdmissionChatbot:
    def init(self):
        self.context = {}

    def greet(self):
        return "Hello! I'm here to help you with college admissions. How can I assist you today?"

    def farewell(self):
        return "Goodbye! If you have any more questions, feel free to ask. Have a great day!"

    def respond(self, user_input):
        responses = {
            "admission procedure": "The admission procedure involves filling out an online application, submitting required documents. Would you like more details on any specific step?",
            "requirements": "The admission requirements include a completed application form, high school transcripts and a personal statement.",
            "fees":"1 Lakh per annum",
            "What is the student-faculty ratio at your college?":"the student-faculty ratio at our college is  this means that for every  students, there is one faculty member available to provide personalized attention and support.",
            "Campus Life":" our campus provides a vibrant and diverse community for students. we have numerous student organizations, clubs, and recreational facilities.",
            "Financial Aid and Scholarships": "we offer various types of financial aid including grants, loans, and work-study opportunities. to apply for scholarships, you can fill out our scholarship application form and also explore external scholarship options. merit-based scholarships are awarded based on academic achievements.",
            "Are there study abroad programs available?":"Yes, our college offers study abroad programs for students like IELTS,TOEFL",
            "contact information": "You can contact the admissions office at admissions@BVRIT.edu or call us at (123) 456-7890.",
        }

        user_input_lower = user_input.lower()
        for key, response in responses.items():
            if key in user_input_lower:
                return response
        
        return "I'm sorry, I didn't understand that. Could you please rephrase your question?"

    def remember_context(self, key, value):
        self.context[key] = value

    def recall_context(self, key):
        return self.context.get(key, None)

    def ask_questions(self):
        questions = [
            "Which program are you interested in?",
            "Do you have any specific questions about the admission process?",
            "Would you like information on scholarships?"
        ]

        answers = {}
        for question in questions:
            print(question)
            answer = input()
            answers[question] = answer
            self.remember_context(question, answer)
        
        return answers

    def handle_interaction(self):
        print(self.greet())
        while True:
            user_input = input()
            if "bye" in user_input.lower():
                print(self.farewell())
                break
            response = self.respond(user_input)
            print(response)
            if response.startswith("The admission procedure"):
                print("Would you like more details on any specific step?")
            elif response.startswith("The application deadlines"):
                print("Do you need more information about any specific deadline?")

# Running the chatbot
chatbot = AdmissionChatbot()
chatbot.handle_interaction()