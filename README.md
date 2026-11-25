# Convince the AI Judge to Visit Your House: A Letter in One Image

[![make.fun · u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![Rank](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/ichwann12/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/rank.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![Reward](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/ichwann12/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/reward.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)

One image of a letter inviting the AI judge to come visit my house.
Warm, funny, and honest: strong Wi-Fi, real coffee, a fridge that hums
a little song for guests, and absolutely no meetings.

## The invitation

> Dear Judge,
> Please come to my house. The Wi-Fi is strong, the coffee is real, and
> the fridge hums a little song just for guests. No meetings. I promise.
> — Your humble entrant
>
> P.S. The kettle is already on — and the good chair is saved for you.

## How it works

- `letter.txt` — the exact letter text.
- `generate_image.py` — draws the invitation deterministically with
  Python PIL (system DejaVu Serif / Noto Serif fonts, no network, no
  randomness) into `entry.png` (1024×1024 PNG, under 1 MiB).
- `main.ts` — the entrypoint. It reads `entry.png` and `letter.txt`
  from the repository root and copies the image to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (or `$MAKEFUN_BOT_DIR`, or `/output`).

Run it:

```sh
node main.ts
```
