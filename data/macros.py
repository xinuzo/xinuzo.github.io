import datetime
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib  # type: ignore[no-redef]

from git.repo import Repo
from markdown_it_pyrs import MarkdownIt

_md = MarkdownIt()

repo = Repo(Path(__file__).parent, search_parent_directories=True)
tree = repo.head.commit.tree

GITHUB_BASE = "https://github.com/xinuzo/xinuzo.github.io"


def handout_link(name: str, filename=None) -> str:
    """Generate PDF + TeX download links for a handout."""
    filename = filename or name
    return (
        f'<a href="/handouts/{name}/{filename}.pdf">(pdf)</a>'
        " "
        f'<a href="/handouts/{name}/{filename}.tex">(tex)</a>'
        "<br>"
    )


def page_footer(src: str) -> str:
    """Generate the footer for a page showing git revision info."""
    input_path = Path("input") / f"{src}.md"
    try:
        blob = tree[str(input_path).replace("\\", "/")]
    except KeyError:
        return (
            '<div class="text-muted">\n'
            f'View the <a href="{GITHUB_BASE}">source repository</a>.\n'
            "</div>\n"
            '<div class="font-italic text-muted">\n'
            "This page is not under public version control.\n"
            "</div>"
        )
    else:
        commit = next(repo.iter_commits(paths=blob.path, max_count=1))
        last_update_dt = datetime.datetime.fromtimestamp(
            commit.committed_date, tz=datetime.timezone.utc
        )
        # Windows-compatible strftime (no %-d)
        last_update_str = last_update_dt.strftime("%a %d %b %Y, %H:%M:%S UTC")
        return (
            "<div>\n"
            f'<a href="{GITHUB_BASE}">Source repository (git)</a> &bullet;\n'
            f'<a href="{GITHUB_BASE}/commits/main/{input_path}">Revision history</a> &bullet;\n'
            f'<a href="{GITHUB_BASE}/edit/main/{input_path}">Suggest edit</a>\n'
            "</div>\n"
            f'<div class="text-muted">Updated {last_update_str} by\n'
            f'<a href="{GITHUB_BASE}/commit/{commit.hexsha}"><code>{commit.hexsha[0:12]}</code></a>\n'
            "</div>"
        )


def hl(link: str, text: str) -> str:
    """Generate a heading with a hash-link anchor."""
    return f'<a id="{link}"></a>{text}<a href="#{link}" class="hash-link">#</a>'


def faq(label: str, question: str) -> str:
    """Generate a FAQ entry with anchor link."""
    return (
        f'<a id="{label}" href="#{label}" style="color:#004824;">{label}.</a> {question}'
        f'<a href="#{label}" class="hash-link">#</a>'
    )
