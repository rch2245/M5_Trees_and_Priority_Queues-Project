"""Hospital triage system priority queue using heapq."""

import heapq


class TriageSystem:
    """Priority queue of patients ordered by severity (high first), with FIFO tie-breaking."""

    # class-level counter so ties between instances stay in arrival order
    _arrival_counter = 0

    def __init__(self):
        self._queue = []

    def is_empty(self):
        """Return True if there are no patients in the queue."""
        return len(self._queue) == 0

    def size(self):
        """Return the number of patients in the queue."""
        return len(self._queue)

    def clear(self):
        """Remove all patients from the queue."""
        self._queue.clear()

    @staticmethod
    def next_arrival_order():
        """Return the next arrival number and advance the counter."""
        order = TriageSystem._arrival_counter
        TriageSystem._arrival_counter += 1
        return order

    def add_patient(self, name, severity):
        """Add a patient to the queue with the given severity (1-5)."""
        if not isinstance(name, str) or name == "":
            raise ValueError("Patient name must be a non-empty string")
        if not isinstance(severity, int) or not (1 <= severity <= 5):
            raise ValueError("Severity must be an integer between 1 and 5")

        # heapq is a min-heap, so negate severity to treat highest first
        arrival = TriageSystem.next_arrival_order()
        heapq.heappush(self._queue, (-severity, arrival, name))

    def process_next(self):
        """Remove and return the highest-priority patient, or None if empty."""
        if not self._queue:
            return None
        neg_sev, _, name = heapq.heappop(self._queue)
        return (name, -neg_sev)

    def peek_next(self):
        """Return the highest-priority patient without removing them."""
        if not self._queue:
            return None
        neg_sev, _, name = self._queue[0]
        return (name, -neg_sev)
