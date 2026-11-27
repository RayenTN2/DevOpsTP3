# TP3 — FastAPI CI Pipeline (Pytest, Coverage, Pylint & GitHub Actions)

## Description

This project is a Python web application built with **FastAPI** and automated with **GitHub Actions** for Continuous Integration (CI).

In addition to the initial endpoints, it includes the `/soustraction` endpoint (`GET /soustraction?a=...&b=...`), which returns the difference between two numbers:

```json
{
  "resultat": 6.0
}