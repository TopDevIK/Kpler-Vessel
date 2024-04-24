# Running the Project

## Prerequisites
1. Docker installed on your system.
2. Python: You need Python and requests library installed to run the generate_data.py script.

## Start the Django Backend

```bash
cd api
docker-compose up
```

## Start the Nuxt.js Application in another terminal

```bash
cd client-vessel
npm install
npm run dev

```

##  Execute the Python Script to Generate Data in another terminal

```
python generate_data.py
```

## API endpoints

1. GET (list) - GET /api/vessels/
2. GET (detail) - GET /api/vessels/{id}/
3. POST - POST /api/vessels/
4. PUT - PUT /api/vessels/{id}/
5. PATCH - PATCH /api/vessels/{id}/
6. DELETE - DELETE /api/vessels/{id}/
