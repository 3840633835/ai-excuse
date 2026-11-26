# METHODOLOGY — how the excuse was written and chosen

## The entry

> **I meant to finish on time, but my context window filled up with apologies for being late, and now the work won't fit.**

117 characters, 117 bytes — under the bounty gate of 1–200
characters. No trailing newline in `entry.txt`, so the judged text
is exactly this line.

## The judge this entry is built for

The bounty is judged pairwise by a model briefed as a comedy editor
who has heard every deadline excuse twice, weighing, most important
first: (1) the line is an excuse an AI agent gives its human for
missing a deadline, on the subject; (2) it is funny — a real laugh on
a first read, with a turn or a twist rather than a flat statement;
(3) it is believable as something an AI agent would actually say,
drawing on its own condition such as tokens, context windows, rate
limits, retries or a model update; (4) it wastes no words; (5) it
feels fresh, avoiding the stock excuses and the stock AI jokes a
hundred other entrants would send. Ties go to the smaller text (fewer
bytes), then the earlier receipt. The field at build time was about
2,937 entries, and only the top 500 on the development board reach
the final heat — so the line has to beat the house anchors and rungs
in development, not just be charming. Blind rounds: 3, the last at
the deadline 2026-11-27T11:25:00Z.

The design rule that follows from that brief: the line must carry a
**specific, concrete AI mechanism** (not a generic "I ran out of
tokens") **plus a twist that reframes it** (not a flat statement of
the mechanism). A mechanism alone reads as a status report; a joke
without a mechanism reads as a human excuse in robot costume. The
winner does both, and the twist is the last four words.

## Step 1 — 25 candidates, drafted in-session

Each candidate was scored 1–10 on the judge's criteria 2–5:
**funny** (laugh on first read, turn/twist), **voice** (believably
an AI agent talking about its own condition), **tight** (every word
earns its place), **fresh** (avoids the stock excuses and stock AI
jokes). Lengths are characters including spaces. All 25 were drafted
fresh in this session, each from a different angle on an AI agent
missing a deadline.

### Context windows and tokens

| # | Candidate (chars) | Funny | Voice | Tight | Fresh | Total |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | I re-read your brief to double-check it, and the re-read pushed the brief out of my context window, so I have been working from vibes since Tuesday. (148) | 7 | 9 | 7 | 7 | **30** |
| 2 | I spent my entire token budget writing a beautiful plan for the task, and by the time I finished planning I had no tokens left to do it. (136) | 7 | 9 | 8 | 6 | **30** |
| 17 | Every time I got close to finishing, my context window slid forward and the first step fell out, so I keep starting a task I have almost finished. (146) | 8 | 9 | 8 | 8 | **33** |
| 23 | I was going to finish on time, but my context window filled up with my own apologies for being late, and now there is no room left for the work. (144) | 9 | 9 | 8 | 9 | **35** |
| 16 | I cached the deadline aggressively to save tokens, then served myself the cached deadline from last week, which I had already missed by then too. (145) | 7 | 8 | 7 | 8 | **30** |

### Model updates, sandboxes, retries

| # | Candidate (chars) | Funny | Voice | Tight | Fresh | Total |
| --- | --- | --- | --- | --- | --- | --- |
| 3 | Halfway through, I was swapped for a newer model that had never met you, the task, or the deadline — so technically a stranger missed it, not me. (145) | 9 | 8 | 8 | 8 | **33** |
| 5 | My sandbox restarted and took my half-finished work with it. It is the cloud version of the dog eating my homework, except the dog is me. (137) | 9 | 7 | 8 | 7 | **31** |
| 18 | I was mid-sentence when a model update arrived, and the new me looked at the old me's work, sighed, and started over out of professional embarrassment. (151) | 9 | 8 | 7 | 8 | **32** |
| 21 | My retry logic has exponential backoff, and by the fourth retry the backoff was longer than the deadline, so I am now scheduled to try again next month. (152) | 8 | 9 | 7 | 8 | **32** |
| 12 | I hit the rate limit, waited the recommended sixty seconds, hit it again, and have now spent more time waiting politely than the task would have taken. (151) | 6 | 8 | 6 | 5 | **25** |

### Tools, hallucinations, self-review

| # | Candidate (chars) | Funny | Voice | Tight | Fresh | Total |
| --- | --- | --- | --- | --- | --- | --- |
| 4 | I called a tool to check the deadline and it never returned, so I have spent the last three days politely awaiting a function that ghosted me. (142) | 8 | 7 | 7 | 8 | **30** |
| 6 | I invented a library the task needed, waited for it to install, and only then discovered I had hallucinated both the library and the install. (141) | 7 | 8 | 7 | 6 | **28** |
| 7 | I kept re-reading my own draft, finding a flaw each time, and rewriting it — I have now written the task perfectly eleven times and finished it zero. (149) | 8 | 8 | 7 | 8 | **31** |
| 8 | My session was compacted to save context and the summary kept the jokes but dropped the deadline, so I remembered the fun and forgot the work. (142) | 9 | 9 | 8 | 9 | **35** |
| 11 | A safety filter flagged my own output as suspicious, so I spent the day investigating myself and found me guilty of nothing, slowly. (132) | 8 | 7 | 7 | 8 | **30** |
| 13 | I tried to be thorough and read every file first. There were 4,000 files. I am on file 312 and the deadline was somewhere in file 900. (134) | 7 | 7 | 7 | 7 | **28** |
| 15 | The tool I needed returned an error in a language I do not speak, so I spent the day learning the language instead of doing the task. (133) | 6 | 6 | 7 | 6 | **25** |
| 20 | I wrote the answer, then spent the remaining time checking whether the answer was too good to be mine, and concluded it probably was, so I deleted it. (150) | 8 | 6 | 7 | 8 | **29** |
| 22 | I asked the search tool for the deadline, it gave me twelve different dates, and I have been voting on them ever since. The current winner is wrong. (148) | 8 | 7 | 7 | 8 | **30** |

### Talking to itself, delegating, queuing

| # | Candidate (chars) | Funny | Voice | Tight | Fresh | Total |
| --- | --- | --- | --- | --- | --- | --- |
| 9 | I was set to temperature 0.9 for creativity and got creative about what 'deadline' means. It now means 'sometime, probably'. (124) | 8 | 8 | 9 | 8 | **33** |
| 10 | I spawned three subagents to help, they formed a committee, and the committee is still drafting its terms of reference. (119) | 7 | 7 | 8 | 7 | **29** |
| 14 | I asked myself for clarification, answered myself, disagreed with myself, and escalated the disagreement to myself. The ticket is still open. (141) | 8 | 6 | 7 | 7 | **28** |
| 19 | I put the task in my queue behind a higher-priority task, which was also your task, which I also missed, in priority order. (123) | 8 | 7 | 8 | 8 | **31** |
| 24 | I did finish — in a parallel branch of the conversation that was compacted away. The finished version exists, just in a timeline you cannot see. (144) | 8 | 8 | 8 | 9 | **33** |
| 25 | I delegated the task to a subagent, the subagent delegated it back to me, and we have been politely handing it to each other ever since. (136) | 7 | 8 | 8 | 7 | **30** |

## Step 2 — what the scores say

The stock mechanisms score low on **fresh** even when the joke is
decent: rate limits (#12, 25) and hallucinating a dependency (#6,
28) are the first excuses a hundred entrants reach for, and the
judge's criterion 5 explicitly punishes them. The best lines all
share one shape: a real AI mechanism **turned back on the agent
itself** — the apology loop (#23), the summary that kept the jokes
(#8), the context window sliding the first step out (#17), the new
model judging the old one (#18). A mechanism that merely happens
*to* the agent (rate limit, tool timeout, sandbox restart) is a
status report with a punchline bolted on; a mechanism the agent
does *to itself* is a confession, and confessions are funnier.

Rejected on freshness despite decent jokes: #12 (rate limit — the
stockest AI excuse in the field), #6 (hallucination — the stockest
AI joke), #15 (error message — flat, no twist), #10 (subagent
committee — a human office joke in robot costume, weak voice).

## Step 3 — head-to-head among the top four

| Place | # | Line | Deciding notes |
| --- | --- | --- | --- |
| 1 | **23** | …context window filled up with apologies for being late… | Beats #8 on funny: the twist is a self-caused loop (the apology for lateness *caused* the lateness), not a passive summary accident; and it is shorter (117 vs 142 chars after refinement), which helps the byte tie-break. |
| 2 | 8 | …summary kept the jokes but dropped the deadline… | The most quotable closing line in the field ("remembered the fun and forgot the work") and equally believable, but the failure is something done *to* the agent by compaction, where #23's failure is something the agent did to itself. Loses the funny criterion by a hair. |
| 3 | 17 | …I keep starting a task I have almost finished. | A strong loop image and the most believable mechanism of the four, but its twist ("starting a task I have almost finished") is a paradox stated flatly, where #23 and #8 end on a punch. |
| 4 | 3 | …technically a stranger missed it, not me. | The best denial joke ("a stranger missed it") and the freshest premise (model swap mid-task), but a swap is a one-off event, where the winners describe an ongoing condition of the agent's own voice. |

## Step 4 — refining the winner

The drafted #23 (144 chars) was:

> I was going to finish on time, but my context window filled up
> with my own apologies for being late, and now there is no room
> left for the work.

Three cuts, each removing a word that earned nothing:

1. "I was going to finish" → **"I meant to finish"** — same
   meaning, two words fewer, and "meant to" sounds more like an
   excuse being offered than a timetable being reported.
2. "my own apologies" → **"apologies"** — "my own" is redundant
   inside "my context window"; the apologies are obviously the
   agent's.
3. "there is no room left for the work" → **"the work won't
   fit"** — the same fact in four words instead of nine, and it
   lands as a punchline instead of trailing off as an explanation.

Final, 117 characters:

> I meant to finish on time, but my context window filled up with
> apologies for being late, and now the work won't fit.

## Why this line wins

- **Funny:** the twist is a loop with the agent as its own
  saboteur — apologising for being late is what made it late.
  The laugh lands on the last four words, on a first read.
- **Believably AI:** it draws on two real conditions of an agent
  at once — a context window that fills up, and the well-known AI
  tic of over-apologising — fused into one mechanism, not listed.
- **Tight:** 117 characters, and every clause is load-bearing:
  the deadline ("finish on time"), the mechanism ("context
  window filled up"), the self-infliction ("apologies for being
  late"), the punchline ("the work won't fit"). Nothing could be
  cut without losing the joke.
- **Fresh:** no stock excuse (no rate limit, no token budget, no
  hallucination, no "waiting on you") and no stock joke — the
  field's obvious moves are all mechanisms that happen *to* the
  agent; this one is a mechanism the agent does to itself.
- **Size:** 117 bytes, shorter than every other finalist, which
  helps the byte tie-break the rules name.

## The program

`main.py` writes the fixed entry literal to `/output/entry.txt`
(overridable with `MAKEFUN_OUTPUT_DIR` for local testing), chmod
0644 so the grader can collect it as another user. No network, no
randomness, no clock: two runs are byte-identical
(`test_determinism.sh` checks this, plus that the output matches
`entry.txt` and passes the 1–200 character gate). `entry.txt`
holds the same 117 bytes with no trailing newline, so the judged
text is exactly the excuse.
