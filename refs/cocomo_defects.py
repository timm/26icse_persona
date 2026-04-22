#!/usr/bin/env python3 -B
# cocomo_defects.py — cocomo.py style + COQUALMO defect model.
#
# TODO:ranges — see ../todo.md §1–§6. Slope ranges and the scale-factor form
# are provisional. Resolve before final experiments.
#
# Structural notes (full write-up belongs in a model-math.tex later):
#   effort  = a · kloc^(b + 0.01·ΣSF) · ΠEM                    (XOMO 2006, Eq 1)
#   defects = Σ_{phase} baseRate_phase · kloc · ΠintroFactor_phase
#                                           · Π(1 − removeFactor_phase)
#   intro factor form  : m·(x−3) + 1                           (sawtooth, Eq 5)
#   remove factor form : m·(x−1)                               (sawtooth, Eq 18)
#   base rates         : reqs=10, design=20, code=30  per KSLOC
#   risk               : additive normalized penalty from pairwise tables
#                        (simplification of XOMO 2006 Fig 4 multiplicative form;
#                         TODO:ranges §4)

from random import uniform, seed

#--- dsl code (must precede module-level uses of `o`)
class o(dict):
  __getattr__ = dict.get
  __setattr__ = dict.__setitem__
  def __repr__(self):
    isa = isinstance
    def say(v):
      if isa(v, float): return f"{v:,.2f}".rstrip('0').rstrip('.')
      if isa(v, dict):  return o(v)
      if isa(v, (list, tuple)): return ', '.join(say(x) for x in v)
      return str(v)
    return "{" + " ".join(f":{k} {say(v)}"
                          for k, v in sorted(self.items())) + "}"

def from_(lo, hi): return uniform(lo, hi)
def within(x, lo, hi): return max(lo, min(hi, x))
def int_(x): return int(x+0.5)

def has(ako, lo=1, hi=5): return o(ako=ako, lo=lo, hi=hi)

def coc2():
  p, n, s = "+", "-", "*"
  d = "dr"  # defect remover: aa, etat, pr (1..6)
  return o(
    Acap=has(n),       Aexp=has(n),       Pcap=has(n),
    Pcon=has(n),       Plex=has(n),       Ltex=has(n),
    Tool=has(n),       Sced=has(n),       Rely=has(p),
    Docu=has(p),       Cplx=has(p, 1, 6),
    Prec=has(s, 1, 6), Flex=has(s, 1, 6), Arch=has(s, 1, 6),
    Team=has(s, 1, 6), Pmat=has(s, 1, 6),
    Site=has(n, 1, 6), Data=has(p, 2, 5), Pvol=has(p, 2, 5),
    Ruse=has(p, 2, 6), Time=has(p, 3, 6), Stor=has(p, 3, 6),
    # Defect removers
    Aa=has(d, 1, 6), Etat=has(d, 1, 6), Pr=has(d, 1, 6),
    KLOC       = has("=", 2, 2000),
    KLOC_times = has("=", 1, 100)
  )

def policies(): return o(
  Noop     = proj(coc2(), o()),
  Arch     = proj(coc2(), o(Arch=5)),
  MoreTime = proj(coc2(), o(Sced=5)),
  MoreProc = proj(coc2(), o(Pmat=5)),
  Team     = proj(coc2(), o(Team=5)),
  Prec     = proj(coc2(), o(Prec=5, Flex=5)),
  DoLess   = proj(coc2(), o(Data=2, KLOC_times=50)),
  LoQual   = proj(coc2(), o(Rely=1, Docu=1, Time=3, Cplx=1)),
  Tools    = proj(coc2(), o(Time=3, Stor=3, Pvol=2, Tool=5, Site=6)),
  Pers     = proj(coc2(), o(Acap=5, Pcap=5, Pcon=5, Aexp=5, Plex=5,
                            Ltex=5)),
  # Defect-focused policies
  PeerRev  = proj(coc2(), o(Pr=6)),
  AutoAn   = proj(coc2(), o(Aa=6)),
  ExecTest = proj(coc2(), o(Etat=6)),
)

def projects(): return o(
  OSP = proj(coc2(), o(
    KLOC=(75, 125),   KLOC_times=100,
    Prec=(1, 2),      Flex=(2, 5),    Arch=(1, 3),    Team=(2, 3),
    Pmat=(1, 4),      Stor=(3, 5),    Ruse=(2, 4),    Docu=(2, 4),
    Cplx=(5, 6),      Data=3,         Pvol=2,         Rely=5,
    Acap=(2, 3),      Pcon=(2, 3),    Aexp=(2, 3),    Ltex=(2, 4),
    Tool=(2, 3),      Sced=(1, 3),    Pcap=3,         Plex=3,
    Site=3
  )),
  OSP2 = proj(coc2(), o(
    KLOC=(75, 125),   KLOC_times=100,
    Prec=(3, 5),      Pmat=(4, 5),    Flex=3,         Arch=4,
    Team=3,           Docu=(3, 4),    Ltex=(2, 5),    Sced=(2, 4),
    Time=3,           Stor=3,         Data=4,         Pvol=3,
    Ruse=4,           Rely=5,         Cplx=4,         Acap=4,
    Pcap=3,           Pcon=3,         Aexp=4,         Plex=4,
    Tool=5,           Site=6
  )),
  JPL_Flight = proj(coc2(), o(
    KLOC=(7, 418),    KLOC_times=100,
    Pmat=(2, 3),      Rely=(3, 5),    Data=(2, 3),    Cplx=(3, 6),
    Time=(3, 4),      Stor=(3, 4),    Acap=(3, 5),    Aexp=(2, 5),
    Pcap=(3, 5),      Plex=(1, 4),    Ltex=(1, 4),    Tool=2,
    Sced=3
  )),
  JPL_Ground = proj(coc2(), o(
    KLOC=(11, 392),   KLOC_times=100,
    Pmat=(2, 3),      Rely=(1, 4),    Data=(2, 3),    Cplx=(1, 4),
    Time=(3, 4),      Stor=(3, 4),    Acap=(3, 5),    Aexp=(2, 5),
    Pcap=(3, 5),      Plex=(1, 4),    Ltex=(1, 4),    Tool=2,
    Sced=3
  ))
)

#-- COQUALMO sign tables (TODO:ranges §5, §6; verify vs sawtooth paper)
# Attributes whose increase REDUCES introduced defects at that phase.
DEFECT_NEG = o(
  reqs   = "Pmat Prec Arch Team Acap Aexp Docu Ltex Pcon Plex "
           "Rely Sced Site Tool".split(),
  design = "Pmat Prec Arch Team Acap Aexp Docu Ltex Pcon Plex "
           "Rely Sced Site Tool Pcap".split(),
  code   = "Pmat Prec Arch Team Acap Aexp Docu Ltex Pcon Plex "
           "Rely Sced Site Tool Pcap".split(),
)
# Attributes whose increase ADDS introduced defects at that phase.
DEFECT_POS = o(
  reqs   = "Cplx Data Pvol Ruse Stor Time".split(),
  design = "Cplx Data Pvol Ruse Stor Time".split(),
  code   = "Cplx Data Pvol Ruse Stor Time".split(),
)

_ = 0

ne = [[_,_,_,1,2,4],[_,_,_,_,1,2],[_,_,_,_,_,1],
      [_,_,_,_,_,_],[_,_,_,_,_,_],[_,_,_,_,_,_]]
ne86 = [[_,_,1,2,4,8],[_,_,_,1,2,4],[_,_,_,_,1,2],
        [_,_,_,_,_,1],[_,_,_,_,_,_],[_,_,_,_,_,_]]
nw = [[4,2,1,_,_,_],[2,1,_,_,_,_],[1,_,_,_,_,_],
      [_,_,_,_,_,_],[_,_,_,_,_,_],[_,_,_,_,_,_]]
nw8 = [[8,4,2,1,_,_],[4,2,1,_,_,_],[2,1,_,_,_,_],
       [1,_,_,_,_,_],[_,_,_,_,_,_],[_,_,_,_,_,_]]
sw = [[_,_,_,_,_,_],[1,_,_,_,_,_],[2,1,_,_,_,_],
      [4,2,1,_,_,_],[_,_,_,_,_,_],[_,_,_,_,_,_]]
sw8 = [[_,_,_,_,_,_],[1,_,_,_,_,_],[2,1,_,_,_,_],
       [4,2,1,_,_,_],[8,4,2,1,_,_],[_,_,_,_,_,_]]
sw26 = [[_,_,_,_,_,_],[_,_,_,_,_,_],[1,_,_,_,_,_],
        [2,1,_,_,_,_],[4,2,1,_,_,_],[_,_,_,_,_,_]]
sw86 = [[_,_,_,_,_,_],[1,_,_,_,_,_],[2,1,_,_,_,_],
        [4,2,1,_,_,_],[8,4,2,1,_,_],[_,_,_,_,_,_]]

def risks(): return o(
  Ltex=o(Pcap=nw8),
  Pvol=o(Plex=sw),
  Pmat=o(Acap=nw, Pcap=sw86),
  Ruse=o(Aexp=sw86, Ltex=sw86),
  Stor=o(Acap=sw86, Pcap=sw86),
  Cplx=o(Acap=sw86, Pcap=sw86, Tool=sw86),
  Rely=o(Acap=sw8, Pcap=sw8, Pmat=sw8),
  Team=o(Aexp=nw, Sced=nw, Site=nw),
  Time=o(Acap=sw86, Pcap=sw86, Tool=sw26),
  Tool=o(Acap=nw, Pcap=nw, Pmat=nw),
  Sced=o(
    Cplx=ne86, Time=ne86, Pcap=nw8, Aexp=nw8, Acap=nw8,
    Plex=nw8, Ltex=nw, Pmat=nw, Rely=ne, Pvol=ne, Tool=nw
  )
)

def proj(b4, also):
  def check(k, v):
    if isinstance(v, o): lo, hi = v.lo, v.hi
    elif isinstance(v, (list, tuple)): lo, hi = v[0], v[1]
    else: lo, hi = v, v
    if k not in b4:
      if k in ["KLOC", "KLOC_times"]: return has("=", lo, hi)
      raise ValueError(f"Unknown key: {k}")
    p = b4[k]
    return has(p.ako, within(lo, p.lo, p.hi), within(hi, p.lo, p.hi))
  return o(b4 | {k: check(k, v) for k, v in also.items()})

#-- cocomo logic

# TODO:ranges §1 — EM slope ranges. Provisional: widest union of cocomo.py,
# xomo.py, sawtooth-2009. EM+ ∈ [0.055, 0.21]; EM- ∈ [−0.187, −0.075].
# TODO:ranges §2 — SF form. Provisional: sawtooth additive linear
# m·(z−6) with m ∈ [−1.56, −1.014].
def emsf(sign, z):
  if sign == "+": return 1.0 + (z-3) * from_(0.055, 0.21)
  if sign == "-": return 1.0 + (z-3) * from_(-0.187, -0.075)
  if sign == "*": return (z-6) * from_(-1.56, -1.014)
  if sign == "dr": return z  # defect-remover raw setting; slopes applied in defects()
  return 0

def effort(coc, y):
  em, sf = 1.0, 0.0
  for k, t in coc.items():
    if k in ["KLOC", "KLOC_times"]: continue
    v = y[k]
    if t.ako in ("+", "-"): em *= v
    elif t.ako == "*":      sf += v
  return y.a * (y.kloc ** (y.b + 0.01*sf)) * em

# TODO:ranges §3 — COQUALMO slopes. Using xomo.py's wider ranges per
# user directive "widest always".
_INTRO_SLOPE = o(
  reqs   = o(pos=(0.0166, 0.38),  neg=(-0.215, -0.035)),
  design = o(pos=(0.0066, 0.145), neg=(-0.325, -0.05)),
  code   = o(pos=(0.0066, 0.145), neg=(-0.29, -0.05)),
)
_REMOVE_SLOPE = o(
  reqs   = (0.0, 0.14),
  design = (0.0, 0.156),
  code   = (0.1, 0.176),
)
_BASE_RATE = o(reqs=10, design=20, code=30)  # defects / KSLOC

def _sample_defect_slopes():
  """Draw one slope per (phase, role) once per cocoon run (pivot style)."""
  s = o(intro=o(), remove=o())
  for ph in ("reqs", "design", "code"):
    s.intro[ph] = o(
      pos = from_(*_INTRO_SLOPE[ph].pos),
      neg = from_(*_INTRO_SLOPE[ph].neg),
    )
    s.remove[ph] = from_(*_REMOVE_SLOPE[ph])
  return s

def defects(x, slopes):
  """Total residual defects across reqs + design + code."""
  total = 0.0
  kloc = x.KLOC * x.get("KLOC_times", 100) / 100
  for ph in ("reqs", "design", "code"):
    intro_factor = 1.0
    for attr in DEFECT_POS[ph]:
      intro_factor *= slopes.intro[ph].pos * (x[attr] - 3) + 1
    for attr in DEFECT_NEG[ph]:
      intro_factor *= slopes.intro[ph].neg * (x[attr] - 3) + 1
    introduced = _BASE_RATE[ph] * kloc * intro_factor
    # removal: product of (1 − m·(x−1)) across the three removers
    kept = 1.0
    for rem in ("Aa", "Etat", "Pr"):
      if rem in x:
        kept *= 1 - slopes.remove[ph] * (x[rem] - 1)
    total += introduced * max(0.0, kept)
  return total

def cocoon(proj, risk):
  x, y = o(), o()
  for k, t in proj.items():
    x[k] = int_(from_(t.lo, t.hi))
    y[k] = emsf(t.ako, x[k])
  y.a = from_(2.3, 9.18)
  y.b = ((0.85 - 1.1) / (9.18 - 2.3)) * (y.a - 2.3) + 1.1
  y.kloc = x.KLOC * x.get("KLOC_times", 100)/100
  y.effort = effort(proj, y)
  # TODO:ranges §4 — additive risk (simplification of XOMO 2006 Fig 4).
  y.risk = 100*sum(risk[a][b][x[a]-1][x[b]-1]
                   for a in risk for b in risk[a]
                   if risk[a][b][x[a]-1][x[b]-1]) / 216
  slopes = _sample_defect_slopes()
  y.defects = defects(x, slopes)
  return o(x=x, y=y)

def checks():
  import statistics
  def median(lst): return statistics.median(lst)
  seed(1)
  no_policy = policies().Noop
  jpl = projects().JPL_Ground

  def median_of(pol, pro, key):
    return median([getattr(cocoon(proj(pol, pro), risks()).y, key)
                   for _ in range(50)])

  print("--- RUNNING CHECKS ---")
  do_less = median_of(policies().DoLess, jpl, "effort")
  noop = median_of(no_policy, jpl, "effort")
  print(f"01. DoLess<Noop effort : {do_less < noop} "
        f"({do_less:,.0f} vs {noop:,.0f})")

  pers = median_of(policies().Pers, jpl, "effort")
  print(f"02. Pers<Noop effort   : {pers < noop} "
        f"({pers:,.0f} vs {noop:,.0f})")

  pr = median_of(policies().PeerRev, jpl, "defects")
  d0 = median_of(no_policy, jpl, "defects")
  print(f"03. PeerRev<Noop defects: {pr < d0} "
        f"({pr:,.0f} vs {d0:,.0f})")

  aa = median_of(policies().AutoAn, jpl, "defects")
  print(f"04. AutoAn<Noop defects : {aa < d0} "
        f"({aa:,.0f} vs {d0:,.0f})")

  risky = [cocoon(proj(no_policy, jpl), risks()).y.risk
           for _ in range(100)]
  print(f"05. Risk ∈ [0,100]     : "
        f"{min(risky) >= 0 and max(risky) <= 100}")

  defs = [cocoon(proj(no_policy, jpl), risks()).y.defects
          for _ in range(100)]
  print(f"06. Defects ≥ 0        : {min(defs) >= 0}")

  seed(42)
  v1 = cocoon(proj(no_policy, jpl), risks()).y
  seed(42)
  v2 = cocoon(proj(no_policy, jpl), risks()).y
  print(f"07. Seed reproducible  : "
        f"{v1.effort == v2.effort and v1.defects == v2.defects}")

def sample():
  seed(1)
  for k1, pro in projects().items():
    print("\n" + k1)
    for k2, pol in policies().items():
      tmp = [cocoon(proj(pol, pro), risks()).y for _ in range(10)]
      print(f"  {k2}")
      print("    ", o(effort =sorted(int(z.effort)  for z in tmp)))
      print("    ", o(risk   =sorted(int(z.risk)    for z in tmp)))
      print("    ", o(defects=sorted(int(z.defects) for z in tmp)))

if __name__ == "__main__":
  checks()
  sample()
