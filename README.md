# Gllacy Ice Cream Website

This repository contains a Django-based website created for a fictional ice cream company. The project demonstrates a clean backend structure, templating, static assets, and basic web functionality suitable for a small business site.

## Overview

The website presents a catalog of ice cream products, brand information, and UI elements typical for a commercial landing page. Although the company is fictional, the project follows real-world development practices and can serve as a template for similar web projects.

## Features

* Django backend with organized app structure.
* Templates for rendering website pages.
* Static assets (CSS, JavaScript, images) included within the app structure.
* Ready for expansion into a full e‑commerce or catalog system.

## Requirements

* Python 3.10+
* Django (version specified in `requirements.txt`)
* Recommended: virtual environment for dependency isolation

## Installation

Clone the repository and set up the environment:

```bash
git clone <repository-url>
cd gllacy
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

