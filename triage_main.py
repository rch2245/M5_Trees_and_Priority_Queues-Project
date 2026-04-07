"""Driver program for the TriageSystem class.
"""

from triage_system import TriageSystem


# (name, severity) in arrival order, taken from the project instructions.
TEST_PATIENTS = [
    ("Sofia", 5),
    ("Bob", 2),
    ("Charlie", 4),
    ("Diana", 3),
    ("Eli", 1),
    ("Tom", 4),
    ("Alice", 5),
    ("Rachel", 4),
]


def main():
    """Add the test patients and process them in triage order."""
    triage = TriageSystem()
    for name, severity in TEST_PATIENTS:
        triage.add_patient(name, severity)

    print("Processing patients:")
    while not triage.is_empty():
        name, severity = triage.process_next()
        print(f"Now treating: {name} (Severity {severity})")


if __name__ == "__main__":
    main()
