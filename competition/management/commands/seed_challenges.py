from django.core.management.base import BaseCommand

from competition.models import Challenge


class Command(BaseCommand):
    help = "Seed starter challenges for local development."

    def handle(self, *args, **options):
        Challenge.objects.all().delete()
        self.stdout.write(self.style.WARNING("Cleared existing challenges."))

        challenges = [
            {
                "title": "ISCC Launch Hero",
                "description": "Design a polished hero section with a badge, headline, supporting copy, two CTA buttons, and a stats card.",
                "difficulty": "easy",
                "time_limit": 18,
                "category": "landing",
                "target_html": """<section class="hero">
  <div class="hero-text">
    <span class="pill">ISCC 2026</span>
    <h1>Build the future of student interfaces.</h1>
    <p>
      Compete in a live UI challenge, submit your best build, and climb the
      leaderboard in real time.
    </p>
    <div class="cta">
      <button class="primary">Start a challenge</button>
      <button class="secondary">View leaderboard</button>
    </div>
  </div>
  <div class="hero-card">
    <div class="card-header">
      <span>Live Metrics</span>
      <strong>Week 04</strong>
    </div>
    <div class="metrics">
      <div>
        <h3>128</h3>
        <p>Active competitors</p>
      </div>
      <div>
        <h3>46</h3>
        <p>Challenges open</p>
      </div>
    </div>
    <div class="progress">
      <div class="bar"><span></span></div>
      <div class="caption">Submission rate +23%</div>
    </div>
  </div>
</section>""",
                "target_css": """* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: 'Inter', sans-serif;
  background: #0f0b1d;
  color: #f8fafc;
}
.hero {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 32px;
  padding: 64px;
}
.pill {
  display: inline-flex;
  padding: 6px 14px;
  border-radius: 999px;
  background: rgba(139, 92, 246, 0.2);
  color: #c4b5fd;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.2em;
}
.hero-text h1 {
  font-size: 44px;
  line-height: 1.1;
  margin: 16px 0 12px;
}
.hero-text p {
  color: #cbd5f5;
  font-size: 16px;
  max-width: 500px;
}
.cta {
  display: flex;
  gap: 12px;
  margin-top: 22px;
}
.primary, .secondary {
  padding: 12px 18px;
  border-radius: 12px;
  border: none;
  font-weight: 600;
}
.primary { background: #8b5cf6; color: white; }
.secondary {
  background: transparent;
  border: 1px solid rgba(148, 163, 184, 0.35);
  color: #e2e8f0;
}
.hero-card {
  background: #17102b;
  border-radius: 20px;
  padding: 24px;
  box-shadow: 0 16px 40px rgba(15, 23, 42, 0.4);
}
.card-header {
  display: flex;
  justify-content: space-between;
  color: #a5b4fc;
  font-size: 13px;
  margin-bottom: 18px;
}
.metrics {
  display: flex;
  gap: 24px;
}
.metrics h3 {
  margin: 0;
  font-size: 28px;
}
.metrics p {
  margin: 4px 0 0;
  font-size: 12px;
  color: #94a3b8;
}
.progress {
  margin-top: 22px;
}
.bar {
  height: 8px;
  border-radius: 999px;
  background: rgba(148, 163, 184, 0.2);
  overflow: hidden;
}
.bar span {
  display: block;
  height: 100%;
  width: 68%;
  background: linear-gradient(90deg, #7c3aed, #22d3ee);
}
.caption {
  margin-top: 10px;
  color: #94a3b8;
  font-size: 12px;
}
""",
                "target_js": "",
            },
            {
                "title": "Competitor Profile Card",
                "description": "Create a professional profile card with avatar, badges, and performance stats.",
                "difficulty": "easy",
                "time_limit": 14,
                "category": "card",
                "target_html": """<div class="profile-card">
  <div class="avatar">CO</div>
  <div class="info">
    <h3>Competitor One</h3>
    <p>Frontier Tech Institute · @competitor</p>
  </div>
  <div class="badges">
    <span class="pill">Top 10</span>
    <span class="pill ghost">UI</span>
  </div>
  <div class="stats">
    <div>
      <strong>12</strong>
      <span>Submissions</span>
    </div>
    <div>
      <strong>94%</strong>
      <span>Best score</span>
    </div>
    <div>
      <strong>3</strong>
      <span>Streak</span>
    </div>
  </div>
</div>""",
                "target_css": """body {
  font-family: 'Inter', sans-serif;
  background: #0f0b1d;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  color: #f8fafc;
}
.profile-card {
  width: 360px;
  background: #1b1333;
  border-radius: 20px;
  padding: 24px;
  box-shadow: 0 18px 40px rgba(15, 23, 42, 0.35);
}
.avatar {
  height: 54px;
  width: 54px;
  border-radius: 16px;
  background: #8b5cf6;
  display: grid;
  place-items: center;
  font-weight: 700;
  margin-bottom: 12px;
}
.info h3 {
  margin: 0;
  font-size: 20px;
}
.info p {
  margin: 6px 0 14px;
  color: #94a3b8;
  font-size: 13px;
}
.badges {
  display: flex;
  gap: 8px;
  margin-bottom: 16px;
}
.pill {
  padding: 6px 12px;
  border-radius: 999px;
  background: rgba(99, 102, 241, 0.2);
  color: #c7d2fe;
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.2em;
}
.pill.ghost {
  background: transparent;
  border: 1px solid rgba(148, 163, 184, 0.3);
  color: #e2e8f0;
}
.stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
}
.stats strong {
  display: block;
  font-size: 18px;
}
.stats span {
  color: #94a3b8;
  font-size: 11px;
}
""",
                "target_js": "",
            },
            {
                "title": "Challenge Brief Panel",
                "description": "Design a brief panel with difficulty pill, time limit, and start button.",
                "difficulty": "medium",
                "time_limit": 20,
                "category": "layout",
                "target_html": """<div class="brief">
  <div class="header">
    <span class="pill">Medium</span>
    <span class="time">30 min</span>
  </div>
  <h2>Profile Settings UI</h2>
  <p>Build a settings panel with profile fields, toggles, and a save action.</p>
  <div class="meta">
    <div>
      <strong>Elements</strong>
      <span>Inputs · Toggles · Button</span>
    </div>
    <div>
      <strong>Score</strong>
      <span>90%+ target</span>
    </div>
  </div>
  <button>Start challenge</button>
</div>""",
                "target_css": """body {
  font-family: 'Inter', sans-serif;
  background: #0f0b1d;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  color: #f8fafc;
}
.brief {
  width: 420px;
  background: #1b1333;
  border-radius: 20px;
  padding: 26px;
  box-shadow: 0 18px 40px rgba(15, 23, 42, 0.35);
}
.header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 16px;
}
.pill {
  padding: 6px 12px;
  border-radius: 999px;
  background: rgba(34, 197, 94, 0.2);
  color: #86efac;
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.2em;
}
.time { color: #a5b4fc; font-size: 12px; }
h2 { margin: 0 0 8px; font-size: 22px; }
p { color: #cbd5f5; margin: 0 0 18px; }
.meta {
  display: grid;
  gap: 12px;
  margin-bottom: 20px;
}
.meta strong {
  display: block;
  font-size: 12px;
  color: #e2e8f0;
}
.meta span {
  font-size: 12px;
  color: #94a3b8;
}
button {
  width: 100%;
  padding: 12px;
  border: none;
  border-radius: 12px;
  background: #8b5cf6;
  color: white;
  font-weight: 600;
}
""",
                "target_js": "",
            },
            {
                "title": "Leaderboard Highlight Row",
                "description": "Create a leaderboard row with rank, user info, and score badge.",
                "difficulty": "easy",
                "time_limit": 12,
                "category": "list",
                "target_html": """<div class="leaderboard-row">
  <div class="rank">#1</div>
  <div class="user">
    <div class="avatar">JD</div>
    <div>
      <strong>Jolie Joie</strong>
      <span>Greenfields College · @jolie</span>
    </div>
  </div>
  <div class="score">98%</div>
  <button>View</button>
</div>""",
                "target_css": """body {
  font-family: 'Inter', sans-serif;
  background: #0f0b1d;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  color: #f8fafc;
}
.leaderboard-row {
  width: 520px;
  background: #1b1333;
  border-radius: 18px;
  padding: 16px 20px;
  display: grid;
  grid-template-columns: 60px 1fr 90px 90px;
  align-items: center;
  gap: 16px;
  box-shadow: 0 16px 35px rgba(15, 23, 42, 0.35);
}
.rank {
  font-weight: 700;
  font-size: 20px;
  color: #facc15;
}
.user {
  display: flex;
  align-items: center;
  gap: 12px;
}
.avatar {
  height: 42px;
  width: 42px;
  border-radius: 12px;
  background: #8b5cf6;
  display: grid;
  place-items: center;
  font-weight: 700;
}
.user strong {
  display: block;
}
.user span {
  font-size: 12px;
  color: #94a3b8;
}
.score {
  text-align: right;
  font-weight: 700;
  color: #22d3ee;
}
button {
  padding: 8px 14px;
  border-radius: 10px;
  border: 1px solid rgba(148, 163, 184, 0.35);
  background: transparent;
  color: #e2e8f0;
}
""",
                "target_js": "",
            },
            {
                "title": "Scoreboard Stats Grid",
                "description": "Create a compact grid of KPI cards with icon placeholders and helper text.",
                "difficulty": "medium",
                "time_limit": 22,
                "category": "dashboard",
                "target_html": """<div class="grid">
  <div class="card">
    <div class="icon"></div>
    <h3>Submissions</h3>
    <strong>248</strong>
    <span>+18 today</span>
  </div>
  <div class="card">
    <div class="icon"></div>
    <h3>Avg Score</h3>
    <strong>87%</strong>
    <span>+2.4% week</span>
  </div>
  <div class="card">
    <div class="icon"></div>
    <h3>Review Time</h3>
    <strong>14m</strong>
    <span>-3m this week</span>
  </div>
</div>""",
                "target_css": """body {
  font-family: 'Inter', sans-serif;
  background: #0f0b1d;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  color: #f8fafc;
}
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}
.card {
  background: #1b1333;
  border-radius: 18px;
  padding: 18px;
  min-width: 180px;
  box-shadow: 0 14px 30px rgba(15, 23, 42, 0.35);
}
.icon {
  height: 36px;
  width: 36px;
  border-radius: 12px;
  background: rgba(56, 189, 248, 0.2);
  margin-bottom: 12px;
}
h3 {
  margin: 0;
  font-size: 14px;
  color: #cbd5f5;
}
strong {
  display: block;
  font-size: 24px;
  margin: 8px 0 4px;
}
span {
  font-size: 12px;
  color: #94a3b8;
}
""",
                "target_js": "",
            },
        ]

        extra_specs = [
            {
                "title": "Notification Banner",
                "description": "Design a banner with icon, message, and action button.",
                "difficulty": "easy",
                "time_limit": 10,
                "category": "alert",
                "accent": "#22d3ee",
            },
            {
                "title": "Team Card",
                "description": "Build a team card with avatars, role labels, and action buttons.",
                "difficulty": "easy",
                "time_limit": 12,
                "category": "card",
                "accent": "#a855f7",
            },
            {
                "title": "Pricing Toggle",
                "description": "Create a pricing header with a monthly/yearly toggle.",
                "difficulty": "medium",
                "time_limit": 18,
                "category": "pricing",
                "accent": "#38bdf8",
            },
            {
                "title": "Challenge Filters",
                "description": "Build a filter bar with pills, search, and sort control.",
                "difficulty": "medium",
                "time_limit": 18,
                "category": "navigation",
                "accent": "#60a5fa",
            },
            {
                "title": "Progress Timeline",
                "description": "Create a timeline with three steps and status indicators.",
                "difficulty": "medium",
                "time_limit": 20,
                "category": "timeline",
                "accent": "#f97316",
            },
            {
                "title": "Challenge Card Grid",
                "description": "Build a grid of challenge cards with badges and timers.",
                "difficulty": "hard",
                "time_limit": 25,
                "category": "grid",
                "accent": "#8b5cf6",
            },
            {
                "title": "Mentor Spotlight",
                "description": "Design a spotlight panel with mentor bio and stats.",
                "difficulty": "medium",
                "time_limit": 18,
                "category": "profile",
                "accent": "#38bdf8",
            },
            {
                "title": "Schedule Card",
                "description": "Design a schedule card with open/close times and toggle.",
                "difficulty": "easy",
                "time_limit": 14,
                "category": "scheduler",
                "accent": "#818cf8",
            },
            {
                "title": "Profile Settings Form",
                "description": "Build a form layout with inputs and save button.",
                "difficulty": "medium",
                "time_limit": 20,
                "category": "form",
                "accent": "#22c55e",
            },
            {
                "title": "Activity Feed",
                "description": "Create a list of activity items with timestamps.",
                "difficulty": "medium",
                "time_limit": 18,
                "category": "feed",
                "accent": "#38bdf8",
            },
        ]

        for spec in extra_specs:
            accent = spec["accent"]
            challenges.append(
                {
                    "title": spec["title"],
                    "description": spec["description"],
                    "difficulty": spec["difficulty"],
                    "time_limit": spec["time_limit"],
                    "category": spec["category"],
                    "target_html": f"""<div class=\"card\">
  <div class=\"card-header\">
    <span class=\"pill\">{spec['category']}</span>
    <strong>{spec['title']}</strong>
  </div>
  <p>{spec['description']}</p>
  <div class=\"meta\">
    <span>Difficulty</span>
    <strong>{spec['difficulty'].title()}</strong>
  </div>
  <button>Open</button>
</div>""",
                    "target_css": f"""body {{
  font-family: 'Inter', sans-serif;
  background: #0f0b1d;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  color: #f8fafc;
}}
.card {{
  width: 360px;
  background: #1b1333;
  border-radius: 18px;
  padding: 22px;
  box-shadow: 0 16px 35px rgba(15, 23, 42, 0.35);
}}
.card-header {{
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 12px;
}}
.pill {{
  display: inline-flex;
  width: fit-content;
  padding: 6px 12px;
  border-radius: 999px;
  background: {accent}22;
  color: {accent};
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.2em;
}}
p {{
  color: #cbd5f5;
  font-size: 14px;
  margin: 0 0 18px;
}}
.meta {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 18px;
  font-size: 12px;
  color: #94a3b8;
}}
.meta strong {{
  color: #e2e8f0;
}}
button {{
  width: 100%;
  padding: 10px 14px;
  border-radius: 12px;
  border: 1px solid rgba(148, 163, 184, 0.3);
  background: transparent;
  color: #e2e8f0;
  font-weight: 600;
}}
""",
                    "target_js": "",
                }
            )

        for payload in challenges:
            challenge = Challenge.objects.create(**payload)
            self.stdout.write(self.style.SUCCESS(f"Created {challenge.title}"))
