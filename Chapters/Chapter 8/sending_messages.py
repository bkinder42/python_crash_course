def send_messages(message_queue, sent_messages):
    while message_queue:
        message = message_queue.pop()
        print(f"{message}\n")
        sent_messages.append(message)

messages = [
    "What wonderful weather we're having today",
    "The evil league of evil has got your application.",
    "It's hi-ho silver, signed that horse!",
    "The pool on the roof must have a leak...",
    "New Atlanta. Sector 11. Building 71-G. 5 April, year 2072. \n11:36pm: "
    "Hacker gains unauthorized access to the TriOptimum Corporate Network\n"
    "1:26am: Hacker attempts to access confidential files concerning space "
    "station citadel.\n1:33am: TriOptimum security forces apprehend the "
    "intruder.",
    "Hack the Planet!"
    ]

sent_messages = []

send_messages(messages, sent_messages)

print(messages)
print(sent_messages)