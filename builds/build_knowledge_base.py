from class11.motion_1d.distance_displacement import distance_vs_displacement
from class11.motion_1d.speed_velocity import speed_vs_velocity
from class11.motion_1d.acc import acceleration
from class11.motion_1d.equations_motion import equations_of_motion
from class11.motion_1d.graphs_motion import graphs_motion

TOPICS = [
    ("distance_displacement", distance_vs_displacement),
    ("speed_velocity", speed_vs_velocity),
    ("acceleration", acceleration),
    ("equations_of_motion", equations_of_motion),
    ("graphs_motion", graphs_motion),
]


def topic_to_chunks(name, data):
    chunks = []

    def _add_chunks(section_prefix: str, value):
        # Leaf string: turn into a chunk if it's non-trivial (> 3 words)
        if isinstance(value, str):
            if len(value.split()) > 3:
                chunks.append(
                    {
                        "topic": name,
                        "section": section_prefix,
                        "text": value,
                    }
                )
        # Nested dict: recurse into sub-keys
        elif isinstance(value, dict):
            for key, val in value.items():
                new_prefix = f"{section_prefix}.{key}" if section_prefix else key
                _add_chunks(new_prefix, val)

    if isinstance(data, dict):
        for key, value in data.items():
            _add_chunks(key, value)

    return chunks

import json

def build_kb():
    all_chunks = []

    for name,topic in TOPICS:
        chunks = topic_to_chunks(name,topic)
        all_chunks.extend(chunks)
    return all_chunks

if __name__ == '__main__' :
    kb = build_kb()

    with open("knowledge_base.json", "w", encoding="utf-8") as f:
        json.dump(kb,f, indent=2)
    
    print(f"Knowledge base created with {len(kb)} chunks.")