# Rendi's Blog

Source files for [Rendi's Blog](https://xinuzo.github.io/blog/),
a personal blog about math, code, and everything in between.

Built with [Pelican](https://getpelican.com/), inspired by
[blog.evanchen.cc](https://github.com/vEnhance/blog.evanchen.cc).

## Development

### Installation

After installing [uv](https://docs.astral.sh/uv), do:

- `uv sync` to install dependencies
- `uv run prek install` to install pre-commit hooks

### Compilation

- `uv run pelican content` to build development site to `output/`
- `uv run pelican content -s publishconf.py` to build the published version
  to `output/` (absolute URL's)
- `uv run pelican --listen` to launch a development server

For faster development (avoids building all posts):

- `./scripts/recent.sh [N]` — dev server with only posts from the last N days
  (default: 365)
- `./scripts/watch-one.sh <slug>` — dev server rendering a single post

### Writing a new post

1. Run `uv run scripts/new.py` to create a new post with a frontmatter template.
2. Write your post in Markdown with YAML frontmatter.
3. When ready to publish, change `status: draft` to `status: published`
   and set the correct date.
4. Build and preview with `uv run pelican --listen`.

### Listing drafts

```bash
./scripts/drafts.sh
```

## Directory structure

```
blog/
├── content/          # Blog posts (Markdown)
│   ├── Math/         # Category: Math
│   ├── Essays/       # Category: Essays (etc.)
│   └── pages/        # Static pages (About, etc.)
├── theme/            # Custom Pelican theme
│   ├── templates/    # Jinja2 HTML templates
│   └── static/       # CSS, images, SVG assets
├── plugins/          # Custom Pelican plugins
│   ├── sidenotes.py  # Footnotes → Tufte sidenotes
│   ├── oembed_gen.py # oEmbed JSON generation
│   └── ...
├── markdown_ext_custom/  # Custom Markdown extensions
├── scripts/          # Utility scripts
├── pelicanconf.py    # Development config
├── publishconf.py    # Production config
├── recentconf.py     # Recent-posts-only config
└── pyproject.toml    # Python project definition
```

## Features

- **Dark mode** theme matching the main site (`#0f0f0f` + `#f28585`)
- **KaTeX** for fast math rendering
- **Tufte-style sidenotes** (footnotes become margin notes on wide screens)
- **Categories & tags** with dedicated listing pages
- **Pagination** (10 posts per page)
- **Sidebar** with recent posts (on wide screens)
- **oEmbed** support for rich link previews
- **Isso** comment system
- **Atom feed** for subscribers

## License

MIT License.
