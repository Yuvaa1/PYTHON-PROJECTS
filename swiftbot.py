import random
import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses
pairs = [
    [
        r"(.*) favorite album(.*)",
        ["I love all of Taylor Swift's albums! Some fan favorites are '1989', 'Folklore', and 'Midnights'!"]
    ],
    [
        r"(.*) recommend a song for (happy|sad|love|breakup|party|chill) mood", 
        [
            "For a happy mood, try 'Shake It Off' or 'You Belong With Me'!",
            "For a sad mood, 'All Too Well' and 'The Archer' are masterpieces!",
            "For love, 'Lover' and 'Enchanted' are great choices!",
            "For a breakup, 'We Are Never Ever Getting Back Together' and 'Back to December' fit perfectly!",
            "For a party vibe, '22' and 'Me!' are iconic!",
            "For a chill mood, 'The Lakes' and 'Snow on the Beach' are soothing!"
        ]
    ],
    [
        r"(.*) favorite song(.*)",
        ["It's hard to pick just one! 'Enchanted', 'Cruel Summer', and 'Cardigan' are top-tier!"]
    ],
    [
        r"(.*) latest album(.*)",
        ["Taylor Swift's latest album is 'The Tortured Poets Department'. It's a must-listen!"]
    ],
    [
        r"(.*) Taylor Swift's real name(.*)",
        ["Her full name is Taylor Alison Swift!"]
    ],
    [
        r"(.*) won how many Grammys(.*)",
        ["As of 2024, Taylor Swift has won 14 Grammy Awards!"]
    ],
    [
        r"(.*) list all albums(.*)",
        ["Here are all of Taylor Swift's albums: \n1. Taylor Swift (2006) \n2. Fearless (2008) \n3. Speak Now (2010) \n4. Red (2012) \n5. 1989 (2014) \n6. Reputation (2017) \n7. Lover (2019) \n8. Folklore (2020) \n9. Evermore (2020) \n10. Midnights (2022) \n11. The Tortured Poets Department (2024)"]
    ],
    [
        r"(.*) tell me about Taylor Swift(.*)",
        ["Taylor Swift is an American singer-songwriter known for her storytelling in music. She was born on December 13, 1989, in Reading, Pennsylvania. She started as a country singer and transitioned into pop and indie-folk. She has won multiple awards, including 14 Grammy Awards, and is known for her albums like 'Fearless', 'Red', '1989', and 'Folklore'."]
    ],
    [
        r"quit", 
        ["Goodbye! Keep listening to Taylor Swift!"]
    ]
]

# Create chatbot instance
swiftbot = Chat(pairs, reflections)

def taylor_swift_chatbot():
    print("Hello! I'm a Taylor Swift chatbot. Ask me anything about her music!")
    while True:
        user_input = input(": ")
        if user_input.lower() == "quit":
            print("Goodbye! Keep listening to Taylor Swift!")
            break
        response = swiftbot.respond(user_input)
        print(response if response else "I'm not sure about that, but I love Taylor Swift!")

# Run chatbot
taylor_swift_chatbot()
