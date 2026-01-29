from django.core.management.base import BaseCommand

from competition.models import Challenge


class Command(BaseCommand):
    help = "Seed starter challenges for local development."

    def handle(self, *args, **options):
        Challenge.objects.all().delete()
        self.stdout.write(self.style.WARNING("Cleared existing challenges."))

        challenges = [
            {
                "title": "ISCC Top Navbar",
                "description": "Build a top navigation bar with logo, 4 links, a search input, and a profile button.",
                "difficulty": "easy",
                "time_limit": 12,
                "category": "navbar",
                "target_html": """<nav class="nav">
  <div class="logo">ISCC</div>
  <div class="links">
    <a href="#">Home</a>
    <a href="#">Challenges</a>
    <a href="#">Leaderboard</a>
    <a href="#">Rules</a>
  </div>
  <div class="actions">
    <input type="text" placeholder="Search challenges" />
    <button>Profile</button>
  </div>
</nav>""",
                "target_css": """body{margin:0;font-family:Inter,sans-serif;background:#0f0b1d;color:#f8fafc;}
.nav{display:flex;align-items:center;justify-content:space-between;padding:18px 28px;background:#17102b;border-bottom:1px solid rgba(148,163,184,0.12);}
.logo{font-weight:700;letter-spacing:0.2em;color:#c4b5fd;}
.links{display:flex;gap:18px;}
.links a{color:#cbd5f5;text-decoration:none;font-size:14px;}
.actions{display:flex;gap:10px;align-items:center;}
input{background:#0f0b1d;border:1px solid rgba(148,163,184,0.3);padding:8px 12px;border-radius:10px;color:#e2e8f0;}
button{background:#8b5cf6;border:none;padding:8px 14px;border-radius:10px;color:white;font-weight:600;}""",
                "target_js": "",
            },
            {
                "title": "ISCC Login Form",
                "description": "Create a login form with email, password, remember me, and primary button.",
                "difficulty": "easy",
                "time_limit": 12,
                "category": "form",
                "target_html": """<div class="card">
  <h2>Welcome back</h2>
  <p>Sign in to continue.</p>
  <label>Email</label>
  <input type="email" placeholder="you@example.com"/>
  <label>Password</label>
  <input type="password" placeholder="••••••••"/>
  <div class="row">
    <label class="check"><input type="checkbox"/>Remember me</label>
    <a href="#">Forgot password?</a>
  </div>
  <button>Sign in</button>
</div>""",
                "target_css": """body{margin:0;font-family:Inter,sans-serif;background:#0f0b1d;display:flex;align-items:center;justify-content:center;height:100vh;color:#f8fafc;}
.card{width:360px;background:#1b1333;padding:28px;border-radius:18px;box-shadow:0 18px 40px rgba(15,23,42,0.35);}
label{font-size:12px;color:#94a3b8;}
input{width:100%;margin:8px 0 14px;padding:10px 12px;border-radius:12px;border:1px solid rgba(148,163,184,0.3);background:#0f0b1d;color:#e2e8f0;}
.row{display:flex;align-items:center;justify-content:space-between;font-size:12px;color:#94a3b8;}
.row a{color:#c4b5fd;text-decoration:none;}
button{margin-top:16px;width:100%;padding:10px;border-radius:12px;border:none;background:#8b5cf6;color:white;font-weight:600;}""",
                "target_js": "",
            },
            {
                "title": "ISCC Challenge Card",
                "description": "Design a challenge card with title, difficulty pill, time, and start button.",
                "difficulty": "easy",
                "time_limit": 12,
                "category": "card",
                "target_html": """<div class="challenge">
  <span class="pill">Easy</span>
  <h3>Profile Card UI</h3>
  <p>Build a profile card with avatar, name, and stats.</p>
  <div class="meta">
    <span>Time: 20 min</span>
    <span>Score: 100</span>
  </div>
  <button>Start challenge</button>
</div>""",
                "target_css": """body{margin:0;font-family:Inter,sans-serif;background:#0f0b1d;display:flex;align-items:center;justify-content:center;height:100vh;color:#f8fafc;}
.challenge{width:360px;background:#1b1333;padding:24px;border-radius:18px;}
.pill{display:inline-flex;padding:6px 12px;border-radius:999px;background:rgba(34,197,94,0.2);color:#86efac;font-size:11px;letter-spacing:0.2em;text-transform:uppercase;}
.meta{display:flex;justify-content:space-between;color:#94a3b8;font-size:12px;margin:12px 0;}
button{width:100%;padding:10px;border-radius:12px;border:none;background:#8b5cf6;color:white;font-weight:600;}""",
                "target_js": "",
            },
            {
                "title": "ISCC Leaderboard Table",
                "description": "Create a simple leaderboard table header and one row.",
                "difficulty": "medium",
                "time_limit": 18,
                "category": "table",
                "target_html": """<div class="table">
  <div class="header">
    <span>Rank</span><span>Competitor</span><span>School</span><span>Score</span>
  </div>
  <div class="row">
    <span>#1</span><span>Ivan Kato</span><span>SMASK</span><span>98</span>
  </div>
</div>""",
                "target_css": """body{margin:0;font-family:Inter,sans-serif;background:#0f0b1d;color:#f8fafc;display:flex;align-items:center;justify-content:center;height:100vh;}
.table{width:520px;background:#1b1333;border-radius:16px;padding:16px;}
.header,.row{display:grid;grid-template-columns:80px 1.2fr 1fr 80px;gap:8px;padding:10px 12px;}
.header{color:#94a3b8;font-size:11px;text-transform:uppercase;letter-spacing:0.2em;border-bottom:1px solid rgba(148,163,184,0.2);}
.row{font-size:14px;}""",
                "target_js": "",
            },
            {
                "title": "ISCC Submission Form",
                "description": "Build a submission form with title input, description textarea, and submit button.",
                "difficulty": "easy",
                "time_limit": 12,
                "category": "form",
                "target_html": """<div class="panel">
  <h3>Submit your work</h3>
  <label>Title</label>
  <input type="text" placeholder="Challenge submission title"/>
  <label>Description</label>
  <textarea rows="4" placeholder="Describe your approach..."></textarea>
  <button>Submit</button>
</div>""",
                "target_css": """body{margin:0;font-family:Inter,sans-serif;background:#0f0b1d;display:flex;align-items:center;justify-content:center;height:100vh;color:#f8fafc;}
.panel{width:420px;background:#1b1333;padding:24px;border-radius:18px;}
input,textarea{width:100%;margin:8px 0 14px;padding:10px 12px;border-radius:12px;border:1px solid rgba(148,163,184,0.3);background:#0f0b1d;color:#e2e8f0;}
button{width:100%;padding:10px;border-radius:12px;border:none;background:#8b5cf6;color:white;font-weight:600;}""",
                "target_js": "",
            },
            {
                "title": "ISCC Stats Row",
                "description": "Create three stat cards in a row with label and value.",
                "difficulty": "easy",
                "time_limit": 10,
                "category": "cards",
                "target_html": """<div class="stats">
  <div class="stat"><span>Challenges</span><strong>12</strong></div>
  <div class="stat"><span>Submissions</span><strong>248</strong></div>
  <div class="stat"><span>Avg Score</span><strong>87%</strong></div>
</div>""",
                "target_css": """body{margin:0;font-family:Inter,sans-serif;background:#0f0b1d;display:flex;align-items:center;justify-content:center;height:100vh;color:#f8fafc;}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;}
.stat{background:#1b1333;padding:16px;border-radius:16px;min-width:160px;}
span{font-size:12px;color:#94a3b8;}
strong{display:block;margin-top:6px;font-size:22px;}""",
                "target_js": "",
            },
            {
                "title": "ISCC Side Navigation",
                "description": "Build a vertical sidebar with logo, 5 links, and a footer button.",
                "difficulty": "medium",
                "time_limit": 18,
                "category": "navbar",
                "target_html": """<aside class="sidebar">
  <div class="logo">ISCC</div>
  <nav>
    <a>Dashboard</a>
    <a>Challenges</a>
    <a>Leaderboard</a>
    <a>Workspace</a>
    <a>Settings</a>
  </nav>
  <button>Logout</button>
</aside>""",
                "target_css": """body{margin:0;font-family:Inter,sans-serif;background:#0f0b1d;color:#f8fafc;}
.sidebar{height:100vh;width:220px;background:#1b1333;padding:24px;display:flex;flex-direction:column;gap:18px;}
.logo{font-weight:700;letter-spacing:0.2em;}
nav{display:flex;flex-direction:column;gap:10px;}
nav a{color:#cbd5f5;text-decoration:none;}
button{margin-top:auto;padding:10px;border-radius:12px;border:none;background:#8b5cf6;color:white;font-weight:600;}""",
                "target_js": "",
            },
            {
                "title": "ISCC Header Search",
                "description": "Design a header with title, search field, and filter dropdown.",
                "difficulty": "easy",
                "time_limit": 10,
                "category": "header",
                "target_html": """<header class="header">
  <h2>Challenges</h2>
  <div class="controls">
    <input placeholder="Search"/>
    <select><option>All levels</option></select>
  </div>
</header>""",
                "target_css": """body{margin:0;font-family:Inter,sans-serif;background:#0f0b1d;color:#f8fafc;padding:24px;}
.header{display:flex;align-items:center;justify-content:space-between;background:#1b1333;padding:16px;border-radius:16px;}
.controls{display:flex;gap:10px;}
input,select{background:#0f0b1d;border:1px solid rgba(148,163,184,0.3);padding:8px 12px;border-radius:10px;color:#e2e8f0;}""",
                "target_js": "",
            },
            {
                "title": "ISCC Profile Settings",
                "description": "Create a settings form with name, school, and save button.",
                "difficulty": "medium",
                "time_limit": 18,
                "category": "form",
                "target_html": """<div class="panel">
  <h3>Profile settings</h3>
  <label>Full name</label>
  <input type="text" placeholder="Amina Nabirye"/>
  <label>School</label>
  <input type="text" placeholder="Makerere Hill School"/>
  <button>Save changes</button>
</div>""",
                "target_css": """body{margin:0;font-family:Inter,sans-serif;background:#0f0b1d;display:flex;align-items:center;justify-content:center;height:100vh;color:#f8fafc;}
.panel{width:420px;background:#1b1333;padding:24px;border-radius:18px;}
input{width:100%;margin:8px 0 14px;padding:10px 12px;border-radius:12px;border:1px solid rgba(148,163,184,0.3);background:#0f0b1d;color:#e2e8f0;}
button{width:100%;padding:10px;border-radius:12px;border:none;background:#8b5cf6;color:white;font-weight:600;}""",
                "target_js": "",
            },
            {
                "title": "SafeBoda Ride Request Form",
                "description": "Build a simple ride request form with pickup, dropoff, and confirm button.",
                "difficulty": "easy",
                "time_limit": 12,
                "category": "form",
                "target_html": """<div class="panel">
  <h3>Request a ride</h3>
  <label>Pickup</label>
  <input placeholder="Kampala Road"/>
  <label>Dropoff</label>
  <input placeholder="Kololo Hill"/>
  <button>Confirm ride</button>
</div>""",
                "target_css": """body{margin:0;font-family:Inter,sans-serif;background:#0f0b1d;display:flex;align-items:center;justify-content:center;height:100vh;color:#f8fafc;}
.panel{width:360px;background:#1b1333;padding:24px;border-radius:18px;}
input{width:100%;margin:8px 0 14px;padding:10px 12px;border-radius:12px;border:1px solid rgba(148,163,184,0.3);background:#0f0b1d;color:#e2e8f0;}
button{width:100%;padding:10px;border-radius:12px;border:none;background:#22c55e;color:white;font-weight:600;}""",
                "target_js": "",
            },
            {
                "title": "SafeBoda Wallet Card",
                "description": "Create a wallet summary card with balance and top up button.",
                "difficulty": "easy",
                "time_limit": 12,
                "category": "card",
                "target_html": """<div class="wallet">
  <span>Wallet balance</span>
  <h2>UGX 84,500</h2>
  <button>Top up</button>
</div>""",
                "target_css": """body{margin:0;font-family:Inter,sans-serif;background:#0f0b1d;display:flex;align-items:center;justify-content:center;height:100vh;color:#f8fafc;}
.wallet{width:300px;background:#1b1333;padding:20px;border-radius:18px;text-align:center;}
button{margin-top:12px;width:100%;padding:10px;border-radius:12px;border:none;background:#22c55e;color:white;font-weight:600;}""",
                "target_js": "",
            },
            {
                "title": "SafeBoda Trip Summary Card",
                "description": "Design a trip summary card with route, time, and fare.",
                "difficulty": "medium",
                "time_limit": 18,
                "category": "card",
                "target_html": """<div class="trip">
  <h3>Trip summary</h3>
  <div class="row"><span>Pickup</span><strong>Wandegeya</strong></div>
  <div class="row"><span>Dropoff</span><strong>Ntinda</strong></div>
  <div class="row"><span>Fare</span><strong>UGX 8,000</strong></div>
  <button>Pay driver</button>
</div>""",
                "target_css": """body{margin:0;font-family:Inter,sans-serif;background:#0f0b1d;display:flex;align-items:center;justify-content:center;height:100vh;color:#f8fafc;}
.trip{width:360px;background:#1b1333;padding:22px;border-radius:18px;}
.row{display:flex;justify-content:space-between;color:#cbd5f5;margin:8px 0;}
button{margin-top:12px;width:100%;padding:10px;border-radius:12px;border:none;background:#22c55e;color:white;font-weight:600;}""",
                "target_js": "",
            },
            {
                "title": "SafeBoda Driver Card",
                "description": "Create a driver card with name, rating, and call button.",
                "difficulty": "easy",
                "time_limit": 12,
                "category": "card",
                "target_html": """<div class="driver">
  <div class="avatar">DK</div>
  <div>
    <h3>Denis Kato</h3>
    <p>Rating 4.9 · 1,024 trips</p>
  </div>
  <button>Call</button>
</div>""",
                "target_css": """body{margin:0;font-family:Inter,sans-serif;background:#0f0b1d;display:flex;align-items:center;justify-content:center;height:100vh;color:#f8fafc;}
.driver{width:420px;background:#1b1333;padding:18px;border-radius:18px;display:flex;gap:14px;align-items:center;}
.avatar{width:44px;height:44px;border-radius:12px;background:#22c55e;display:grid;place-items:center;font-weight:700;}
button{margin-left:auto;padding:8px 14px;border-radius:10px;border:none;background:#22c55e;color:white;font-weight:600;}""",
                "target_js": "",
            },
            {
                "title": "SafeBoda Earnings Row",
                "description": "Build an earnings row with three columns: today, week, month.",
                "difficulty": "medium",
                "time_limit": 18,
                "category": "table",
                "target_html": """<div class="earnings">
  <div><span>Today</span><strong>UGX 45,000</strong></div>
  <div><span>This week</span><strong>UGX 280,000</strong></div>
  <div><span>This month</span><strong>UGX 1.2M</strong></div>
</div>""",
                "target_css": """body{margin:0;font-family:Inter,sans-serif;background:#0f0b1d;display:flex;align-items:center;justify-content:center;height:100vh;color:#f8fafc;}
.earnings{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;background:#1b1333;padding:18px;border-radius:18px;}
span{display:block;color:#94a3b8;font-size:12px;}
strong{display:block;margin-top:6px;font-size:18px;}""",
                "target_js": "",
            },
            {
                "title": "SafeBoda Support Chat",
                "description": "Create a chat layout with two messages and an input box.",
                "difficulty": "hard",
                "time_limit": 24,
                "category": "chat",
                "target_html": """<div class="chat">
  <div class="bubble">Hello, how can we help?</div>
  <div class="bubble user">I need a refund.</div>
  <div class="input">
    <input placeholder="Type a message"/>
    <button>Send</button>
  </div>
</div>""",
                "target_css": """body{margin:0;font-family:Inter,sans-serif;background:#0f0b1d;display:flex;align-items:center;justify-content:center;height:100vh;color:#f8fafc;}
.chat{width:360px;background:#1b1333;padding:18px;border-radius:18px;display:flex;flex-direction:column;gap:10px;}
.bubble{background:#2a1d4a;padding:10px;border-radius:12px;max-width:80%;}
.bubble.user{align-self:flex-end;background:#22c55e;color:#0f0b1d;}
.input{display:flex;gap:8px;margin-top:10px;}
input{flex:1;padding:8px 10px;border-radius:10px;border:1px solid rgba(148,163,184,0.3);background:#0f0b1d;color:#e2e8f0;}
button{padding:8px 12px;border-radius:10px;border:none;background:#22c55e;color:white;font-weight:600;}""",
                "target_js": "",
            },
        ]

        for payload in challenges:
            challenge = Challenge.objects.create(**payload)
            self.stdout.write(self.style.SUCCESS(f"Created {challenge.title}"))
