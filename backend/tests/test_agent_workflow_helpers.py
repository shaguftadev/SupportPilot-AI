from app.agents.support_workflow.nodes import _json_from_text
from app.agents.support_workflow.nodes import route_ticket


def test_json_parser_handles_fenced_json():
    assert _json_from_text('```json\n{"category":"billing"}\n```') == {"category": "billing"}


def test_json_parser_returns_none_for_invalid_text():
    assert _json_from_text("not json") is None


def test_router_uses_valid_category():
    assert route_ticket({"route": "technical"}) == "technical"


def test_router_defaults_unknown_category():
    assert route_ticket({"route": "unknown"}) == "general"
