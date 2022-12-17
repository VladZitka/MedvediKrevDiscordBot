"""File for handling reponses."""
import typing
import random
import re

HELP_STRING =\
"""```
Basic funcitonality is:

- Say hello:
    if you say Hello or hello you'll get "Hello there!" as a response
- Get general kenobi:
    if you say Hello there you'll get "General Kenobi!" response
- Roll a dice:
    if you say 'roll n' for n in (4, 6, 8, 10, 12, 20, 100) you'll get a random
    number response in the range of 1 to n
- Get Help:
    if you say "!help" you'll print this message.
```"""


def handle_response(message: str) -> typing.Optional[str]:
    """Handle process the message and return a reposnse.

    Args:
        message: message to be processed.
    """
    p_message = message.lower()


    if "hello" == p_message:
        return "Hello there!"

    if "hello there" in p_message:
        return "General Kenobi!"

    if ("roll" in p_message) or ("hod" in p_message):
        print(f"processing {p_message}")
        return handle_possible_rolls(p_message)

    if "!help" == p_message:
        return HELP_STRING

    return None


def handle_possible_rolls(message: str) -> typing.Optional[str]:
    """Return random number or nothing if regex is matched."""
    possible_ways_to_say_roll: list[re.Pattern] = [
        r"(roll\s\d+\s*)",
        r"(hod\s\d+\s*)",
        r"(hod\ssi\s\d+\s*)"
    ]
    for pattern in possible_ways_to_say_roll:
        match = re.search(pattern, message)
        if match:
            roll_request = message[match.start(): match.end()]
            number_match = re.search(r"\d+", roll_request)
            max = int(roll_request[number_match.start(): number_match.end()])
            return str(random.randint(1,max))