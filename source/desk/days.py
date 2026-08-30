from desk.dialog import Dialog, Voice
from desk.world import SylwesterLook

global_dictionary = {"days": 1, "burned_documents": 0, "mistakes": 0}

documents_to_burn = [15, 21, 25, 30, 50, 50]
spawned_documents = [5, 7, 10, 15, 20, 25]

message_1 = [
    "Hi! I'm Sylwester!",
    "I'm the boss here",
    "This place is called H.E.L.L.",
    "You can call me also the Devil",
    "You were sentenced here...",
    "for eternity",
    "But lucky you...",
    "...I have chosen YOU...",
    "...to serve as my worker in...",
    "...H.E.L.L. bureaucracy",
    "See this furnace on your right?",
    "You wanna keep it at 666°C",
    "If it drops below 555°C...",
    "...then you will be...",
    "...fired and sent...",
    "...back to literal hell",
    "But if it ever goes...",
    "...above 777°C...",
    "...then it potentially...",
    "...may explode",
    "Why 777°C?",
    "Well, we order it from..",
    "H.E.A.V.E.N. and its Mirek's...",
    "...I mean God's...",
    "...favorite number...",
    "...or something",
    "Either way, you...",
    "...don't wanna go...",
    "...above this temperature...",
    "...because if you do...",
    "...then I will guarantee more...",
    "...suffering to you",
    "Got it? Good",
    "So for the first day...",
    "...I don't have any...",
    "...special requests",
    "You just need to burn...",
    f"...{documents_to_burn[0]} documents before...",
    "the time runs out",
    "And remember that the...",
    "...documents with only...",
    "...virtues should be sent",
    "...to H.E.A.V.E.N",
    "They were lost...",
    "...somewhere in our...",
    "...bureaucracy",
    "You will have only...",
    "3 mistakes, before...",
    "...I will come",
    "Oh and you will need...",
    "...to wait for the...",
    "...temperature to...",
    "...stabilise",
    "So good luck in your...",
    "...new eternal work!",
]

message_2 = [
    "Hey!",
    "So remember when...",
    "...I told you about...",
    "...no special rules?",
    "So here it comes!",
    "Today you will need...",
    "...to burn every document...",
    "...that has the...",
    "...”procrastination” sin",
    "Oh, and you will need to...",
    f"...burn at least {documents_to_burn[0]}...",
    "...documents,",
    "So good luck in your...",
    "...second day of work!"
]

message_3 = [
    "Wow, you are...",
    "...still alive!",
    "Impressive",
    "Okay, so today's sin...",
    "...is ”lying”",
    "And you have to...",
    f"...burn {documents_to_burn[2]} documents",
    "See ya next day!"
]

message_4 = [
    "Oh, sorry for...",
    "...being late",
    "The banned sin...",
    "...today is ”theft”...",
    "...and you need to...",
    f"...burn at least {documents_to_burn[3]}...",
    "...documents",
    "Good luck!"
]

message_5 = [
    "Okay, no more...",
    "...talking",
    "The sin is ”betrayal”...",
    "and you need to burn...",
    f"{documents_to_burn[4]} documents",
    "See ya tomorrow"
]

message_6 = [
    "Okay, so...",
    "I will tell you...",
    "...a secret",
    "Nobody survived...",
    "...this long in...",
    "...this job",
    "You are the first one...",
    "...that made it to...",
    "...sixth day",
    "If you complete this...",
    "...day, then I will...",
    "...really employ you...",
    "So get back to the work.",
    "Most important day...",
    "...is waiting for you",
    "Good luck!"
]

test_m = ["Test"]

dialogs = [
    Dialog(message_1, Voice.SYLWESTER),
    Dialog(message_2, Voice.PHONE),
    Dialog(message_3, Voice.PHONE),
    Dialog(message_4, Voice.PHONE),
    Dialog(message_5, Voice.PHONE),
    Dialog(message_6, Voice.SYLWESTER),
]

list_of_banned_sins = [
    None,
    "Procrastination",
    "Lying",
    "Theft",
    "Betrayal",
    "Murder"
]

world_sylwester = [
    SylwesterLook.SYLWESTER,
    None,
    None,
    None,
    None,
    SylwesterLook.SYLWESTER
]

dialogs_sylwester = [
    Voice.SYLWESTER,
    Voice.PHONE,
    Voice.PHONE,
    Voice.PHONE,
    Voice.PHONE,
    SylwesterLook.SYLWESTER
]

message_you_lost = ["You are fired"]

dialog_you_lost = Dialog(message_you_lost, Voice.SYLWESTER)
dialog_you_lost.should_draw = False