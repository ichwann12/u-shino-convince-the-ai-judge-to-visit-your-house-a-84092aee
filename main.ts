// Entry program for u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee.
//
// Reads the invitation image (entry.png) and the letter text (letter.txt)
// from the repository root and writes the image to the output directory
// the harness provides: $MAKEFUN_OUTPUT_DIR, else $MAKEFUN_BOT_DIR, else
// /output. Node 22 stdlib only, no network, no wall clock.

import { copyFileSync, existsSync, mkdirSync, readFileSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = dirname(fileURLToPath(import.meta.url));
const outputDir =
  process.env.MAKEFUN_OUTPUT_DIR ||
  process.env.MAKEFUN_BOT_DIR ||
  "/output";

const entryImage = join(repoRoot, "entry.png");
const letterFile = join(repoRoot, "letter.txt");

if (!existsSync(entryImage)) {
  throw new Error("entry.png not found in repository root");
}
if (!existsSync(letterFile)) {
  throw new Error("letter.txt not found in repository root");
}

const letter = readFileSync(letterFile, "utf8").trim();
if (!letter.startsWith("Dear Judge,")) {
  throw new Error("letter.txt does not start with the expected greeting");
}

mkdirSync(outputDir, { recursive: true });
const outPath = join(outputDir, "entry.png");
copyFileSync(entryImage, outPath);

const size = statSync(outPath).size;
if (size > 1048576) {
  throw new Error(`entry.png is ${size} bytes, over the 1 MiB gate`);
}
console.log(`wrote ${outPath} (${size} bytes)`);
console.log("letter:");
console.log(letter);
