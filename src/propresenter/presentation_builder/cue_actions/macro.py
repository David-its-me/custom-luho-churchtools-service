from propresenter.pb_auto_generated.action_pb2 import Action
from propresenter.pb_auto_generated.basicTypes_pb2 import UUID, CollectionElementType
from propresenter.presentation_builder.uuid_generator import generate_random_uuid


def create_announcement_macro() -> Action:
    action = Action(
        name="Announcement (mit Timer)",
        isEnabled=True,
        uuid=generate_random_uuid(),
        type=Action.ACTION_TYPE_MACRO,
        macro=Action.MacroType(
            identification=CollectionElementType(
                parameter_uuid=UUID(string="5ddbfd5f-625c-4305-b6d7-d69cfaac78de"),
                parameter_name="Announcement (mit Timer)",
            )
        ),
    )
    return action
