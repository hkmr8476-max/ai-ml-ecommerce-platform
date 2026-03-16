import json
from pathlib import Path


ARTIFACT = Path('ml-engine/model_artifact.json')


def train_pipeline() -> None:
    artifact = {'status': 'trained', 'version': '0.1.0'}
    ARTIFACT.write_text(json.dumps(artifact, indent=2))


if __name__ == '__main__':
    train_pipeline()
