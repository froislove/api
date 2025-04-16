import os
import json
import inspect
import importlib
from pathlib import Path
from pydantic import BaseModel
from settings import settings

MODELS = [
    "models.author_models",
]


def export_schema(model: type[BaseModel], schema_path: Path) -> None:
    """
    Translate BaseModel subclass to json schema
    :param model: model object
    :param schema_path: path to save schema
    :return: None
    """
    schema = model.model_json_schema()
    schema_path.parent.mkdir(parents=True, exist_ok=True)

    with open(schema_path, "w", encoding="utf-8") as f:
        json.dump(schema, f, indent=2)
    print(f"Schema saved: {schema_path}")


def main():
    for module_path in MODELS:
        module = importlib.import_module(module_path)

        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and issubclass(obj, BaseModel) and obj is not BaseModel:
                rel_path = Path(module_path.replace("models.", "")).with_suffix("")
                out_path = settings.schemas_dir / rel_path / f"{name}.json"
                export_schema(obj, out_path)


if __name__ == "__main__":
    main()
