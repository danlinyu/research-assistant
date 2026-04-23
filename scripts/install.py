#!/usr/bin/env python3
"""Install this skill into the local Codex skills directory."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path


def parse_skill_name(skill_md: Path) -> str:
    text = skill_md.read_text(encoding="utf-8")
    in_frontmatter = False
    for line in text.splitlines():
        if line.strip() == "---":
            if not in_frontmatter:
                in_frontmatter = True
                continue
            break
        if in_frontmatter and line.startswith("name:"):
            return line.split(":", 1)[1].strip()
    raise ValueError(f"Could not find skill name in {skill_md}")


def default_skills_dir() -> Path:
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        return Path(codex_home).expanduser() / "skills"
    return Path.home() / ".codex" / "skills"


def copy_skill(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)

    def ignore(_dir: str, names: list[str]) -> set[str]:
        ignored = {".git", "__pycache__", ".DS_Store", "Thumbs.db"}
        return {name for name in names if name in ignored}

    shutil.copytree(src, dst, ignore=ignore)


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    skill_md = repo_root / "SKILL.md"
    skill_name = parse_skill_name(skill_md)

    parser = argparse.ArgumentParser(
        description="Install this skill into the Codex skills directory."
    )
    parser.add_argument(
        "--skills-dir",
        type=Path,
        default=default_skills_dir(),
        help="Directory that contains installed Codex skills.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing installed copy.",
    )
    args = parser.parse_args()

    target_skills_dir = args.skills_dir.expanduser().resolve()
    target_dir = target_skills_dir / skill_name

    if repo_root.resolve() == target_dir:
        print(f"Skill already installed at {target_dir}")
        return 0

    target_skills_dir.mkdir(parents=True, exist_ok=True)

    if target_dir.exists() and not args.force:
        print(
            f"Refusing to overwrite existing skill at {target_dir}. "
            "Re-run with --force to replace it.",
            file=sys.stderr,
        )
        return 1

    copy_skill(repo_root, target_dir)
    print(f"Installed {skill_name} to {target_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
