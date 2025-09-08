
from propresenter.pb_auto_generated.basicTypes_pb2 import UUID
import random

def __random_character() -> str:
    return random.choice('0123456789abcdef')

def __random_character_string(length: int) -> str:
    character_string = ""
    for i in range(length):
        character_string = character_string + __random_character()
    return character_string

def generate_random_uuid() -> UUID:
    return UUID(
        string='{}-{}-{}-{}-{}'.format(
            __random_character_string(8),
            __random_character_string(4),
            __random_character_string(4),
            __random_character_string(4),
            __random_character_string(12),
        )
    )

def uuid_zero() -> UUID:
    return UUID(
        string="00000000-0000-0000-0000-000000000000"
    )