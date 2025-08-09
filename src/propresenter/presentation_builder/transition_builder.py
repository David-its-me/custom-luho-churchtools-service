from propresenter.pb_auto_generated.effects_pb2 import Transition, Effect
from propresenter.presentation_builder.uuid_builder import generate_random_uuid


def cube_transition(transition_duration: float) -> Transition:
    return Transition(
        duration=transition_duration,
        effect=Effect(
            category="Objects",
            behavior_description="Cube",
            name="Cube",
            enabled=True,
            uuid=generate_random_uuid(),
            render_id="CD545FC3-70FA-4120-8A48-29EFE903BD10",
        ),
    )
