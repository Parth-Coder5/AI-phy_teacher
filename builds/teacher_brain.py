from class11.motion_1d.distance_displacement import distance_vs_displacement
from class11.motion_1d.speed_velocity import speed_vs_velocity
from class11.motion_1d.acc import acceleration
from class11.motion_1d.equations_motion import equations_of_motion
from class11.motion_1d.graphs_motion import graphs_motion


# ---------- Intent helpers ----------
def _wants_definition(q: str) -> bool:
    return any(
        kw in q
        for kw in [
            "define",
            "definition",
            "meaning",
            "what is",
            "kya hota hai",
            "kya hai",
        ]
    )


def _wants_nature(q: str) -> bool:
    return any(kw in q for kw in ["nature", "scalar", "vector", "type", "quantity"])


def _wants_formula(q: str) -> bool:
    return any(kw in q for kw in ["formula", "relation", "equation", "expression"])


def _wants_example(q: str) -> bool:
    return any(
        kw in q
        for kw in ["example", "samjha", "samjhao", "explain with", "numerical"]
    )


def _wants_practice(q: str) -> bool:
    return any(kw in q for kw in ["practice", "question", "exercise", "problems"])


def _wants_types(q: str) -> bool:
    return any(
        kw in q
        for kw in ["types", "type", "kind", "category", "classification", "variation"]
    )


def _wants_meaning(q: str) -> bool:
    return any(
        kw in q
        for kw in ["means", "meaning", "matlab", "description", "define", "explanation"]
    )


def _wants_use(q: str) -> bool:
    return any(
        kw in q
        for kw in ["usage", "when to use", "uses", "use", "used", "using"]
    )


def _wants_equation(q: str) -> bool:
    return any(
        kw in q
        for kw in ["equation of motion", "equations of motion", "eq of motion"]
    )


# ---------- Topic builders ----------

def _build_distance_displacement(parts: list[str], flags: dict) -> None:
    data = distance_vs_displacement

    if flags["definition"]:
        parts.append("DEFINITION:\n")
        parts.append("Distance: " + data["definition"]["distance"] + "\n")
        parts.append("Displacement: " + data["definition"]["displacement"] + "\n")

    if flags["nature"] and "nature" in data:
        parts.append("\nNATURE:\n")
        nature = data["nature"]
        parts.append(f"Distance: {nature['distance']}\n")
        parts.append(f"Displacement: {nature['displacement']}\n")

    if flags["formula"] and "formula" in data:
        parts.append("\nFORMULA:\n")
        formula = data["formula"]
        parts.append(f"Distance: {formula['distance']}\n")
        parts.append(f"Displacement: {formula['displacement']}\n")

    if flags["example"] and "example" in data:
        parts.append("\nEXAMPLE:\n")
        parts.append(data["example"] + "\n")

    if flags["practice"] and "practice_question" in data:
        parts.append("\nPRACTICE QUESTION:\n")
        parts.append(data["practice_question"] + "\n")


def _build_speed_velocity(parts: list[str], flags: dict) -> None:
    data = speed_vs_velocity

    if flags["definition"]:
        parts.append("DEFINITION:\n")
        parts.append("Speed: " + data["definition"]["speed"] + "\n")
        parts.append("Velocity: " + data["definition"]["velocity"] + "\n")

    if flags["nature"] and "nature" in data:
        parts.append("\nNATURE:\n")
        nature = data["nature"]
        parts.append(f"Speed: {nature['speed']}\n")
        parts.append(f"Velocity: {nature['velocity']}\n")

    if flags["formula"] and "formula" in data:
        parts.append("\nFORMULA:\n")
        formula = data["formula"]
        parts.append(f"Speed: {formula['speed']}\n")
        parts.append(f"Velocity: {formula['velocity']}\n")

    if flags["example"] and "example" in data:
        parts.append("\nEXAMPLE:\n")
        parts.append(data["example"] + "\n")

    if flags["practice"] and "practice_question" in data:
        parts.append("\nPRACTICE QUESTION:\n")
        parts.append(data["practice_question"] + "\n")


def _build_acceleration(parts: list[str], flags: dict) -> None:
    data = acceleration["definition"]

    if flags["definition"]:
        parts.append("DEFINITION:\n")
        parts.append("Acceleration: " + data["acceleration"] + "\n")

    if flags["types"] and "types" in data:
        parts.append("TYPES:\n")
        parts.append(data["types"]["uniform"] + "\n")
        parts.append(data["types"]["non-uniform"] + "\n")

    if flags["nature"] and "nature" in data:
        parts.append("\nNATURE:\n")
        parts.append(f"Nature: {data['nature']}\n")

    if flags["formula"] and "formula" in data:
        parts.append("\nFORMULA:\n")
        parts.append(f"Acceleration Formula: {data['formula']}\n")

    if flags["example"] and "example" in data:
        parts.append("\nEXAMPLE:\n")
        parts.append(data["example"] + "\n")

    if flags["practice"] and "practice-question" in data:
        parts.append("\nPRACTICE QUESTION:\n")
        parts.append(data["practice-question"] + "\n")


def _build_equations_of_motion(parts: list[str], flags: dict) -> None:
    data = equations_of_motion

    if flags["equation"] and "equations" in data:
        parts.append("EQUATIONS:\n")
        parts.append("First Equation: " + data["equations"]["first"] + "\n")
        parts.append("Second Equation: " + data["equations"]["second"] + "\n")
        parts.append("Third Equation: " + data["equations"]["third"] + "\n")

    if flags["meaning"] and "meaning" in data:
        parts.append("MEANING OF SYMBOLS:\n")
        meaning = data["meaning"]
        parts.append(f"u: {meaning['u']}\n")
        parts.append(f"v: {meaning['v']}\n")
        parts.append(f"a: {meaning['a']}\n")
        parts.append(f"t: {meaning['t']}\n")
        parts.append(f"s: {meaning['s']}\n")

    if flags["use"] and "when_to_use" in data:
        parts.append("\nWHEN TO USE:\n")
        use = data["when_to_use"]
        parts.append(f"First equation: {use['first']}\n")
        parts.append(f"Second equation: {use['second']}\n")
        parts.append(f"Third equation: {use['third']}\n")

    if flags["example"] and "example" in data:
        parts.append("\nEXAMPLE:\n")
        parts.append(data["example"] + "\n")

    if flags["practice"] and "practice_question" in data:
        parts.append("\nPRACTICE QUESTION:\n")
        parts.append(data["practice_question"] + "\n")


def _build_graphs_of_motion(parts: list[str], flags: dict, q: str) -> None:
    g = graphs_motion

    # Decide which graphs the user is asking about
    wants_position = any(
        kw in q for kw in ["position-time", "position time", "x-t", "xt graph", "x t graph"]
    )
    wants_velocity = any(
        kw in q for kw in ["velocity-time", "velocity time", "v-t", "vt graph", "v t graph"]
    )
    wants_acceleration = any(
        kw in q
        for kw in ["acceleration-time", "acceleration time", "a-t", "at graph", "a t graph"]
    )

    # If none specifically mentioned, explain all three
    if not (wants_position or wants_velocity or wants_acceleration):
        wants_position = wants_velocity = wants_acceleration = True

    if wants_position and "position_time" in g:
        pt = g["position_time"]
        parts.append("\nPOSITION-TIME (x-t) GRAPH:\n")
        parts.append(pt["meaning"] + "\n")
        parts.append(pt["important_points"] + "\n")

    if wants_velocity and "velocity_time" in g:
        vt = g["velocity_time"]
        parts.append("\nVELOCITY-TIME (v-t) GRAPH:\n")
        parts.append(vt["meaning"] + "\n")
        parts.append(vt["important_points"] + "\n")

    if wants_acceleration and "acceleration_time" in g:
        at = g["acceleration_time"]
        parts.append("\nACCELERATION-TIME (a-t) GRAPH:\n")
        parts.append(at["meaning"] + "\n")
        parts.append(at["important_points"] + "\n")

    if flags["practice"] and "practice_question" in g:
        parts.append("\nPRACTICE QUESTION:\n")
        parts.append(g["practice_question"] + "\n")


# ---------- Topic registry ----------
TOPICS = [
    {
        "name": "DISTANCE vs DISPLACEMENT",
        "keywords": ["distance", "displacement"],
        "builder": _build_distance_displacement,
    },
    {
        "name": "SPEED vs VELOCITY",
        "keywords": ["speed", "velocity"],
        "builder": _build_speed_velocity,
    },
    {
        "name": "ACCELERATION",
        "keywords": ["acceleration"],
        "builder": _build_acceleration,
    },
    {
        "name": "EQUATIONS OF MOTION",
        "keywords": ["equation of motion", "equations of motion", "eq of motion"],
        "builder": _build_equations_of_motion,
    },
    {
        "name": "GRAPHS IN MOTION",
        "keywords": [
            "graph",
            "graphs",
            "x-t",
            "position-time",
            "position time",
            "v-t",
            "velocity-time",
            "velocity time",
            "a-t",
            "acceleration-time",
            "acceleration time",
        ],
        "builder": _build_graphs_of_motion,
    },
]


def answer_question(question: str) -> str:
    q = question.lower()

    flags = {
        "definition": _wants_definition(q),
        "nature": _wants_nature(q),
        "formula": _wants_formula(q),
        "example": _wants_example(q),
        "practice": _wants_practice(q),
        "types": _wants_types(q),
        "meaning": _wants_meaning(q),
        "use": _wants_use(q),
        "equation": _wants_equation(q),
    }

    # If user didn't specify what exactly, default to definition
    if not any(flags.values()):
        flags["definition"] = True

    parts: list[str] = []

    for topic in TOPICS:
        if any(kw in q for kw in topic["keywords"]):
            if parts:
                parts.append("\n-----------------------------\n\n")

            parts.append(topic["name"] + "\n")

            builder = topic["builder"]
            if builder is _build_graphs_of_motion:
                builder(parts, flags, q)
            else:
                builder(parts, flags)

    if parts:
        return "".join(parts).strip()

    return (
        "Sorry, I can explain Distance, Displacement, Speed, Acceleration, "
        "Equations of Motion, Graphs of Motion and Velocity.\n"
        "Try asking things like:\n"
        "- Define distance and displacement\n"
        "- What is the nature of speed and velocity?\n"
        "- Give formula of acceleration\n"
        "- Give example and practice question on distance and displacement\n"
        "- Explain equations of motion or graphs of motion"
    )
