from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

CONFIG_DIR = Path("config") / "targets"
DEFAULT_CONFIG_NAME = "default"
SUPPORTED_REPOSITORY_STATES = ("MVP", "MVP_DONE", "TEST", "PROD")
DEFAULT_REPOSITORY_STATE = "MVP"


@dataclass(frozen=True)
class TargetRepoConfig:
    name: str
    path: Path
    repository_state: str
    source_path: Path | None = None


def _parse_properties(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip()
    return values


def resolve_target_config_path(repo_root: Path, config_name: str | None) -> Path:
    selected = (config_name or DEFAULT_CONFIG_NAME).strip()
    candidate = Path(selected)
    if candidate.suffix == ".properties":
        if candidate.is_absolute():
            return candidate
        return (repo_root / candidate).resolve()
    return (repo_root / CONFIG_DIR / f"{selected}.properties").resolve()


def load_target_repo_config(repo_root: Path, config_name: str | None) -> TargetRepoConfig | None:
    config_path = resolve_target_config_path(repo_root, config_name)
    if not config_path.exists():
        return None

    properties = _parse_properties(config_path)
    raw_repo_path = properties.get("target.repository.path", ".")
    raw_state = properties.get("target.repository.state", DEFAULT_REPOSITORY_STATE)
    state = raw_state.strip().upper()
    if state not in SUPPORTED_REPOSITORY_STATES:
        supported = ", ".join(SUPPORTED_REPOSITORY_STATES)
        raise ValueError(
            f"Unsupported target.repository.state '{raw_state}' in {config_path}. "
            f"Expected one of: {supported}."
        )

    config_name_value = properties.get("target.repository.name", config_path.stem).strip() or config_path.stem
    repo_path = Path(raw_repo_path)
    if not repo_path.is_absolute():
        repo_path = (config_path.parent / repo_path).resolve()

    return TargetRepoConfig(
        name=config_name_value,
        path=repo_path,
        repository_state=state,
        source_path=config_path,
    )


def resolve_target_repo_config(
    repo_root: Path,
    *,
    cli_repo: str | None,
    cli_state: str | None,
    config_name: str | None,
) -> TargetRepoConfig:
    loaded = load_target_repo_config(repo_root, config_name)
    repo_path = (
        Path(cli_repo).resolve()
        if cli_repo
        else (loaded.path if loaded is not None else repo_root)
    )
    state = (
        cli_state.strip().upper()
        if cli_state
        else (loaded.repository_state if loaded is not None else DEFAULT_REPOSITORY_STATE)
    )
    if state not in SUPPORTED_REPOSITORY_STATES:
        supported = ", ".join(SUPPORTED_REPOSITORY_STATES)
        raise ValueError(
            f"Unsupported target repository state '{state}'. Expected one of: {supported}."
        )

    return TargetRepoConfig(
        name=loaded.name if loaded is not None else DEFAULT_CONFIG_NAME,
        path=repo_path,
        repository_state=state,
        source_path=loaded.source_path if loaded is not None else None,
    )
