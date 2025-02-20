"""Generic base class for websocket events."""

from typing import Any


class WebsocketEvent:
    """Base class defining a generic websocket event.

    Attributes
    ----------
    event_type : str
        The event type.
    data : dict
        The event data.
    broadcast : dict
        Information about who the event was sent to.
    seq : int
        Sequence number set by the client.

    """

    def __init__(self, event: dict[str, Any]) -> None:
        """Initialize the attributes.

        Parameters
        ----------
        event : dict
            The websocket event as a JSON.

        Raises
        ------
        KeyError
            If either event, data, broadcast or seq is missing.

        """
        self.event_type: str = event["event"]
        self.broadcast: dict[str, Any] = event["broadcast"]
        self.seq: int = event["seq"]
