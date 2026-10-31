# Resume website

A small, data-driven resume site with a Python (Flask) API and a React frontend.
The resume content lives in `backend/profile.py`; the React components render
that JSON instead of duplicating the content in the browser.

## Run it locally

You need Python 3 and Node.js/npm installed.

1. In a terminal, create a Python environment and install the API dependencies:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r backend/requirements.txt
   ```

2. Start the API from the project root:

   ```bash
   python -m backend.app
   ```

   The API runs at `http://localhost:5000`. You can check it at
   `http://localhost:5000/api/health`.

3. In a second terminal, install and start the React app:

   ```bash
   cd frontend
   npm install
   npm run dev
   ```

   Open the local URL printed by Vite (usually `http://localhost:5173`).

## Where to make changes

- **Resume data:** edit `backend/profile.py`.
- **API routes and local server settings:** edit `backend/app.py`.
- **Page sections:** edit or add components in `frontend/src/components/`.
- **Theme colors:** edit `frontend/src/styles/themes.css`.
- **Page geometry:** edit `frontend/src/styles/layouts.css`.
- **Component appearance:** edit `frontend/src/styles/components.css`.
- **API URL:** copy `frontend/.env.example` to `frontend/.env` and set
  `VITE_API_URL` if the API runs somewhere other than the local default.

The appearance controls show how the CSS is split up: themes change color
variables, while layouts change the grid. Add another option by adding a
matching selector in `App.jsx` and CSS rules in the appropriate stylesheet.

## Test and build

Run the API tests from the project root after installing its requirements:

```bash
python -m unittest discover -s backend/tests
```

Create an optimized frontend build with:

```bash
cd frontend
npm run build
```

## Hosting notes

Deploy the Python API and React frontend as separate services, or serve the
frontend build from a static host. Set `VITE_API_URL` to the public API URL when
building the frontend, and set `FRONTEND_ORIGINS` on the API to the frontend
origin (comma-separated if there is more than one). Hosts that provide a
`PORT` environment variable are supported by the API entry point.

Flask's built-in server is for local learning and development; use a
production WSGI server when deploying the API.
