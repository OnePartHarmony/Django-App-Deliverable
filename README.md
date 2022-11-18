# Django-App-Deliverable

## Description

This is an app for practicing CRUD in Django.  It contains two unrelated models, fruits and pets, which each have full-crud capabilities.  It also now contains owners and toys, which have one-to many relationships with pets.

## Routes Table

| Action  | HTTP Verb | Paths                                               |
|---------|-----------|-----------------------------------------------------|
| Index   | GET       | /fruit<br>/pets<br>/toys<br>/owners                 |
| Show    | GET       | /fruit/:pk<br>/pets/:pk<br>/toys/:pk<br>/owners/:pk |
| Create  | POST      | /fruit<br>/pets<br>/toys<br>/owners                 |
| Update  | PATCH     | /fruit/:pk<br>/pets/:pk<br>/toys/:pk<br>/owners/:pk |
| Destroy | DELETE    | /fruit/:pk<br>/pets/:pk<br>/toys/:pk<br>/owners/:pk |


## Models

| <td colspan=2>Fruits     |
|--------------------------|
| id         | primary key |
| type       | string      |
| color      | string      |
| is_ripe    | boolean     |
| created_at | datetime    |
| updated_at | datetime    |




## Instructions

Install required packages: django, psycopg2-binary, djangorestframework