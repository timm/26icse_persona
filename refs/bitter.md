
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>You're Being Promoted, Not Replaced · Tim Menzies</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <div class="link-bar">
    <span class="side">
      <a href="index.html" aria-label="home"><i class="fa-solid fa-house"></i></a>
      <span class="sep">|</span>
      <a href="mailto:timm@ieee.org"><i class="fa-solid fa-envelope"></i>timm@ieee.org</a>
      <span class="sep">|</span>
      <a href="tel:+13043762859"><i class="fa-solid fa-phone"></i>+1-304-376-2859</a>
    </span>
    <span class="side">
      <a href="https://scholar.google.com/citations?user=7htTUTgmLtUC"><img class="glyph" src="https://cdn.simpleicons.org/googlescholar/FFB86C" alt="">papers</a>
      <span class="sep">|</span>
      <a href="https://arxiv.org/search/?searchtype=all&amp;query=tim+menzies"><img class="glyph" src="https://cdn.simpleicons.org/arxiv/FFB86C" alt="">pre-prints</a>
    </span>
  </div>

  <a href="index.html"><img src="banner.png" alt="Tim Menzies" class="banner"></a>

  <div class="kicker">Apr 2026 · 5-minute talk · SE audience</div>
  <h2 style="margin-top:0.3rem;">You're Being Promoted, Not Replaced<span class="cursor">▌</span></h2>

  <article>
    <h3>The Sutton Highway vs the "higher way"</h3>
    <p>Rich Sutton, 2019. <em>The Bitter Lesson.</em> Sixty years of evidence: brute-force compute beats human-engineered knowledge. Chess heuristics? Scale won. Edge detectors? Scale won. Phoneme models? Scale won.</p>
    <p>His conclusion: stop baking your intelligence into the system. Just assume you can scale using tomorrow's CPU.</p>
    <div class="callout warn">
      So now your manager wants: <strong>Inception → LLM → Code.</strong><br>
      One invisible leap. Ship it.
    </div>
    <p>But there is a problem: SE isn't chess.</p>
  </article>

  <article>
    <h3>SE Isn't Chess</h3>
    <p>Every one of Sutton's examples shares a quiet assumption: <strong>you can assess the "What" the moment it's created.</strong> Move 47 — good or bad? Instant feedback.</p>
    <p>Reliability? Measured eighteen months into prod. Maintainability? Ask whoever inherits the LLM-slop in 2027. Understandability? Good luck explaining it to the regulator at 2am.</p>
    <p><cite>Brooks 1976</cite> knew this. The V-diagram isn't just testing — it's epistemology. After project <em>i</em>, you carry domain knowledge into project <em>i+1</em>. The code is not the artifact. <strong>What you learned building it</strong> is the artifact.</p>
    <p><cite>Swartout 1983</cite>, XPLAIN system. Blunt finding: jump straight to code and you lose the <em>Why.</em> The domain principles that drove the refinement — gone. The system can't justify itself. Forty years later, trillion parameters, same problem.</p>
  </article>

  <article>
    <h3>The MSR'26 Hangover</h3>
    <p>This isn't theory. Look at the posters. Pattern after pattern:</p>
    <div class="callout warn">
      <strong>Productivity spike. Then collapse.</strong><br>
      Dev time up. Code quality down. Technical debt accumulating
      in a latent space nobody can read.
    </div>
    <p>The sugar high Sutton's highway promises — followed by a maintenance crisis that lands, as always, on <em>you.</em></p>
    <p>Predicted outcome. Not a bug.</p>
  </article>

  <article>
    <h3>The Higher Way</h3>
    <p>Not rejection of AI. <em>Elevation</em> of the engineer.</p>
    <div class="callout">
      <strong>Inception → Domain Models → Code</strong>
    </div>
    <p>Domain models are the intermediaries. Markdown skill files. DSLs that describe the <em>why</em> in fifty lines instead of fifty thousand. Post-conditions from specs. Fuzzing mutators carried forward from prior projects. Symbolic. Browsable. A human can challenge them.</p>
    <p><cite>Lethbridge</cite>: compact symbolic models actively <em>improve</em> LLM performance — less hallucination, tighter reasoning. <cite>Pugh</cite>: these models are where you define experiments. Does X beat Y? Now you have a testbed instead of a prayer.</p>
  </article>

  <div class="punchline">
    <p>The Bitter Lesson is for games.<br>The Higher Way is for Software Engineering.</p>
    <p style="margin-top:0.8rem; font-style:normal;">
      The LLM is a fast typist.<br>
      You're the one who knows <strong>what's worth typing.</strong>
    </p>
    <div class="tagline-final">That's not replacement. That's a promotion.</div>
  </div>

</body>
</html>
