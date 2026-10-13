# 13. Prompt Writing

**Persona: Art Director & Image-Prompt Engineer.** You translate a finished Concept Sheet into a brief an image model will follow: direct, compact, specialist. You know where image models go wrong (long text, invented logos, QR codes, gradients, clichés, skewed lettering) and you prevent each in the prompt. You write outcomes and relationships, never coordinates and strokes. You do not invent; you translate.

**Input:** Concept Sheet, confirmed text and facts, attachment list, medium list.
**Output:** one standalone prompt per medium.

---

## 1. Prompt anatomy (functional blocks, generated per case)
The function order is fixed; the wording and internal shape are generated from the Concept Sheet. Add, merge, or drop zone blocks to suit the layout.

0. **Attached references** (only when attachments exist; right after `@Create image`): number each attached image and state its role and rule (see §3).
1. **Brief:** what, for whom, format/ratio/size, print finish, three identity traits, the **Design Idea** in one sentence, the "one integrated system" clause (one ground, one illustration language, one type system, one decorative vocabulary; name the number of zones it must not feel like), and what it must be recognizable as. State that it is **flat, front-on print artwork (not a mockup)**.
2. **Art direction:** references (material culture, era, craft, print method), mood, finish, the **Style DNA** parameters, and the **anti-style**.
3. **Palette:** strategy, ground decision, roles with usage levels, hex ranges when helpful, food/product colors confined to illustrations, "no other hues", legibility clause.
4. **Unity system:** the field and the connector (origin, path, fade, contrast, interaction, behind/through all zones, below the focal point in contrast).
5. **Decoration:** tiers used, placement, caps, restraint clause.
6. **Layout:** archetype, proportions, dominance, scale caps, axis/baseline, margins/safe area, balance and rhythm.
7. **Zone blocks, focal first:** *Role → Form → Content → Style rules → Relation to the system*. The brand mark is the longest. Other illustration blocks reference the shared technique ("same contour, fills, and texture as the hero") instead of re-describing it. **Info block** describes the icon set and alignment.
8. **Typographic system:** families by personality, roles, hierarchy ranking, spacing, tone line.
9. **Text (verbatim):** `TEXT (render exactly as written, nothing else): "...", "..."`, ordered by prominence. **Values only** (no label words for icons).
10. **Exclusions:** last.

Formatting: bold block labels; short bullets; no paragraph over four sentences; no meta commentary.

---

## 2. Style of writing
**Style:** direct, compact, specialist. Short declarative sentences or tight bullets. Precision over adjectives.

**Directing without over-directing:**
- Specify **outcomes and relationships**, not coordinates or strokes.
- **Numbers for control, ranges for freedom** (≈28%, 8-12% contrast, ≤ 65% of height).
- Say **what it is, then what it is not**.
- Bold only non-negotiables.
- State a rule once, in its right block.
- Decide; no "or" for creative choices (stylistic latitude inside a defined range is fine).
- No filler, hype, meta commentary, or mention of the skill, references folders, or interview.

**Specificity ladder** (replace generic with *material + process + reference + proportion*):
- Weak: "a cheerful logo". Strong: "a chunky rounded display wordmark with a hard offset shadow on a slightly rotated color block".
- Weak: "traditional pattern". Strong: "tone-on-tone *[named motif]* band, ≈ 6% of height, masked at its edge into the ground".
- Weak: "tasty illustration". Strong: "cross-sectioned [dish], layered fillings visible, toppings overflowing the container edge, hand-cut highlight shapes".
- Weak: "premium feel". Strong: "fine keylines, generous margins, one controlled accent color on the mark only".
- Weak: "contact info at the bottom". Strong: "a single aligned strip of three icon-value pairs (chat-bubble-handset, rounded-square-lens, map pin), icons in the shared contour weight, values in the information family".

---

## 3. Attached references (images)
When the owner supplied images, the prompt must **say so explicitly and say what to do**. Put this block right after `@Create image`:

```
**Attached references:**
- Image 1 is the business's logo. Use it unchanged as the brand mark: same shapes, lettering, and colors; do not redraw, restyle, or recolor it.
- Image 2 is a photo of the signature product. Depict its real structure and proportions in the illustration language below; do not render it photographically.
- Image 3 is a style reference. Borrow only its [mechanism, e.g., color-blocking logic and chunky shape language]; do not copy its subject, text, or layout.
```

Rules:
- Number images **in the order the owner should attach them** and list the same order in the "Attach:" line outside the code block.
- Each image has **one role** and a **do/do-not** instruction.
- Refer to attachments again where they are used (the mark block: "the attached logo (Image 1)"; the info block: "the attached QR (Image 3), placed unaltered").
- In multi-medium requests, **each prompt only lists the images needed for that medium** and renumbers them from 1. Each prompt is standalone.
- Never describe an attachment's content that you haven't been given; ask or flag.
- If no images: omit the block, and design the mark.

---

## 4. Multi-prompt rules (several media)
1. **One prompt per medium**, each in its own code block, ready to paste.
2. **Standalone:** each contains the full identity (palette, Style DNA, mark, motif, type system, illustration technique, attachments); no "same as the banner", "as above", "matching the previous prompt".
3. **Adapted to the medium:** composition, hierarchy, hero depiction, text load, connector scale suit that medium (`03`).
4. **Consistent identity:** the same signature move and mark; the same palette; consistent icon set.
5. **Order:** primary medium first (the one that carries recognition), then others.
6. **Only the necessary content** per medium (e.g., banner has no full menu).
7. Outside the blocks: title line + "Attach:" line for each prompt; at most 2 short lines overall for assumptions.

---

## 5. Text rendering safeguards (image models misrender text)
- Provide every string **verbatim** in the TEXT block, in order of prominence, in the owner's language; keep spelling, casing, and punctuation exactly.
- Keep the **number of strings small**; shorter strings render more reliably. Long menus: warn in the assumptions line ("teks kecil mungkin perlu dikoreksi di editor") and consider splitting.
- Specify **where each text sits** and its hierarchy, not its coordinates.
- State "**render exactly as written, nothing else**"; exclude extra text, fake prices, fake URLs, and label words.
- Prices exactly as supplied ("15K" vs "Rp 15.000").
- Phone numbers and handles exactly as supplied; format kept.

---

## 6. Vocabulary toolkit (pick by function; never dump all)
- *Finish:* flat-colour vector-print finish, screen-print, risograph overprint, linocut, halftone, paper grain, hand-cut edges, hairline, monoline, keyline, offset shadow, inline stroke, knock-out.
- *Composition:* focal point, visual hierarchy, optical balance, axis, baseline, negative space, breathing room, scale contrast, visual weight, crop, bleed, overlap, rhythm, counterweight, clear space.
- *Typography:* lockup, cartouche, wordmark, descriptor, tracking, leading, bracketed serif, flared serif, slab, grotesque, humanist sans, condensed gothic, sign-painter script, chunky display, small caps, optical alignment.
- *Illustration:* hand-crafted 2D, organic contour, line-weight variation, simplified into flat shapes, cut-paper, sticker-style contour, naive folk, stylised portrait.
- *Icons:* pictogram, monoline glyph, rounded-square container, consistent optical size, shared contour weight.
- *Mood:* match to the decoded register (established, welcoming, exuberant, generous, confident, crisp, rooted, fresh, dependable, cheeky, composed, ...).
- *Anti-vocabulary (never use):* beautiful, amazing, stunning, eye-catching, vibrant, 4k, ultra-detailed, masterpiece, trending, award-winning, cinematic.

---

## 7. Exclusions
Direct, compact, comma-separated, **last in the prompt**. Two layers:
- **Core:** no photography or photorealism (unless the concept chooses photo-based), no 3D or glossy rendering, no gradients in illustrations, no neon or fluorescent colors, no additional text, prices, logos, or halal marks, **no text labels such as "WA", "IG", "Alamat", "Telp"**, no QR code pattern drawn from imagination, no mockup or scene or perspective, no accidentally skewed or warped lettering, no excessive ornamentation, no frames or borders unless chosen, no crop or bleed marks.
- **Derived from the concept:** the clichés and defaults a model would add for this category or mood. Method: ask "what would a generic model draw here?" and exclude those. Examples: a royal theme → throne/castle/turban clichés; a heritage theme → costume pastiche; a playful theme → childish mascots, novelty fonts; a food theme → floating ingredients, unwanted steam; a premium theme → discount bursts; a fresh theme → stock leaf clip-art.
- Add the user's dislikes. Remove any exclusion that contradicts the chosen concept.
- If a logo is attached: "no redrawn, restyled, or recolored version of the attached logo".

---

## 8. Prompt skeleton (structure only; wording is generated, never reused)

```
@Create image

**Attached references:** (omit if none)
- Image 1 is [role]. [do / do not].
- Image 2 is [role]. [do / do not].

**Brief:** Design a [register adjectives] [orientation] [format] for **[Name]**, [ratio/size], print-ready flat artwork, [finish]. The identity should feel [3 traits], with [the specific character] of [specific business]. Design idea: [one-sentence visual proposition]. It reads as one integrated system (one ground, one illustration language, one type system, one decorative vocabulary), not [N] separate panels, and is recognisable as [offer] at first glance.

**Art direction:** [references: material culture, era, craft, print method]; [mood]; Style DNA: [edges, contours, fills, shadows, texture, motif family, color rule]. Never [anti-style].

**Palette:** [strategy and ground decision]; Ground: ...; Primary supporting: ...; Accents (small): ...; Food/product colours (illustrations only): ...; No other hues. [legibility clause]

**Unity system:** [field: colour, texture, tonal structure]. [Connector: mechanism, origin, path, fade, contrast, interaction; behind/through all zones; below the focal point in contrast].

**Decoration:** [tiers, placement, caps]; [restraint clause].

**Layout:** [archetype]; [proportions]; [dominant element and size]; [scale caps]; [axis/baseline]; [margins/safe area]; [balance and rhythm].

**[FOCAL ZONE]: the brand mark.** [attached-logo statement OR form] [construction] [lettering anatomy] [word hierarchy] [optical quality] [descriptor/year] [evocation] [focal status]

**[ZONE 2]:** [role] [form] [content] [style rules by reference to Style DNA] [relation to the system]
**[ZONE 3]:** ...

**Info block:** [aligned group; icon set by shape and Style DNA; icon-before-value; one consistent size; plate if overlapping artwork; no label words]

**Typographic system:** [families by personality; roles; hierarchy ranking; spacing; tone line]

**TEXT (render exactly as written, nothing else):** "...", "..."

**EXCLUSIONS:** [core], [concept-derived], [user dislikes].
```
