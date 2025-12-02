# myapp

Simple Django project used for learning and demo purposes. This repository contains a small blog app with templates, static files, and basic views. Note: the project is not fully finished — see the "Status" section below.

**Quick Start**
- **Create & activate venv (PowerShell)**:
  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```
- **Install dependencies** (if you have a `requirements.txt`):
  ```powershell
  pip install -r requirements.txt
  ```
  If you don't have `requirements.txt`, at minimum install Django:
  ```powershell
  pip install django
  ```
- **Prepare database & run**:
  ```powershell
  python manage.py migrate
  python manage.py createsuperuser  # optional
  python manage.py runserver
  ```

**Project Structure (short)**
- `manage.py` — Django management entry
- `blog/` — app code: `models.py`, `views.py`, `templates/`, `static/`
- `myapp/` — project settings and URLs
- `templates/` — site-level templates like `404.html`

**Status**
- This project is a work-in-progress. Some features, tests and production configuration are not implemented.

**Known TODOs**
- Add comprehensive unit tests for `blog` views and models
- Add `requirements.txt` and lock dependencies
- Separate `settings.py` into `development`/`production` and secure secrets
- Configure media file handling and deployment settings
- Add CI (GitHub Actions) and linting/formatting checks

**Useful Commands**
- Run tests: `python manage.py test`
- Create static build (for production): `python manage.py collectstatic --noinput`

If you want, I can: commit this `README.md`, add a `requirements.txt`, or shorten/expand any section. Which would you like next?
