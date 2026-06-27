## Notification App Backend
# Notification App Backend

Django REST API for AffordMed Campus Notification System.

## Features

- Health check API
- Notification CRUD API
- Filter by notification type
- Search notification message
- Sort by timestamp
- Pagination
- Optimized queryset
- Notification dispatch simulation
- Email, SMS, and Push simulation

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- django-filter

## Run Project

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

APIs
Health Check
GET /evaluation-service/health/
Notification List
GET /evaluation-service/notifications/
Filter
GET /evaluation-service/notifications/?type=Event
Search
GET /evaluation-service/notifications/?search=placement
Sort
GET /evaluation-service/notifications/?ordering=-timestamp
Send Notification
POST /evaluation-service/send/
{
  "type": "Event",
  "message": "Exam starts tomorrow",
  "timestamp": "2026-06-27T18:30:00Z"
}

---

### 2. Update `notification-system-design.md`

Add this:

```markdown
## Stage 6 – Final System Design

### Architecture

Client → Django REST API → Service Layer → Dispatcher → Database

### Layers

1. Views
- Handles HTTP requests and responses.

2. Serializers
- Converts model data to JSON.

3. Models
- Stores notification data.

4. Services
- Contains business logic.

5. Dispatcher
- Simulates email, SMS, and push notification delivery.

### Performance

- Indexed `type` field.
- Indexed `timestamp` field.
- Pagination enabled.
- Queryset optimized using `.only()`.
- Latest notifications returned first.

### Scalability

For production:
- Use PostgreSQL instead of SQLite.
- Use Celery workers for background notification dispatch.
- Use Redis/RabbitMQ as message broker.
- Use batch processing for 50,000+ students.
- Add retry mechanism for failed notifications.
- Add authentication and role-based access.

### Final APIs

GET /evaluation-service/health/

GET /evaluation-service/notifications/

POST /evaluation-service/notifications/

GET /evaluation-service/notifications/{id}/

PUT /evaluation-service/notifications/{id}/

DELETE /evaluation-service/notifications/{id}/

POST /evaluation-service/send/
3. Final test
python manage.py runserver

Open:

http://127.0.0.1:8000/evaluation-service/health/
http://127.0.0.1:8000/evaluation-service/notifications/