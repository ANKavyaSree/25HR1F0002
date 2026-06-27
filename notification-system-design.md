# Notification System Design
## Stage 3 – Performance Optimization

### Problem
The notifications API can become slow when the database grows to many students and notifications.

### Optimizations Implemented
- Added database indexes on `type` and `timestamp`.
- Used latest notifications first using `order_by("-timestamp")`.
- Added pagination to avoid returning all records at once.
- Added filtering by notification type.
- Added searching by notification message.
- Used `.only()` to fetch only required fields.

### APIs Tested
GET /evaluation-service/notifications/
GET /evaluation-service/notifications/?type=Event
GET /evaluation-service/notifications/?ordering=-timestamp
GET /evaluation-service/notifications/?search=placement

### Result
The API is faster, cleaner, and ready for larger notification data.