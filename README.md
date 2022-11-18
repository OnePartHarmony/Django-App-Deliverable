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

<table>
    <th colspan="2" style="text-align:center">Fruits</th>
    <tr>
        <td>id</td>
        <td>primary key</td>
    </tr>
    <tr>
        <td>type</td>
        <td>string</td>
    </tr>
    <tr>
        <td>color</td>
        <td>string</td>
    </tr>
    <tr>
        <td>is_ripe</td>
        <td>boolean</td>
    </tr>
    <tr>
        <td>created_at</td>
        <td>datetime</td>
    </tr>
    <tr>
        <td>updated_at</td>
        <td>datetime</td>
    </tr>
</table>


<table style="display:inline">
  <th colspan="2" style="text-align:center">Pets</th>
  <th colspan="2" style="text-align:center">Owners</th>
  <th colspan="2" style="text-align:center">Toys</th>
  <tr>
    <td>id</td>
    <td>primary key</td>
    <td>id</td>
    <td>primary key</td>
    <td>id</td>
    <td>primary key</td>
  </tr>
  <tr>
    <td>name</td>
    <td>string</td>
    <td>first_name</td>
    <td>string</td>
    <td>description</td>
    <td>string</td>
  </tr>
  <tr>
    <td>type</td>
    <td>string</td>
    <td>last_name</td>
    <td>string</td>
    <td>condition</td>
    <td>string</td>
  </tr>
  <tr>
    <td>age</td>
    <td>integer</td>
    <td>profession</td>
    <td>string</td>
    <td>is_squeaky</td>
    <td>boolean</td>
  </tr>
  <tr>
    <td>is_adoptable</td>
    <td>boolean</td>
    <td>created_at</td>
    <td>datetime</td>
    <td>pet_id</td>
    <td>foreign key</td>
  </tr>
  <tr>
    <td>owner_id</td>
    <td>foreign key</td>
    <td>updated_at</td>
    <td>datetime</td>
    <td>created_at</td>
    <td>datetime</td>
  </tr>
  <tr>
    <td>created_at</td>
    <td>datetime</td>
    <td></td>
    <td></td>
    <td>updated_at</td>
    <td>datetime</td>
  </tr>
  <tr>
    <td>updated_at</td>
    <td>datetime</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>    
  </tr>
</table>


## Instructions

Install required packages: django, psycopg2-binary, djangorestframework