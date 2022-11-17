# Django-App-Deliverable

## Description

This is an app for practicing CRUD in Django.  It contains two unrelated models, fruits and pets, which each have full-crud capabilities.

## Routes Table

| Action  | HTTP Verb | Paths                   |
|---------|-----------|-------------------------|
| Index   | GET       | /fruit<br>/pets         |
| Show    | GET       | /fruit/:pk<br>/pets/:pk |
| Create  | POST      | /fruit<br>/pets         |
| Update  | PATCH     | /fruit/:pk<br>/pets/:pk |
| Destroy | DELETE    | /fruit/:pk<br>/pets/:pk |

## Instructions

Install required packages: django, psycopg2-binary, djangorestframework