from django.core.management.base import BaseCommand

from competition.models import Challenge


class Command(BaseCommand):
    help = "Seed starter challenges for local development."

    def handle(self, *args, **options):
        Challenge.objects.all().delete()
        self.stdout.write(self.style.WARNING("Cleared existing challenges."))

        challenges = []

        specs = [
            {
                "title": "ISCC Welcome Hero",
                "description": "Design a hero section for the ISCC landing page with badge, headline, CTA buttons, and stats card.",
                "difficulty": "easy",
                "time_limit": 18,
                "category": "landing",
                "accent": "#8b5cf6",
            },
            {
                "title": "ISCC Competitor Card",
                "description": "Create a competitor profile card with school, handle, and performance stats.",
                "difficulty": "easy",
                "time_limit": 14,
                "category": "card",
                "accent": "#22d3ee",
            },
            {
                "title": "ISCC Challenge Brief",
                "description": "Design a challenge brief panel with difficulty pill, time limit, and start button.",
                "difficulty": "medium",
                "time_limit": 20,
                "category": "layout",
                "accent": "#34d399",
            },
            {
                "title": "ISCC Leaderboard Row",
                "description": "Build a leaderboard row with rank, avatar, name, and score badge.",
                "difficulty": "easy",
                "time_limit": 12,
                "category": "leaderboard",
                "accent": "#facc15",
            },
            {
                "title": "ISCC Stat Tiles",
                "description": "Create a row of stat tiles for submissions, avg score, and open challenges.",
                "difficulty": "medium",
                "time_limit": 20,
                "category": "dashboard",
                "accent": "#38bdf8",
            },
            {
                "title": "ISCC Schedule Card",
                "description": "Design a schedule card showing open/close times with a toggle.",
                "difficulty": "easy",
                "time_limit": 14,
                "category": "scheduler",
                "accent": "#818cf8",
            },
            {
                "title": "ISCC Announcement Banner",
                "description": "Create an announcement banner for ISCC updates with CTA button.",
                "difficulty": "easy",
                "time_limit": 12,
                "category": "alert",
                "accent": "#f59e0b",
            },
            {
                "title": "ISCC Activity Feed",
                "description": "Design an activity feed for recent submissions with timestamps.",
                "difficulty": "medium",
                "time_limit": 18,
                "category": "feed",
                "accent": "#60a5fa",
            },
            {
                "title": "SafeBoda Ride Card",
                "description": "Create a ride request card with pickup, dropoff, fare, and driver CTA.",
                "difficulty": "easy",
                "time_limit": 14,
                "category": "card",
                "accent": "#22c55e",
            },
            {
                "title": "SafeBoda Driver Profile",
                "description": "Design a driver profile with rating, trips, and contact actions.",
                "difficulty": "easy",
                "time_limit": 14,
                "category": "profile",
                "accent": "#16a34a",
            },
            {
                "title": "SafeBoda Trip Summary",
                "description": "Build a trip summary panel with route, time, and payment method.",
                "difficulty": "medium",
                "time_limit": 18,
                "category": "summary",
                "accent": "#22d3ee",
            },
            {
                "title": "SafeBoda Earnings Tiles",
                "description": "Create earnings tiles for daily, weekly, and monthly totals.",
                "difficulty": "medium",
                "time_limit": 20,
                "category": "dashboard",
                "accent": "#84cc16",
            },
            {
                "title": "SafeBoda Support Chat",
                "description": "Design a compact support chat panel with messages and input.",
                "difficulty": "hard",
                "time_limit": 24,
                "category": "chat",
                "accent": "#38bdf8",
            },
            {
                "title": "SafeBoda Booking Flow",
                "description": "Build a stepper showing request, driver match, and trip status.",
                "difficulty": "hard",
                "time_limit": 25,
                "category": "timeline",
                "accent": "#22c55e",
            },
            {
                "title": "SafeBoda Wallet Panel",
                "description": "Create a wallet panel with balance, top-up button, and recent transactions.",
                "difficulty": "medium",
                "time_limit": 20,
                "category": "finance",
                "accent": "#14b8a6",
            },
        ]

        for spec in specs:
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
