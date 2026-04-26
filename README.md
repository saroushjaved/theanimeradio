# The Anime Radio

The Anime Radio is a Django website for anime discovery. It combines a short recommendation quiz, ranked anime lists, user voting, account registration, and community polls into one small fan-site project.

The project was originally built as a deployed Django site. This repo has been cleaned up so it can be shared publicly, cloned safely, and run locally without production secrets.

## Features

- Anime recommendation quiz with branching questions by experience, era, genre, and sub-genre.
- Ranked anime lists for 2018, 2019, and 2020 seasonal pages.
- Authenticated upvote/downvote flow for anime list entries.
- Community polls with one vote per logged-in user per poll.
- Django admin support for managing anime entries, recommendations, polls, and choices.
- SEO-friendly page metadata, canonical URLs, Open Graph tags, `robots.txt`, and `sitemap.xml`.
- Local SQLite defaults for easy setup, with environment variables for production databases.

## Tech Stack

- Python
- Django
- SQLite for local development
- PostgreSQL-ready production settings
- Bootstrap-based templates

## Project Structure

```text
theanimeradio/
  pages/                    Home page, anime list pages, voting logic, sitemap, robots
  polling/                  Poll models and voting views
  reccomendationengine/     Recommendation quiz models and views
  usersreg/                 Signup, login, logout, and profile landing views
  static/                   CSS, JavaScript, fonts, and site images
  templates/                Shared and feature-specific Django templates
  theanimeradio/            Django project settings, URLs, WSGI/ASGI entrypoints
  manage.py
  requirements.txt
  .env.example
```

Note: the app name `reccomendationengine` is misspelled in the original project and remains that way to avoid breaking migrations/import paths.

## Local Setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Create your local environment file:

```powershell
Copy-Item .env.example .env
```

For local development, the defaults are enough. The app uses SQLite unless you set `DB_ENGINE` to PostgreSQL.

Run migrations:

```powershell
python manage.py migrate
```

Create an admin user:

```powershell
python manage.py createsuperuser
```

Start the development server:

```powershell
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Environment Variables

| Variable | Purpose | Default |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | Secret key for signing sessions and tokens | unsafe local dev key |
| `DJANGO_DEBUG` | Enables Django debug mode | `True` |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated allowed hosts | `127.0.0.1,localhost,theanimeradio.com,www.theanimeradio.com` |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | Comma-separated trusted origins | production site URLs |
| `SITE_NAME` | Name used in SEO metadata | `The Anime Radio` |
| `SITE_URL` | Canonical production URL | `https://www.theanimeradio.com` |
| `SITE_DESCRIPTION` | Default meta description | anime discovery description |
| `DB_ENGINE` | Django database backend | `django.db.backends.sqlite3` |
| `DB_NAME` | Database name/path | `db.sqlite3` |
| `DB_USER` | Database user for non-SQLite backends | empty |
| `DB_PASSWORD` | Database password for non-SQLite backends | empty |
| `DB_HOST` | Database host for non-SQLite backends | `localhost` |
| `DB_PORT` | Database port for non-SQLite backends | empty |

## Content Management

Most public content is managed through Django admin:

- `List2018`, `List2019`, `List2020`: anime list entries.
- `RecommendationDatabase`: recommendation quiz results.
- `Polls` and `Choices`: poll questions and voting options.

Uploaded images are stored under `media/` at runtime. The folder is ignored by Git because uploads are environment-specific and should not be committed as source code.

## SEO Notes

The shared base templates include:

- Unique page titles/descriptions where views provide them.
- Canonical URLs based on `SITE_URL`.
- Open Graph tags for link previews.
- Twitter card metadata.
- Search-friendly `robots.txt`.
- XML sitemap at `/sitemap.xml`.

For production, set `SITE_URL` to the final public domain before deploying.

## Production Checklist

- Set `DJANGO_DEBUG=False`.
- Set a strong `DJANGO_SECRET_KEY`.
- Configure `DJANGO_ALLOWED_HOSTS` for your domain.
- Configure `DJANGO_CSRF_TRUSTED_ORIGINS` with `https://` origins.
- Use PostgreSQL or another production database through the `DB_*` variables.
- Run `python manage.py collectstatic`.
- Serve `static/` and `media/` through your hosting platform or web server.
- Keep `media/`, `.env`, and generated `assets/` out of Git.

## Development Notes

This cleanup intentionally removed generated files from source control:

- Python bytecode and `__pycache__`.
- Collected static output in `assets/`.
- Uploaded media files in `media/`.
- Old coming-soon static template bundle.
- Editor and operating-system metadata.

The repository now focuses on the Django application source, reusable static assets, templates, migrations, and documentation.
