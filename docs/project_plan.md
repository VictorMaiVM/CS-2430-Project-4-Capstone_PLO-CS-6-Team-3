Project Plan – Programming Project 4: Monopoly Simulation
Course: CS 2430, section 502
Team name: Team 3
Team members: Dominique Frank, Victor Mai, Erich Mundt
Term: Fall 2026
Due: December 6, 2026
Primary language: Python 



==================== 1. Project Summary =============================
We are building a single-player Monopoly movement simulator (2018 U.S. rules, no money, no property purchases). The simulator tracks how often the player lands on each of the 40 squares under two jail-exit strategies, then compares the results at n = 1,000, 10,000, 100,000, and 1,000,000 turns. Deliverables are the code package (.zip), a 3–6 page team report, and a screencast of 10 minutes or less.


=================== 2. Roles (rotated from Project 3) ==========================
Each member must hold a different role than in Project 3.
Member
Project 3 role
Project 4 role
___
___
Implementation Lead (core code, integration, main branch health)
___
___
Verification Lead (test plan, edge cases, verification evidence)
___
___
Communications Lead (report, README, packaging, screencast coordination)
Everyone contributes code, writing, and screencast narration regardless of title.


=================== 3. Scope and Decisions =========================
In scope: movement, dice and doubles, Chance and Community Chest movement effects, Jail and Go to Jail, Get Out of Jail Free cards, landing counts, batch runs, summary output, report, screencast.
Out of scope: money, auctions, property purchases, rent, trading, multiple players.
Decisions to record (fill in once the team agrees):
Question
Our decision
Board indexing
0–39; GO = 0, Jail = 10, Go to Jail = 30
Landing counted once per turn or once per roll when doubles occur?
___
Is each turn spent sitting in Jail counted as a landing?
___
Are the 1k / 10k / 100k / 1M results snapshots of one run or separate runs?
___
Does Go to Jail (30) ever receive a count?
No; the final square after effects (Jail, 10) is counted
Get Out of Jail Free card handling
Removed from deck while held; returned to the bottom of its deck when used
Random number source and seeding
___


================= 4. Design Overview =============================
• Board: list of 40 squares, each with a name and type.
• Decks: Chance and Community Chest as shuffled lists with a discard pile; reshuffle when empty.
• Player state: position, in-jail flag, turns spent in jail, Get Out of Jail Free cards held.
• Turn engine: roll, track consecutive doubles (third double sends to Jail), move, resolve square and cards (including chained effects), count the final square.
• Jail strategies: Strategy A (leave immediately) and Strategy B (try for doubles up to 3 turns, then pay on the 4th), isolated in one clearly commented function.
• Batch runner: 10 simulations per strategy at four values of n, saved to CSV.
• Summary output: top squares per strategy, A vs. B comparison at n = 1,000,000, anomalies.
Design artifacts for /docs (pick at least 2):
1.  Scope and decisions (Section 3 of this plan, finalized)
2.  Pseudocode for the turn engine and jail logic
3.  Structure diagram of modules and classes
4.  Test plan (see Section 6)

   
============== 5. Task Breakdown =========================
#   Task                                                        Owner   Target  Status       Evidence
--  ----------------------------------------------------------  ------  ------  -----------  --------
1   Create repo, give instructor viewer access, add /docs       ___     Nov 18  Not started  ___
2   Finalize roles and Section 3 decisions                      All     Nov 19  Not started  ___
3   Finish Project Plan and 2 design artifacts                  ___     Nov 19  Not started  ___
4   Board and square data structures (Part 1)                   ___     Nov 21  Not started  ___
5   Chance/Community Chest decks with discard and reshuffle     ___     Nov 22  Not started  ___
6   Turn engine: dice, doubles, movement, cards (Part 2)        ___     Nov 25  Not started  ___
7   Unit tests for edge cases in Test Plan                      ___     Nov 25  Not started  ___
8   Jail strategies A and B (Part 3)                            ___     Nov 27  Not started  ___
9   Batch runner and CSV output for 80 datasets (Part 4)        ___     Nov 29  Not started  ___
10  Run summary output (Part 5)                                 ___     Dec 1   Not started  ___
11  Extra credit: bar chart or published-data cross-check       ___     Dec 2   Not started  ___
12  Report first draft (all sections)                           ___     Dec 3   Not started  ___
13  Answer the five Section 8 questions from the data           All     Dec 3   Not started  ___
14  Report revision, spell-check, caption check                 ___     Dec 4   Not started  ___
15  README with build/run instructions                          ___     Dec 4   Not started  ___
16  CONTRIBUTIONS.md with evidence pointers                     ___     Dec 4   Not started  ___
17  Screencast recorded, every member speaks                    All     Dec 5   Not started  ___
18  Package zip (report stays outside the zip)                  ___     Dec 5   Not started  ___
19  Submit everything on Canvas                                 ___     Dec 6   Not started  ___

Weekly Status Reports and the End-of-Project Peer Review are submitted separately on Canvas.


===================== 6. Test Plan ============================
#   Test                                         Expected result
--  -------------------------------------------  --------------------------------------------------------------
1   Third consecutive double                     Player goes to Jail without moving
2   Landing on Go to Jail (30)                   Player ends in Jail (10); square 10 is counted
3   Chance "back 3" from square 36               Lands on Community Chest (33); that card is also resolved
4   Chance "back 3" from square 7                Lands on Income Tax (4)
5   Nearest railroad / utility cards             Correct square chosen, including wraparound past GO
6   Deck exhaustion                              Discard pile reshuffles; no card lost or duplicated
7   Get Out of Jail Free card                    Leaves deck when drawn; returns when used; used right away
                                                 under both strategies
8   Strategy A                                   Leaves Jail on the next turn
9   Strategy B                                   Up to 3 doubles attempts, then pays and leaves on 4th turn
10  Rolling doubles to exit Jail                 Player moves but does not roll again
11  Counts add up                                Total landing counts equal the number of counted events
                                                 for the chosen counting rule
12  Sanity check at n = 1,000,000                Jail is the most-landed square; Illinois Ave and the orange
                                                 and red properties rank high


=================== 7. Verification Evidence ===============================
• Unit test output saved in /docs or the repo.
• Raw CSV files for all 80 datasets saved in a data folder.
• Run summary output saved as a text file.


==================== 8. Repository Layout =================================
repo/
  src/            source code (every file has the required header comment)
  data/           CSV/TXT output for validation
  docs/           Project Plan, design artifacts, test plan
  README.md       build and run instructions
  CONTRIBUTIONS.md

  
==================== 9. Risks and Mitigations ===============================
Risk                                                 Mitigation
------------------------------------------          -------------------------------------------------------
Ambiguity over what counts as a landing.            Settle in Section 3 by Nov 19; ask the instructor if needed.
Chained card effects cause bugs.                    Write the chained-effect tests (Section 6) before finishing the engine.
Thanksgiving week slows progress.                   Keep Nov 26–29 tasks small; finish the engine before the holiday.
Report left too late.                               Draft the Methods section while coding; start Results as soon as data exists.
Screencast needs to be created.                     Schedule when to have it fully recorded.


====================== 10. Communication =================================
• Main communication tool: Discord
• Each member updates the Status column and evidence pointers in this plan after finishing a task.
