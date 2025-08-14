import os

# Define your folder and file structure
structure = {
    "safehaven": {
        "backend": {
            "app": {
                "__init__.py": "",
                "main.py": "",
                "config.py": "",
                "auth": {
                    "__init__.py": "",
                    "routes.py": "# FastAPI endpoints for auth (signup/login)\n",
                    "service.py": "# Supabase auth logic (sign_up, sign_in)\n"
                },
                "models": {
                    "__init__.py": "",
                    "user.py": "",
                    "report.py": "",
                    "shelter.py": ""
                },
                "schemas": {
                    "__init__.py": "",
                    "auth.py": "# Pydantic models for Auth requests/responses\n"
                },
                "services": {
                    "nlp.py": "",
                    "vision.py": "",
                    "geospatial.py": ""
                },
                "routes": {
                    "__init__.py": "",
                    "reports.py": "",
                    "shelters.py": "",
                    "analytics.py": ""
                },
                "utils": {},
                "database.py": ""
            },
            "requirements.txt": "",
            "Dockerfile": ""
        },
        "frontend-dashboard": {
            "src": {
                "components": {},
                "pages": {},
                "services": {},
                "App.jsx": ""
            },
            "package.json": "",
            "tailwind.config.js": ""
        },
        "mobile-app": {
            "src": {
                "screens": {},
                "components": {},
                "services": {},
                "App.js": ""
            },
            "package.json": "",
            "app.json": ""
        },
        "ai-models": {
            "nlp": {
                "distress_model.pt": "",
                "tokenizer": {}
            },
            "vision": {
                "yolov8_model.pt": ""
            },
            "README.md": ""
        },
        "docs": {
            "architecture.md": "",
            "api_reference.md": "",
            "deployment_guide.md": "",
            "CONTRIBUTING.md": ""
        },
        "scripts": {
            "init_db.py": "",
            "run_dev.sh": "",
            "deploy_render.sh": ""
        },
        ".env.example": "# SUPABASE_URL=your_url\n# SUPABASE_KEY=your_key\n",
        "docker-compose.yml": "",
        "README.md": "",
        "LICENSE": "",
        "CONTRIBUTING.md": ""
    }
}

def create_structure(base_path, struct):
    for name, content in struct.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

if __name__ == "__main__":
    base_dir = os.getcwd()  # current directory
    create_structure(base_dir, structure)
    print("✅ Safehaven folder structure created successfully!")
