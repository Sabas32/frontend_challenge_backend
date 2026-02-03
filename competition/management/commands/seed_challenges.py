from django.core.management.base import BaseCommand

from competition.models import Challenge


class Command(BaseCommand):
    help = "Seed starter challenges for local development."

    def handle(self, *args, **options):
        Challenge.objects.all().delete()
        self.stdout.write(self.style.WARNING("Cleared existing challenges."))

        challenges = [
            # EASY (10)
            {
                "title": "ISCC Primary Button",
                "description": "Create one rounded primary button centered on the page.",
                "difficulty": "easy",
                "time_limit": 8,
                "category": "button",
                "target_html": """<button class=\"btn\">Start Challenge</button>""",
                "target_css": """body{margin:0;display:grid;place-items:center;height:100vh;background:transparent;font-family:Inter,sans-serif;}\n.btn{background:#2563eb;color:#fff;border:none;padding:12px 18px;border-radius:10px;font-weight:700;cursor:pointer;}""",
                "target_js": "",
            },
            {
                "title": "ISCC Two Action Buttons",
                "description": "Build a row with a primary Save button and secondary Cancel button.",
                "difficulty": "easy",
                "time_limit": 9,
                "category": "button",
                "target_html": """<div class=\"row\"><button class=\"ghost\">Cancel</button><button class=\"primary\">Save</button></div>""",
                "target_css": """body{margin:0;display:grid;place-items:center;height:100vh;background:transparent;font-family:Inter,sans-serif;}\n.row{display:flex;gap:12px;}\nbutton{padding:10px 16px;border-radius:10px;font-weight:600;cursor:pointer;}\n.ghost{border:1px solid #94a3b8;background:transparent;color:#cbd5e1;}\n.primary{border:none;background:#0ea5e9;color:white;}""",
                "target_js": "",
            },
            {
                "title": "ISCC Basic Alert Card",
                "description": "Design a compact alert card with title, message, and close button.",
                "difficulty": "easy",
                "time_limit": 10,
                "category": "card",
                "target_html": """<div class=\"card\"><h3>Update ready</h3><p>New challenge set is available.</p><button>Close</button></div>""",
                "target_css": """body{margin:0;display:grid;place-items:center;height:100vh;background:transparent;font-family:Inter,sans-serif;color:#e2e8f0;}\n.card{width:320px;padding:18px;border-radius:14px;background:#0f172a;border:1px solid #1e293b;}\nh3{margin:0 0 6px;}p{margin:0 0 14px;color:#94a3b8;}button{border:none;background:#334155;color:#fff;padding:8px 12px;border-radius:8px;}""",
                "target_js": "",
            },
            {
                "title": "ISCC Tiny Login Form",
                "description": "Build a simple form with username, password, and sign in button.",
                "difficulty": "easy",
                "time_limit": 10,
                "category": "form",
                "target_html": """<form class=\"card\"><h3>Sign in</h3><input placeholder=\"Username\"/><input type=\"password\" placeholder=\"Password\"/><button>Sign in</button></form>""",
                "target_css": """body{margin:0;height:100vh;display:grid;place-items:center;background:transparent;font-family:Inter,sans-serif;}\n.card{display:flex;flex-direction:column;gap:10px;width:300px;background:#111827;padding:18px;border-radius:14px;}\ninput{padding:10px;border-radius:10px;border:1px solid #374151;background:transparent;color:#e5e7eb;}\nbutton{padding:10px;border-radius:10px;border:none;background:#22c55e;color:#052e16;font-weight:700;}""",
                "target_js": "",
            },
            {
                "title": "ISCC Status Badge Row",
                "description": "Create three status badges: Active, Pending, and Closed.",
                "difficulty": "easy",
                "time_limit": 8,
                "category": "badge",
                "target_html": """<div class=\"badges\"><span class=\"ok\">Active</span><span class=\"wait\">Pending</span><span class=\"off\">Closed</span></div>""",
                "target_css": """body{margin:0;display:grid;place-items:center;height:100vh;background:transparent;font-family:Inter,sans-serif;}\n.badges{display:flex;gap:10px;}\nspan{padding:6px 11px;border-radius:999px;font-size:12px;font-weight:700;}\n.ok{background:#14532d;color:#86efac;}.wait{background:#78350f;color:#fcd34d;}.off{background:#7f1d1d;color:#fca5a5;}""",
                "target_js": "",
            },
            {
                "title": "SafeBoda Book Ride Button",
                "description": "Create a bright orange Book Ride button centered on screen.",
                "difficulty": "easy",
                "time_limit": 8,
                "category": "button",
                "target_html": """<button class=\"ride\">Book Ride</button>""",
                "target_css": """body{margin:0;height:100vh;display:grid;place-items:center;background:transparent;font-family:Inter,sans-serif;}\n.ride{background:#f97316;color:white;border:none;padding:12px 20px;border-radius:999px;font-weight:700;letter-spacing:.02em;}""",
                "target_js": "",
            },
            {
                "title": "SafeBoda Fare Pill",
                "description": "Build a fare pill showing text and amount in one horizontal chip.",
                "difficulty": "easy",
                "time_limit": 8,
                "category": "badge",
                "target_html": """<div class=\"pill\"><span>Estimated fare</span><strong>UGX 8,500</strong></div>""",
                "target_css": """body{margin:0;height:100vh;display:grid;place-items:center;background:transparent;font-family:Inter,sans-serif;}\n.pill{display:flex;gap:10px;align-items:center;padding:10px 14px;border-radius:999px;background:#1f2937;color:#e5e7eb;}\nstrong{color:#fb923c;}""",
                "target_js": "",
            },
            {
                "title": "SafeBoda Driver Mini Card",
                "description": "Design a mini card with avatar initials, name, and rating.",
                "difficulty": "easy",
                "time_limit": 10,
                "category": "card",
                "target_html": """<div class=\"card\"><div class=\"avatar\">DK</div><div><h4>Denis Kato</h4><p>4.9 rating</p></div></div>""",
                "target_css": """body{margin:0;height:100vh;display:grid;place-items:center;background:transparent;font-family:Inter,sans-serif;color:#f1f5f9;}\n.card{display:flex;align-items:center;gap:12px;background:#0f172a;padding:14px 16px;border-radius:14px;}\n.avatar{width:38px;height:38px;border-radius:10px;background:#f97316;display:grid;place-items:center;font-weight:700;color:#111827;}\nh4{margin:0;}p{margin:2px 0 0;color:#94a3b8;font-size:13px;}""",
                "target_js": "",
            },
            {
                "title": "SafeBoda Pickup Form",
                "description": "Create two stacked inputs (pickup and dropoff) and a confirm button.",
                "difficulty": "easy",
                "time_limit": 10,
                "category": "form",
                "target_html": """<div class=\"box\"><input placeholder=\"Pickup\"/><input placeholder=\"Dropoff\"/><button>Confirm Trip</button></div>""",
                "target_css": """body{margin:0;height:100vh;display:grid;place-items:center;background:transparent;font-family:Inter,sans-serif;}\n.box{width:320px;display:flex;flex-direction:column;gap:10px;background:#111827;padding:16px;border-radius:14px;}\ninput{padding:10px;border-radius:10px;border:1px solid #374151;background:transparent;color:#e5e7eb;}\nbutton{padding:10px;border:none;border-radius:10px;background:#f97316;color:white;font-weight:700;}""",
                "target_js": "",
            },
            {
                "title": "SafeBoda Wallet Balance Tile",
                "description": "Build a tile with Wallet title, amount, and a Top Up button.",
                "difficulty": "easy",
                "time_limit": 10,
                "category": "card",
                "target_html": """<div class=\"tile\"><span>Wallet</span><h2>UGX 84,500</h2><button>Top Up</button></div>""",
                "target_css": """body{margin:0;height:100vh;display:grid;place-items:center;background:transparent;font-family:Inter,sans-serif;color:#f8fafc;}\n.tile{width:280px;background:#0b1220;border:1px solid #1e293b;border-radius:14px;padding:16px;}\nspan{color:#94a3b8;font-size:13px;}h2{margin:6px 0 14px;}button{width:100%;padding:10px;border:none;border-radius:10px;background:#f97316;color:#fff;font-weight:700;}""",
                "target_js": "",
            },
            # MEDIUM (10)
            {
                "title": "ISCC Challenge List Item",
                "description": "Create a challenge list card with title, difficulty chip, time chip, and Start button.",
                "difficulty": "medium",
                "time_limit": 14,
                "category": "list",
                "target_html": """<article class=\"item\"><div><h3>Hero Section Challenge</h3><p>Build a responsive hero with CTA.</p><div class=\"chips\"><span>Medium</span><span>20 min</span></div></div><button>Start</button></article>""",
                "target_css": """body{margin:0;padding:24px;background:transparent;font-family:Inter,sans-serif;color:#e2e8f0;}\n.item{display:flex;justify-content:space-between;gap:16px;align-items:center;background:#0f172a;border:1px solid #1e293b;border-radius:16px;padding:18px;}\nh3{margin:0 0 6px;}p{margin:0 0 10px;color:#94a3b8;}.chips{display:flex;gap:8px;}span{padding:6px 10px;border-radius:999px;background:#1e293b;font-size:12px;}\nbutton{border:none;background:#06b6d4;color:#083344;padding:10px 16px;border-radius:10px;font-weight:700;}""",
                "target_js": "",
            },
            {
                "title": "ISCC Top Navigation",
                "description": "Build a top nav with logo, 4 links, search field, and profile avatar.",
                "difficulty": "medium",
                "time_limit": 16,
                "category": "navbar",
                "target_html": """<nav class=\"nav\"><div class=\"logo\">ISCC</div><div class=\"links\"><a>Home</a><a>Challenges</a><a>Leaderboard</a><a>Rules</a></div><div class=\"right\"><input placeholder=\"Search\"/><div class=\"avatar\">AL</div></div></nav>""",
                "target_css": """body{margin:0;background:transparent;font-family:Inter,sans-serif;color:#e2e8f0;}\n.nav{display:flex;align-items:center;justify-content:space-between;padding:14px 20px;background:#111827;border-bottom:1px solid #1f2937;}\n.logo{font-weight:800;letter-spacing:.08em;}.links{display:flex;gap:16px;color:#cbd5e1;}.right{display:flex;gap:10px;align-items:center;}\ninput{padding:8px 11px;border-radius:10px;border:1px solid #374151;background:transparent;color:#e5e7eb;}\n.avatar{width:34px;height:34px;border-radius:50%;display:grid;place-items:center;background:#0ea5e9;color:#082f49;font-weight:800;}""",
                "target_js": "",
            },
            {
                "title": "ISCC Leaderboard Table",
                "description": "Create a table-like block with header and 3 rows for rank, name, school, score.",
                "difficulty": "medium",
                "time_limit": 18,
                "category": "table",
                "target_html": """<section class=\"board\"><div class=\"head\"><span>Rank</span><span>Name</span><span>School</span><span>Score</span></div><div class=\"row\"><span>#1</span><span>Amina N.</span><span>Gayaza HS</span><span>98%</span></div><div class=\"row\"><span>#2</span><span>John K.</span><span>SMACK</span><span>95%</span></div><div class=\"row\"><span>#3</span><span>Irene T.</span><span>Mt St Mary</span><span>93%</span></div></section>""",
                "target_css": """body{margin:0;min-height:100vh;display:grid;place-items:center;background:transparent;font-family:Inter,sans-serif;color:#f1f5f9;}\n.board{width:640px;background:#0f172a;border:1px solid #1e293b;border-radius:16px;overflow:hidden;}\n.head,.row{display:grid;grid-template-columns:90px 1.2fr 1fr 100px;padding:12px 14px;gap:8px;}\n.head{font-size:12px;text-transform:uppercase;letter-spacing:.06em;color:#94a3b8;background:#111827;}\n.row{border-top:1px solid #1e293b;}""",
                "target_js": "",
            },
            {
                "title": "ISCC Sidebar Layout",
                "description": "Build a vertical sidebar with logo, five links, and logout button at bottom.",
                "difficulty": "medium",
                "time_limit": 16,
                "category": "layout",
                "target_html": """<aside class=\"side\"><h2>ISCC</h2><nav><a>Dashboard</a><a>Challenges</a><a>Leaderboard</a><a>Workspace</a><a>Settings</a></nav><button>Logout</button></aside>""",
                "target_css": """body{margin:0;background:transparent;font-family:Inter,sans-serif;color:#e2e8f0;}\n.side{height:100vh;width:240px;padding:20px;background:#0f172a;display:flex;flex-direction:column;box-sizing:border-box;}\nh2{margin:0 0 16px;letter-spacing:.08em;}nav{display:flex;flex-direction:column;gap:10px;}\na{color:#cbd5e1;padding:8px 10px;border-radius:8px;background:#111827;}button{margin-top:auto;border:none;background:#334155;color:#fff;padding:10px;border-radius:10px;}""",
                "target_js": "",
            },
            {
                "title": "ISCC Assignment Composer",
                "description": "Create a form with title input, difficulty select, textarea, and publish button.",
                "difficulty": "medium",
                "time_limit": 18,
                "category": "form",
                "target_html": """<form class=\"card\"><h3>New challenge</h3><input placeholder=\"Title\"/><select><option>Easy</option><option>Medium</option><option>Hard</option></select><textarea rows=\"4\" placeholder=\"Challenge brief\"></textarea><button>Publish</button></form>""",
                "target_css": """body{margin:0;min-height:100vh;display:grid;place-items:center;background:transparent;font-family:Inter,sans-serif;}\n.card{width:420px;display:flex;flex-direction:column;gap:10px;background:#111827;padding:18px;border-radius:14px;}\nh3{margin:0 0 4px;color:#f8fafc;}input,select,textarea{border:1px solid #374151;background:transparent;color:#e5e7eb;padding:10px;border-radius:10px;}\nbutton{border:none;background:#22c55e;color:#052e16;padding:10px;border-radius:10px;font-weight:700;}""",
                "target_js": "",
            },
            {
                "title": "SafeBoda Trip Summary",
                "description": "Build a card showing pickup, dropoff, time, fare and a Pay button.",
                "difficulty": "medium",
                "time_limit": 16,
                "category": "card",
                "target_html": """<div class=\"trip\"><h3>Trip Summary</h3><div class=\"row\"><span>Pickup</span><strong>Wandegeya</strong></div><div class=\"row\"><span>Dropoff</span><strong>Ntinda</strong></div><div class=\"row\"><span>ETA</span><strong>14 min</strong></div><div class=\"row\"><span>Fare</span><strong>UGX 8,000</strong></div><button>Pay Driver</button></div>""",
                "target_css": """body{margin:0;min-height:100vh;display:grid;place-items:center;background:transparent;font-family:Inter,sans-serif;color:#f8fafc;}\n.trip{width:360px;background:#0f172a;border:1px solid #1e293b;border-radius:16px;padding:16px;}\n.row{display:flex;justify-content:space-between;margin:8px 0;color:#cbd5e1;}span{color:#94a3b8;}\nbutton{width:100%;margin-top:10px;border:none;background:#f97316;color:#fff;padding:10px;border-radius:10px;font-weight:700;}""",
                "target_js": "",
            },
            {
                "title": "SafeBoda Driver Earnings Grid",
                "description": "Create a 3-column earnings grid for today, week, and month values.",
                "difficulty": "medium",
                "time_limit": 14,
                "category": "grid",
                "target_html": """<section class=\"grid\"><article><span>Today</span><strong>UGX 45k</strong></article><article><span>This week</span><strong>UGX 280k</strong></article><article><span>This month</span><strong>UGX 1.2M</strong></article></section>""",
                "target_css": """body{margin:0;min-height:100vh;display:grid;place-items:center;background:transparent;font-family:Inter,sans-serif;color:#f8fafc;}\n.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;width:680px;}\narticle{background:#0f172a;border:1px solid #1e293b;border-radius:14px;padding:14px;}\nspan{color:#94a3b8;font-size:13px;}strong{display:block;margin-top:8px;font-size:20px;}""",
                "target_js": "",
            },
            {
                "title": "SafeBoda Support Inbox",
                "description": "Design a simple inbox with three conversation rows and unread badge.",
                "difficulty": "medium",
                "time_limit": 18,
                "category": "list",
                "target_html": """<div class=\"inbox\"><h3>Support Inbox</h3><div class=\"row\"><span>Refund issue</span><b>2</b></div><div class=\"row\"><span>Lost item</span><b>1</b></div><div class=\"row\"><span>Payment failed</span><b>0</b></div></div>""",
                "target_css": """body{margin:0;min-height:100vh;display:grid;place-items:center;background:transparent;font-family:Inter,sans-serif;color:#f8fafc;}\n.inbox{width:420px;background:#0f172a;border:1px solid #1e293b;border-radius:16px;padding:16px;}\nh3{margin:0 0 10px;}.row{display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-top:1px solid #1e293b;}\nb{background:#f97316;color:#fff;border-radius:999px;min-width:22px;height:22px;display:grid;place-items:center;font-size:12px;}""",
                "target_js": "",
            },
            {
                "title": "SafeBoda Promo Banner",
                "description": "Build a promo banner with title, subtitle, and Redeem button.",
                "difficulty": "medium",
                "time_limit": 14,
                "category": "banner",
                "target_html": """<section class=\"banner\"><div><h3>Weekend Promo</h3><p>Get 20% off on all rides today.</p></div><button>Redeem</button></section>""",
                "target_css": """body{margin:0;padding:24px;background:transparent;font-family:Inter,sans-serif;color:#f8fafc;}\n.banner{display:flex;justify-content:space-between;gap:14px;align-items:center;background:#7c2d12;border-radius:16px;padding:16px 18px;}\nh3{margin:0 0 6px;}p{margin:0;color:#fed7aa;}button{border:none;background:#fff;color:#9a3412;padding:10px 14px;border-radius:10px;font-weight:700;}""",
                "target_js": "",
            },
            {
                "title": "SafeBoda Multi-Stop Form",
                "description": "Create a route form with pickup, stop 1, stop 2, and final destination fields.",
                "difficulty": "medium",
                "time_limit": 18,
                "category": "form",
                "target_html": """<form class=\"panel\"><input placeholder=\"Pickup\"/><input placeholder=\"Stop 1\"/><input placeholder=\"Stop 2\"/><input placeholder=\"Destination\"/><button>Review Route</button></form>""",
                "target_css": """body{margin:0;min-height:100vh;display:grid;place-items:center;background:transparent;font-family:Inter,sans-serif;}\n.panel{width:360px;display:flex;flex-direction:column;gap:10px;background:#0f172a;border:1px solid #1e293b;padding:16px;border-radius:14px;}\ninput{padding:10px;border-radius:10px;border:1px solid #334155;background:transparent;color:#e2e8f0;}\nbutton{padding:10px;border:none;border-radius:10px;background:#f97316;color:white;font-weight:700;}""",
                "target_js": "",
            },
            # HARD (5)
            {
                "title": "ISCC Tabbed Workspace",
                "description": "Build HTML/CSS/JS tabs where clicking a tab shows matching panel content.",
                "difficulty": "hard",
                "time_limit": 24,
                "category": "interactive",
                "target_html": """<div class=\"tabs\"><div class=\"tab-row\"><button data-tab=\"html\" class=\"active\">HTML</button><button data-tab=\"css\">CSS</button><button data-tab=\"js\">JS</button></div><section class=\"panel show\" data-panel=\"html\">HTML editor panel</section><section class=\"panel\" data-panel=\"css\">CSS editor panel</section><section class=\"panel\" data-panel=\"js\">JS editor panel</section></div>""",
                "target_css": """body{margin:0;min-height:100vh;display:grid;place-items:center;background:transparent;font-family:Inter,sans-serif;color:#f8fafc;}\n.tabs{width:520px;background:#0f172a;border:1px solid #1e293b;border-radius:16px;padding:14px;}\n.tab-row{display:flex;gap:8px;margin-bottom:12px;}button{border:1px solid #334155;background:transparent;color:#cbd5e1;padding:8px 12px;border-radius:8px;cursor:pointer;}\nbutton.active{background:#2563eb;color:white;border-color:#2563eb;}.panel{display:none;padding:14px;border-radius:10px;background:#111827;}.panel.show{display:block;}""",
                "target_js": """const tabs=[...document.querySelectorAll('[data-tab]')];
const panels=[...document.querySelectorAll('[data-panel]')];
tabs.forEach((tab)=>tab.addEventListener('click',()=>{
  tabs.forEach((t)=>t.classList.remove('active'));
  panels.forEach((p)=>p.classList.remove('show'));
  tab.classList.add('active');
  const panel=document.querySelector(`[data-panel="${tab.dataset.tab}"]`);
  if(panel) panel.classList.add('show');
}));""",
            },
            {
                "title": "ISCC Countdown Timer Badge",
                "description": "Create a 60-second timer that updates every second and turns red under 15s.",
                "difficulty": "hard",
                "time_limit": 24,
                "category": "interactive",
                "target_html": """<div class=\"timer\"><span id=\"label\">Time left</span><strong id=\"count\">60</strong></div>""",
                "target_css": """body{margin:0;min-height:100vh;display:grid;place-items:center;background:transparent;font-family:Inter,sans-serif;color:#f8fafc;}\n.timer{display:flex;gap:10px;align-items:center;padding:14px 18px;border-radius:999px;background:#0f172a;border:1px solid #1e293b;}\n#count{font-size:28px;color:#22c55e;min-width:44px;text-align:right;}#count.warn{color:#ef4444;}""",
                "target_js": """let n=60;
const count=document.getElementById('count');
const id=setInterval(()=>{
  n-=1;
  count.textContent=String(n);
  if(n<=15) count.classList.add('warn');
  if(n<=0) clearInterval(id);
},1000);""",
            },
            {
                "title": "SafeBoda Fare Estimator",
                "description": "Build a mini estimator: base 3000 + 1200 per km from input and show total.",
                "difficulty": "hard",
                "time_limit": 26,
                "category": "interactive",
                "target_html": """<div class=\"calc\"><label>Distance (km)</label><input id=\"km\" type=\"number\" min=\"1\" value=\"3\"/><p id=\"out\">UGX 6,600</p></div>""",
                "target_css": """body{margin:0;min-height:100vh;display:grid;place-items:center;background:transparent;font-family:Inter,sans-serif;color:#f8fafc;}\n.calc{width:320px;background:#0f172a;border:1px solid #1e293b;border-radius:14px;padding:16px;}\nlabel{display:block;margin-bottom:8px;color:#94a3b8;}input{width:100%;padding:10px;border-radius:10px;border:1px solid #334155;background:transparent;color:#e2e8f0;}\n#out{margin:12px 0 0;font-size:24px;color:#fb923c;font-weight:800;}""",
                "target_js": """const km=document.getElementById('km');
const out=document.getElementById('out');
function render(){
  const value=Math.max(1, Number(km.value||1));
  const total=3000 + value*1200;
  out.textContent=`UGX ${total.toLocaleString()}`;
}
km.addEventListener('input', render);
render();""",
            },
            {
                "title": "SafeBoda Support Chat UI",
                "description": "Create a chat panel with message list and send box; sending appends a new bubble.",
                "difficulty": "hard",
                "time_limit": 26,
                "category": "chat",
                "target_html": """<div class=\"chat\"><div id=\"feed\"><div class=\"msg\">Hello, how can we help?</div></div><div class=\"input\"><input id=\"text\" placeholder=\"Type message\"/><button id=\"send\">Send</button></div></div>""",
                "target_css": """body{margin:0;min-height:100vh;display:grid;place-items:center;background:transparent;font-family:Inter,sans-serif;color:#f8fafc;}\n.chat{width:360px;background:#0f172a;border:1px solid #1e293b;border-radius:16px;padding:12px;display:flex;flex-direction:column;gap:10px;}\n#feed{display:flex;flex-direction:column;gap:8px;max-height:220px;overflow:auto;}.msg{background:#1f2937;padding:9px 10px;border-radius:10px;max-width:85%;}\n.msg.me{align-self:flex-end;background:#f97316;color:white;}.input{display:flex;gap:8px;}input{flex:1;padding:9px;border-radius:9px;border:1px solid #334155;background:transparent;color:#e2e8f0;}\nbutton{border:none;background:#f97316;color:#fff;padding:9px 12px;border-radius:9px;font-weight:700;}""",
                "target_js": """const btn=document.getElementById('send');
const input=document.getElementById('text');
const feed=document.getElementById('feed');
btn.addEventListener('click',()=>{
  const text=input.value.trim();
  if(!text) return;
  const el=document.createElement('div');
  el.className='msg me';
  el.textContent=text;
  feed.appendChild(el);
  input.value='';
});""",
            },
            {
                "title": "ISCC Live Score Slider",
                "description": "Build a range slider from 0-100 with live numeric value and color bands.",
                "difficulty": "hard",
                "time_limit": 24,
                "category": "interactive",
                "target_html": """<div class=\"box\"><input id=\"score\" type=\"range\" min=\"0\" max=\"100\" value=\"50\"/><h2 id=\"value\">50%</h2></div>""",
                "target_css": """body{margin:0;min-height:100vh;display:grid;place-items:center;background:transparent;font-family:Inter,sans-serif;color:#f8fafc;}\n.box{width:340px;background:#0f172a;border:1px solid #1e293b;border-radius:14px;padding:16px;}input{width:100%;}\nh2{margin:12px 0 0;text-align:center;color:#facc15;}h2.good{color:#22c55e;}h2.warn{color:#facc15;}h2.bad{color:#ef4444;}""",
                "target_js": """const slider=document.getElementById('score');
const value=document.getElementById('value');
function paint(){
  const n=Number(slider.value);
  value.textContent=`${n}%`;
  value.className=n>=75?'good':(n>=40?'warn':'bad');
}
slider.addEventListener('input', paint);
paint();""",
            },
        ]

        for payload in challenges:
            challenge = Challenge.objects.create(**payload)
            self.stdout.write(self.style.SUCCESS(f"Created {challenge.title}"))
