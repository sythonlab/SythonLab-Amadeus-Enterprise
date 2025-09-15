from dataclasses import dataclass


@dataclass
class AvailabilityItinerary:
    ref: int
    departing_from: str
    arriving_to: str
    date: str


@dataclass
class AvailabilityPassenger:
    type: str
