from desk.dialog import Dialog, Voice

day = [1]

documents_to_burn = [10, 15, 20, 25, 30, 35]
spawned_documents = [20, 30, 40, 50, 60, 70]

messages = [
    "Hi! I'm Sylwester!",
    "I'm the boss here",
    "This place is called H.E.L.L.",
    "You can call me also the Devil",
    "You were sentenced here...",
    "for the eternity",
    "But lucky you...",
    "...I have chosen YOU...",
    "...to serve as my worker in...",
    "...H.E.L.L. bureaucracy",
    "See this furnace on you right?",
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
    "Well we order it from..",
    "H.E.A.V.E.N. and it's Mireks's...",
    "...I mean God's...",
    "...favorite number...",
    "...or something",
    "Either way you...",
    "...don't wanna to go...",
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
    "So good luck in your...",
    "...new eternal work!"
]

test_message = ["Test"]

dialogs = [
    Dialog(test_message, Voice.SYLWESTER),
    Dialog(messages[0], Voice.SYLWESTER),
    Dialog(messages[0], Voice.SYLWESTER),
    Dialog(messages[0], Voice.SYLWESTER),
    Dialog(messages[0], Voice.SYLWESTER),
    Dialog(messages[0], Voice.SYLWESTER),
]

list_of_banned_sins = [
    None,
    ["Murder"]
]