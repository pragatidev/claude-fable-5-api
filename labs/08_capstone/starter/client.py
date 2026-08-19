"""Capstone starter. Wire parse + refusal + fallback body.

This file is what the learner edits. Tests import handle() from here
after they copy the solution, or they implement handle() themselves.

The fixture suite must stay green without an API key.
"""

from __future__ import annotations

from typing import Any

# TODO: import first_text, handle_response, fallback_request_body, and the model IDs.


def handle(response: Any) -> dict[str, Any]:
    """Return a JSON-safe dict: ok, text, refused, category, model.

    Must not raise on a refusal fixture. Must not read content[0] blindly.
    """
    raise NotImplementedError("implement handle() using fable_client.handle_response")


def fallback_body(prompt: str) -> dict[str, Any]:
    """Return the server-side fallback request shape for this prompt."""
    raise NotImplementedError("implement fallback_body() using fallback_request_body")
