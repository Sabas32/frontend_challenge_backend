from django.core.management.base import BaseCommand

from competition.models import Challenge


class Command(BaseCommand):
    help = "Seed starter challenges for local development."

    def handle(self, *args, **options):
        challenges = [
            {
                "id": "challenge-1",
                "title": "Modern Login Form",
                "description": "Create a clean, modern login form with email and password fields, a remember me checkbox, and a gradient submit button.",
                "difficulty": "easy",
                "time_limit": 15,
                "category": "form",
                "target_html": """<div class="login-card">
  <h2>Welcome Back</h2>
  <p>Sign in to continue.</p>
  <form>
    <label>Email</label>
    <input type="email" placeholder="you@example.com" />
    <label>Password</label>
    <input type="password" placeholder="" />
    <div class="row">
      <label class="check"><input type="checkbox" />Remember me</label>
      <a href="#">Forgot password?</a>
    </div>
    <button type="submit">Sign in</button>
  </form>
</div>""",
                "target_css": """body {
  font-family: 'Inter', sans-serif;
  background: #f5f7fb;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
}
.login-card {
  width: 360px;
  background: #fff;
  padding: 32px;
  border-radius: 16px;
  box-shadow: 0 20px 50px rgba(15, 23, 42, 0.12);
}
.login-card h2 { margin-bottom: 6px; }
.login-card p { color: #64748b; margin-bottom: 20px; }
label { font-size: 13px; color: #475569; }
input {
  width: 100%;
  padding: 12px 14px;
  margin: 8px 0 16px;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
}
.row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 12px;
  color: #64748b;
  margin-bottom: 18px;
}
button {
  width: 100%;
  padding: 12px;
  border: none;
  border-radius: 12px;
  background: #2563eb;
  color: white;
  font-weight: 600;
}
""",
                "target_js": "",
            },
            {
                "id": "challenge-2",
                "title": "Hero Section with CTA",
                "description": "Build a hero section with a headline, subtext, buttons, and a mock image card.",
                "difficulty": "medium",
                "time_limit": 20,
                "category": "landing",
                "target_html": """<section class="hero">
  <div class="text">
    <span class="pill">New Release</span>
    <h1>Build stunning dashboards faster.</h1>
    <p>Design, code, and ship modern UI in record time with ready-to-use templates.</p>
    <div class="actions">
      <button class="primary">Get Started</button>
      <button class="ghost">Live Preview</button>
    </div>
  </div>
  <div class="card">
    <div class="chart"></div>
    <div class="stats">
      <div><strong>86%</strong><span>Engagement</span></div>
      <div><strong>1.2k</strong><span>New leads</span></div>
    </div>
  </div>
</section>""",
                "target_css": """body {
  font-family: 'Inter', sans-serif;
  background: #0f172a;
  color: #f8fafc;
}
.hero {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 32px;
  padding: 60px;
}
.pill {
  display: inline-block;
  padding: 6px 12px;
  background: rgba(56,189,248,0.15);
  color: #38bdf8;
  border-radius: 999px;
  font-size: 12px;
}
.actions { display: flex; gap: 12px; margin-top: 18px; }
.primary {
  background: #38bdf8;
  border: none;
  padding: 10px 18px;
  border-radius: 10px;
}
.ghost {
  background: transparent;
  border: 1px solid rgba(148,163,184,0.4);
  color: #e2e8f0;
  padding: 10px 18px;
  border-radius: 10px;
}
.card {
  background: #111827;
  padding: 24px;
  border-radius: 20px;
}
.chart {
  height: 160px;
  background: linear-gradient(135deg, rgba(56,189,248,0.2), rgba(34,197,94,0.2));
  border-radius: 16px;
  margin-bottom: 20px;
}
.stats { display: flex; gap: 20px; }
.stats span { color: #94a3b8; font-size: 12px; }
""",
                "target_js": "",
            },
            {
                "id": "challenge-3",
                "title": "Stats Card Row",
                "description": "Create a row of KPI cards with icons and trend indicators.",
                "difficulty": "easy",
                "time_limit": 12,
                "category": "card",
                "target_html": """<div class="stats">
  <div class="stat">
    <div class="label">Revenue</div>
    <div class="value">$42.3k</div>
    <div class="trend up">+12.4%</div>
  </div>
  <div class="stat">
    <div class="label">Users</div>
    <div class="value">8,241</div>
    <div class="trend down">-3.1%</div>
  </div>
  <div class="stat">
    <div class="label">Conversion</div>
    <div class="value">4.8%</div>
    <div class="trend up">+0.9%</div>
  </div>
</div>""",
                "target_css": """body {
  font-family: 'Inter', sans-serif;
  background: #f8fafc;
  padding: 40px;
}
.stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}
.stat {
  background: white;
  border-radius: 16px;
  padding: 20px;
  box-shadow: 0 10px 25px rgba(15, 23, 42, 0.08);
}
.label { color: #94a3b8; font-size: 12px; }
.value { font-size: 24px; font-weight: 600; margin: 8px 0; }
.trend { font-size: 12px; font-weight: 600; }
.trend.up { color: #22c55e; }
.trend.down { color: #ef4444; }
""",
                "target_js": "",
            },
        ]

        for payload in challenges:
            challenge, created = Challenge.objects.get_or_create(
                id=payload["id"], defaults=payload
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created {challenge.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Skipped {challenge.title} (already exists)"))
