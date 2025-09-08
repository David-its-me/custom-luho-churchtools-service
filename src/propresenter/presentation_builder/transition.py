from propresenter.pb_auto_generated.effects_pb2 import Transition, Effect
from propresenter.presentation_builder.uuid_generator import generate_random_uuid


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

def dissolve_transition(transition_duration: float) -> Transition:
    return Transition(
        duration=transition_duration,
        effect=Effect(
            category="Dissolves",
            behavior_description="Dissolve",
            name="Dissolve",
            enabled=True,
            uuid=generate_random_uuid(),
            render_id="EC52A828-AD85-4602-B70C-1DEE7C904DB6"
        ),
    )

