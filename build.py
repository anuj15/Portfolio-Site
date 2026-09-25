"""Static site generator: renders Jinja2 templates + content.py into docs/ for GitHub Pages.

Usage:
    python build.py [--serve]

--serve starts a local HTTP server on the generated output after building.
"""
import argparse
import http.server
import shutil
import socketserver
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

import content

ROOT = Path(__file__).parent
TEMPLATES_DIR = ROOT / "templates"
STATIC_DIR = ROOT / "static"
OUTPUT_DIR = ROOT / "docs"

CONTEXT = {
    "site": content.SITE,
    "about": content.ABOUT,
    "skills": content.SKILLS,
    "projects": content.PROJECTS,
    "experience": content.EXPERIENCE,
    "blog_posts": content.BLOG_POSTS,
}


def build() -> None:
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)

    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), autoescape=True)

    # Home page and blog index live at the site root.
    _render(env, "index.html", OUTPUT_DIR / "index.html", base_path="")
    _render(env, "blog_index.html", OUTPUT_DIR / "blog.html", base_path="")

    # Individual posts live one level deeper, under blog/.
    blog_dir = OUTPUT_DIR / "blog"
    blog_dir.mkdir()
    for post in content.BLOG_POSTS:
        _render(
            env,
            "post.html",
            blog_dir / f"{post['slug']}.html",
            base_path="../",
            post=post,
        )

    _copy_static()

    # Disables Jekyll processing so GitHub Pages serves docs/ as-is.
    (OUTPUT_DIR / ".nojekyll").touch()

    print(f"Built site into {OUTPUT_DIR.relative_to(ROOT)}/")


def _render(env: Environment, template_name: str, output_path: Path, **extra_context) -> None:
    template = env.get_template(template_name)
    html = template.render(**CONTEXT, **extra_context)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")


def _copy_static() -> None:
    for item in STATIC_DIR.iterdir():
        destination = OUTPUT_DIR / item.name
        if item.is_dir():
            shutil.copytree(item, destination, dirs_exist_ok=True)
        else:
            shutil.copy2(item, destination)


def serve() -> None:
    import functools

    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(OUTPUT_DIR))
    with socketserver.TCPServer(("", 8080), handler) as httpd:
        print("Serving docs/ at http://localhost:8080 (Ctrl+C to stop)")
        httpd.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--serve", action="store_true", help="Serve the built site locally after building")
    args = parser.parse_args()

    build()
    if args.serve:
        serve()
