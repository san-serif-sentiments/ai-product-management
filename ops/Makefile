SHELL := /bin/bash
PROJECT_NAME := ai-reading
COMPOSE_FILE := docker-compose.yml

.PHONY: help bootstrap up down restart logs ingest adoption-report agent-test patch-apply

help:
@echo "Available targets:"
@echo "  bootstrap        Pull base containers and download models"
@echo "  up               Start the local stack"
@echo "  down             Stop the stack"
@echo "  restart          Restart the stack"
@echo "  logs             Tail docker logs"
@echo "  ingest           Run ingestion pipeline on sample docs"
@echo "  adoption-report  Generate adoption metrics snapshot"
@echo "  agent-test       Run a single agent with sample payload"
@echo "  patch-apply      Apply security updates to running containers"

bootstrap:
@echo "Pulling containers and downloading models..."
docker compose -f $(COMPOSE_FILE) pull
ollama pull mistral:instruct
ollama pull llama3:70b
ollama pull nomic-embed-text || true

up:
docker compose -f $(COMPOSE_FILE) up -d

restart: down up

down:
docker compose -f $(COMPOSE_FILE) down

logs:
docker compose -f $(COMPOSE_FILE) logs -f

ingest:
docker compose -f $(COMPOSE_FILE) run --rm ingest python ingest.py --samples ./data/samples

adoption-report:
docker compose -f $(COMPOSE_FILE) run --rm analytics python adoption_report.py --window 7

agent-test:
@if [ -z "$(AGENT)" ]; then echo "AGENT variable required"; exit 1; fi
docker compose -f $(COMPOSE_FILE) run --rm agents python agent_runner.py --agent $(AGENT) --config ./agents/configs/settings.example.yml

patch-apply:
docker compose -f $(COMPOSE_FILE) exec orchestrator ./scripts/apply_patches.sh
