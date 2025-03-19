from flask import Blueprint, jsonify
from flask import Blueprint, jsonify, request
from src.validators.events_creator_validator import events_creator_validator
from src.http_types.http_request import HttpRequest
from src.controllers.events.events.creator import EventsCreator
from src.model.repositories.eventos_repository import EventosRepository

event_route_bp = Blueprint("event_route", __name__)


@event_route_bp.route("/event", methods=["POST"])
def create_new_event():
    return jsonify({ "estou": "aqui" }), 201 # noqa
    events_creator_validator(request)
    http_request = HttpRequest(body=request.json)

    eventos_repo = EventosRepository()
    eventos_creator = EventsCreator(eventos_repo)

    http_response = eventos_creator.create(http_request)

    return jsonify(http_response.body), http_response.status_code