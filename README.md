# python-boilerplate

# Using SQLAlchemy as an ORM


REST architecture
- using CRUD operations CREATE, READ, UPDATE, DELETE
- server
    - router1 (/subscriptions)
        - route2 (POST) CREATE
        - route1 (GET)  READ
        - route3 (PUT)  UPDATE
        - route4 (DELETE)
    - router2 (/users)
        - ...
    - router3 (/plans)
        - ...