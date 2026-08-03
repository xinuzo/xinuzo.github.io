# xinuzo.github.io

These are source files for my personal website
[xinuzo.github.io](https://xinuzo.github.io).

The build system is inspired by
[Evan Chen's web.evanchen.cc](https://github.com/vEnhance/web.evanchen.cc).
We use a custom build script with
[Jinja2](https://jinja.palletsprojects.com/) and
[markdown-it-pyrs](https://pypi.org/project/markdown-it-pyrs/) (with extensions).
The [build script](scripts/build.py) is intentionally short, less than 100 lines of code.

## Main content structure

- Content is written in `input/`, and built to `output/`.
  A page `filename.md` is written directly to `output/filename.html`.
  To keep things simple, directory structures are explicitly not supported.
- There is only one Jinja template: `data/page.html.j2`.
- Navigation links on the right are controlled by `data/nav.toml`.
- Python macros are written in `data/macros.py`, available to Jinja.

## Development

After installing [uv](https://docs.astral.sh/uv/), run:

- `uv run scripts/build.py` to build
- `uv run scripts/audit.py` to check for broken links
- `uv run scripts/devserver.py` to run a development server at `http://localhost:8000`

### First-time setup

```bash
# Install uv (if not already installed)
# See https://docs.astral.sh/uv/getting-started/installation/

# Clone the repository
git clone https://github.com/xinuzo/xinuzo.github.io.git
cd xinuzo.github.io

# Install dependencies (uv handles the virtual environment automatically)
uv sync

# Build the site
uv run scripts/build.py

# Start the dev server
uv run scripts/devserver.py
# Open http://localhost:8000 in your browser
```

## How to add and modify content

### Adding a new page

1. Create a new Markdown file in `input/`, e.g. `input/my-page.md`.
2. Add YAML frontmatter at the top:
   ```markdown
   ---
   title: My Page Title
   description: A short description for SEO.
   ---

   Your content goes here in Markdown.

   You can use LaTeX: $E = mc^2$

   ## {{ hl("section-id", "Section Heading") }}

   The `hl()` macro creates a heading with an anchor link.
   ```
3. Run `uv run scripts/build.py` to generate `output/my-page.html`.
4. (Optional) Add it to the navigation sidebar by editing `data/nav.toml`:
   ```toml
   [[block]]
   shortname = "My Page"
   src = "my-page"
   subpages = [
     {shortname = "Subsection", url = "#section-id"},
   ]
   ```

### Editing an existing page

1. Open the corresponding `input/*.md` file.
2. Edit the Markdown content.
3. Rebuild with `uv run scripts/build.py`.
4. Preview with `uv run scripts/devserver.py`.

### Modifying the navigation sidebar

Edit `data/nav.toml`. The format is:

```toml
[[block]]
shortname = "Section Name"    # Display text
src = "page-stem"             # Links to /page-stem.html
subpages = [
  {shortname = "Sub Item", src = "sub-page"},       # Internal link
  {shortname = "External", url = "https://..."},     # External link
  {shortname = "Anchor", url = "#anchor-id"},        # Hash link
]
```

### Changing the template / layout

Edit `data/page.html.j2`. This is a standard Jinja2 template. Variables available:

| Variable | Description |
|----------|-------------|
| `page["title"]` | Page title from frontmatter |
| `page["description"]` | Page description from frontmatter |
| `content` | Rendered HTML content |
| `src` | Page stem (e.g. `"index"`, `"math-notes"`) |
| `nav_links` | Navigation data from `nav.toml` |

### Changing styles

Edit `static/css/style.css` for the main theme.
Edit `static/css/extras.css` for additional component styles.

Key CSS variables / colors to change for theming:

| Element | Current Value | What it controls |
|---------|--------------|-----------------|
| `body background-color` | `#0f0f0f` | Page background |
| `#main background-color` | `#141010` | Main content box |
| `#side background-color` | `#151118` | Sidebar box |
| `#header background-color` | `#1a1010` | Header bar |
| `a:link color` | `#f28585` | Link color (light red) |
| `h1 color` | `#f28585` | H1 heading color |
| `h2 color` | `#ff9e9e` | H2 heading color |
| `h3 color` | `#e6a0c0` | H3 heading color |
| `strong color` | `#f28585` | Bold text color |

### Adding macros

Edit `data/macros.py`. Any function defined there is available in Jinja templates
and in Markdown content. For example:

```python
def my_macro(arg: str) -> str:
    return f'<div class="custom">{arg}</div>'
```

Use it in Markdown:
```markdown
{{ my_macro("Hello world") }}
```

### Adding static files

Place files in the `static/` directory:

| Directory | Purpose |
|-----------|---------|
| `static/css/` | Stylesheets |
| `static/js/` | JavaScript |
| `static/icons/` | Favicons and social icons |
| `static/images/` | Images used in content |
| `static/docs/` | PDFs, CV, downloadable documents |

These are served at `/static/...` by the dev server and copied to the output on deploy.

## Directory structure

```
xinuzo.github.io/
├── input/            # Markdown content (source of truth)
│   ├── index.md
│   ├── math-notes.md
│   ├── software.md
│   ├── teaching.md
│   ├── contact.md
│   └── 404.md
├── data/             # Build system config
│   ├── page.html.j2  # Jinja2 page template
│   ├── nav.toml      # Navigation sidebar config
│   ├── macros.py      # Python macros for Jinja
│   └── EXTDIRS        # External directory prefixes
├── scripts/          # Build scripts
│   ├── build.py       # Main build script (~80 lines)
│   ├── audit.py       # Link checker
│   └── devserver.py   # Local development server
├── static/           # Static assets (served as-is)
│   ├── css/
│   ├── js/
│   ├── icons/
│   ├── images/
│   └── docs/
├── output/           # Generated HTML (gitignored)
├── pyproject.toml    # Python project config
├── prek.toml         # Pre-commit hooks
├── rumdl.toml        # Markdown linting
└── .github/workflows/build.yml  # CI/CD
```

## License

MIT License. See [LICENSE](LICENSE).
