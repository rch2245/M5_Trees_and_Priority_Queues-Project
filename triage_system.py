"""Hospital triage system implemented as a priority queue using heapq.
"""

import heapq


class TriageSystem:
    """A priority queue of (name, severity) patients backed by heapq."""

    # Class-level monotonically increasing arrival counter shared across
    # all instances. Used to break severity ties in FIFO order.
    _arrival_counter = 0

    def __init__(self):
        """Create a new, empty triage system."""
        self._queue = []  # private heap of (-severity, arrival, name) tuples

    @staticmethod
    def next_arrival_order():
        """Return current arrival order value, then advance the counter."""
        order = TriageSystem._arrival_counter
        TriageSystem._arrival_counter += 1
        return order

    def add_patient(self, name, severity):
        """Insert a patient with the given name and severity (1-5)."""
        if not isinstance(name, str) or name == "":
            raise ValueError("Patient name must be a non-empty string")
        if not isinstance(severity, int) or not (1 <= severity <= 5):
            raise ValueError("Severity must be an integer in the range 1..5")

        arrival = TriageSystem.next_arrival_order()
        # Negate severity so the highest severity becomes the smallest key
        # in the min-heap. Arrival order then enforces FIFO tie-breaking.
        heapq.heappush(self._queue, (-severity, arrival, name))

    def process_next(self):
        """Remove and return the highest-priority patient, or None if empty."""
        if not self._queue:
            return None
        neg_sev, _arrival, name = heapq.heappop(self._queue)
        return (name, -neg_sev)

    def peek_next(self):
        """Return (without removing) the next patient, or None if empty."""
        if not self._queue:
            return None
        neg_sev, _arrival, name = self._queue[0]
        return (name, -neg_sev)

    def is_empty(self):
        """Return True if there are no patients in the queue."""
        return len(self._queue) == 0

    def size(self):
        """Return the number of patients currently in the queue."""
        return len(self._queue)

    def clear(self):
        """Remove all patients from the queue."""
        self._queue.clear()
