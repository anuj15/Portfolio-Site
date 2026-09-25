"""Single source of truth for all site content. Edit this file, then run `python build.py`."""

SITE = {
    "name": "Anuj Gupta",
    "title": "Software Engineer",
    "tagline": "Software Engineer specializing in test automation and full-stack development.",
    "email": "your.email@example.com",
    "github": "https://github.com/your-username",
    "linkedin": "https://linkedin.com/in/your-username",
}

ABOUT = {
    "paragraphs": [
        "I'm a software engineer with a passion for building dependable systems and the automated "
        "tests that guard them. My work spans full-stack development, API design, and end-to-end "
        "test automation using tools like Playwright, Python, and TypeScript.",
        "I enjoy turning ambiguous requirements into clean, well-tested code, and I care deeply "
        "about developer experience — readable tests, fast feedback loops, and tooling that makes "
        "the whole team faster.",
    ],
    "facts": [
        {"value": "5+", "label": "Years experience"},
        {"value": "20+", "label": "Projects shipped"},
        {"value": "3", "label": "Languages/stacks"},
    ],
}

SKILLS = [
    {"category": "Languages", "tags": ["Python", "TypeScript", "JavaScript", "SQL"]},
    {"category": "Frontend", "tags": ["React", "Vite", "Tailwind CSS", "HTML/CSS"]},
    {"category": "Backend", "tags": ["FastAPI", "Flask", "SQLAlchemy", "REST APIs"]},
    {"category": "Testing & Automation", "tags": ["Playwright", "Pytest", "pytest-bdd", "Allure"]},
    {"category": "Tools & Platforms", "tags": ["Git", "Docker", "GitHub Actions", "AWS"]},
]

PROJECTS = [
    {
        "name": "ShopCart Demo",
        "description": (
            "A full-stack e-commerce SPA (React + FastAPI + SQLite) built as a realistic sandbox for "
            "practicing Playwright test automation — search, cart, coupons, checkout, and auth flows."
        ),
        "demo_url": "#",
        "source_url": "#",
    },
    {
        "name": "Project Two",
        "description": "Short description of what this project does and the problem it solves.",
        "demo_url": "#",
        "source_url": "#",
    },
    {
        "name": "Project Three",
        "description": "Short description of what this project does and the problem it solves.",
        "demo_url": "#",
        "source_url": "#",
    },
]

EXPERIENCE = [
    {
        "date_range": "2023 — Present",
        "role": "Software Engineer",
        "org": "Company Name",
        "bullets": [
            "Key achievement or responsibility, quantified if possible.",
            "Another accomplishment relevant to the role you're applying for.",
        ],
    },
    {
        "date_range": "2021 — 2023",
        "role": "Previous Role",
        "org": "Previous Company",
        "bullets": [
            "Key achievement or responsibility, quantified if possible.",
            "Another accomplishment relevant to the role you're applying for.",
        ],
    },
]

BLOG_POSTS = [
    {
        "slug": "getting-started-with-playwright-python",
        "title": "Getting Started with Playwright + Python",
        "date": "Jan 2026",
        "excerpt": "A short placeholder post — replace with your own article.",
        "body": [
            "This is placeholder content for your first blog post. Replace this paragraph with an "
            "introduction to your topic — for example, why you chose Playwright over Selenium, or what "
            "problem this post solves for the reader.",
            "Add code samples, screenshots, and lessons learned. Keep posts short, honest, and specific — "
            "recruiters and engineers both respond well to concrete detail over generic advice.",
        ],
    },
    {
        "slug": "designing-realistic-test-fixtures",
        "title": "Designing Realistic Test Fixtures",
        "date": "Feb 2026",
        "excerpt": "A short placeholder post — replace with your own article.",
        "body": [
            "This is placeholder content for your second blog post. Write about how you structure test "
            "data, seed scripts, or fixtures in your automation projects — recruiters love seeing your "
            "real engineering thought process.",
            "Consider linking back to a real project (like a GitHub repo) that demonstrates the pattern "
            "you're describing.",
        ],
    },
]
