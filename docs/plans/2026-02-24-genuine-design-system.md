# Genuine Design System Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create the Genuine Design System as a .pen file — Foundation tokens + Core Components — based on Claude Code's design language with futuristic amber glow aesthetics.

**Architecture:** Hybrid Token-First approach: Figma Variables (Primitive → Semantic) defined first, then Core Components built on top. Dark/Light theme switching handled entirely at the token layer via Figma Variable Modes.

**Tech Stack:** Pencil MCP (`mcp__pencil__batch_design`, `mcp__pencil__set_variables`, `mcp__pencil__get_screenshot`), .pen file format

---

## Task 1: Create the .pen file and Foundation frame

**Files:**
- Create: `design/genuine-design-system.pen`

**Step 1: Open a new .pen document**

```
Use mcp__pencil__open_document with filePathOrTemplate="new"
```
Expected: New document opens in Pencil editor.

**Step 2: Verify editor state**

```
Use mcp__pencil__get_editor_state with include_schema=false
```
Expected: Active file path returned.

**Step 3: Commit**

```bash
git add design/
git commit -m "feat: create genuine-design-system pen file"
```

---

## Task 2: Define Variables (Token System)

**Files:**
- Modify: `design/genuine-design-system.pen` (via set_variables)

**Step 1: Set Primitive + Semantic color variables with Dark/Light modes**

Use `mcp__pencil__set_variables` with the following structure:

```json
{
  "neutral-0":   { "default": "#0A0A0A" },
  "neutral-100": { "default": "#141414" },
  "neutral-200": { "default": "#1C1C1C" },
  "neutral-300": { "default": "#262626" },
  "neutral-400": { "default": "#404040" },
  "neutral-500": { "default": "#737373" },
  "neutral-600": { "default": "#A3A3A3" },
  "neutral-700": { "default": "#D4D4D4" },
  "neutral-800": { "default": "#F5F5F5" },
  "neutral-900": { "default": "#FFFFFF" },

  "amber-50":  { "default": "#1C1508" },
  "amber-100": { "default": "#451A03" },
  "amber-200": { "default": "#92400E" },
  "amber-300": { "default": "#D97706" },
  "amber-400": { "default": "#F59E0B" },
  "amber-500": { "default": "#FBBF24" },
  "amber-600": { "default": "#FEF3C7" },

  "surface/base":    { "dark": "#0A0A0A",  "light": "#FFFFFF"  },
  "surface/raised":  { "dark": "#1C1C1C",  "light": "#F5F5F5"  },
  "surface/overlay": { "dark": "#262626",  "light": "#EDEDED"  },

  "text/default":  { "dark": "#F5F5F5", "light": "#0A0A0A" },
  "text/subtle":   { "dark": "#A3A3A3", "light": "#737373" },
  "text/disabled": { "dark": "#404040", "light": "#D4D4D4" },

  "border/default": { "dark": "#262626", "light": "#E5E5E5" },
  "border/strong":  { "dark": "#404040", "light": "#D4D4D4" },

  "accent/default": { "dark": "#F59E0B", "light": "#D97706" },
  "accent/hover":   { "dark": "#FBBF24", "light": "#B45309" },
  "accent/subtle":  { "dark": "#1C1508", "light": "#FEF3C7" }
}
```

**Step 2: Verify variables**

```
Use mcp__pencil__get_variables
```
Expected: All tokens listed with dark/light mode values.

**Step 3: Commit**

```bash
git add design/
git commit -m "feat: define color tokens with dark/light modes"
```

---

## Task 3: Foundation Page — Color Palette

**Files:**
- Modify: `design/genuine-design-system.pen`

**Step 1: Get guidelines for design system**

```
Use mcp__pencil__get_guidelines with topic="design-system"
```

**Step 2: Create Foundation — Colors frame**

Use `mcp__pencil__batch_design` to build a Color Palette documentation frame:
- Title: "Color Palette" (JetBrains Mono, 32px, text/default)
- Section: Neutral swatches (10 color chips, 64×64px each, labeled)
- Section: Amber swatches (7 color chips)
- Section: Semantic tokens table (Dark / Light columns)

**Step 3: Screenshot and verify**

```
Use mcp__pencil__get_screenshot with the frame node ID
```
Expected: Color palette clearly visible with labels and hex values.

**Step 4: Commit**

```bash
git commit -m "feat: add color palette documentation frame"
```

---

## Task 4: Foundation Page — Typography

**Files:**
- Modify: `design/genuine-design-system.pen`

**Step 1: Create Typography frame**

Use `mcp__pencil__batch_design`:
- Title: "Typography"
- Sans section: Show each size (12/14/16/18/24/32/48px) with Inter, all 4 weights
- Mono section: Show 12/14px JetBrains Mono samples
- Label each row with token name (e.g. `text/display`, `text/body`, `text/caption`)

**Step 2: Screenshot and verify**

```
Use mcp__pencil__get_screenshot
```
Expected: Type scale readable, mono vs sans clearly distinguished.

**Step 3: Commit**

```bash
git commit -m "feat: add typography documentation frame"
```

---

## Task 5: Foundation Page — Spacing, Radius, Shadow

**Files:**
- Modify: `design/genuine-design-system.pen`

**Step 1: Create Spacing frame**

Use `mcp__pencil__batch_design`:
- Show each spacing token as a colored bar with label (space/1=4px … space/16=64px)

**Step 2: Create Radius frame**

- Show 4 rectangles: none(0px) · sm(4px) · md(8px) · full(9999px)
- Each labeled with token name

**Step 3: Create Shadow/Glow frame**

- Show 4 boxes: shadow/sm · shadow/md · glow/accent · glow/strong
- Dark background to make glow visible

**Step 4: Screenshot and verify**

```
Use mcp__pencil__get_screenshot
```

**Step 5: Commit**

```bash
git commit -m "feat: add spacing, radius, shadow documentation frames"
```

---

## Task 6: Component — Button

**Files:**
- Modify: `design/genuine-design-system.pen`

**Step 1: Create Button component frame**

Use `mcp__pencil__batch_design` to build a reusable Button component (`reusable: true`):

Variants matrix:
- Rows: primary · secondary · ghost · destructive
- Columns: default · hover · focus · disabled · loading
- Sizes: sm(32px h) · md(40px h) · lg(48px h)

Specs:
- primary: fill=accent/default, label=black, hover: +glow/accent border
- secondary: fill=surface/raised, border=border/strong, label=text/default
- ghost: fill=transparent, label=text/subtle
- destructive: fill=#DC2626, label=white
- radius=4px, font=14px/500 Inter

**Step 2: Screenshot and verify all states visible**

```
Use mcp__pencil__get_screenshot
```

**Step 3: Commit**

```bash
git commit -m "feat: add Button component with all variants and states"
```

---

## Task 7: Component — Input

**Files:**
- Modify: `design/genuine-design-system.pen`

**Step 1: Create Input component**

Use `mcp__pencil__batch_design` (`reusable: true`):

Variants:
- default: fill=surface/raised, border=border/default, 1px
- focus: border=accent/default, 2px, + glow/accent
- error: border=#DC2626, 2px
- disabled: fill=surface/base, text=text/disabled

Types: text · search(+ icon left) · password(+ eye icon right) · textarea(resizable)

Specs: radius=4px, height=40px (text), font=14px Inter

**Step 2: Screenshot and verify**

```
Use mcp__pencil__get_screenshot
```

**Step 3: Commit**

```bash
git commit -m "feat: add Input component with all variants and types"
```

---

## Task 8: Component — Card

**Files:**
- Modify: `design/genuine-design-system.pen`

**Step 1: Create Card component**

Use `mcp__pencil__batch_design` (`reusable: true`):

Variants:
- flat: fill=surface/base, no border
- raised: fill=surface/raised, shadow/sm
- bordered: fill=surface/raised, border=border/default
- interactive: bordered + hover→border=accent/default + glow/accent

Specs: radius=8px, padding=24px, min-height=120px
Include: optional header slot, body slot, footer slot

**Step 2: Screenshot and verify**

```
Use mcp__pencil__get_screenshot
```

**Step 3: Commit**

```bash
git commit -m "feat: add Card component with 4 variants"
```

---

## Task 9: Component — Modal

**Files:**
- Modify: `design/genuine-design-system.pen`

**Step 1: Create Modal component**

Use `mcp__pencil__batch_design` (`reusable: true`):

Structure:
- Overlay: fill=rgba(0,0,0,0.7), backdrop-blur
- Container: fill=surface/overlay, border=border/strong, radius=8px, shadow/md
- Header: title text + close button (×)
- Body: scrollable content area
- Footer: button row (right-aligned)

Sizes: default(480px w) · large(640px w)

**Step 2: Screenshot and verify**

```
Use mcp__pencil__get_screenshot
```

**Step 3: Commit**

```bash
git commit -m "feat: add Modal component in 2 sizes"
```

---

## Task 10: Component — Badge & Tag

**Files:**
- Modify: `design/genuine-design-system.pen`

**Step 1: Create Badge component**

Use `mcp__pencil__batch_design` (`reusable: true`):

Variants: default · success · warning · error · accent

| Variant | Fill | Text |
|---------|------|------|
| default | surface/overlay | text/subtle |
| success | #14532D | #86EFAC |
| warning | accent/subtle | accent/default |
| error | #450A0A | #FCA5A5 |
| accent | accent/default | #000000 |

Sizes: xs(4px 8px) · sm(4px 10px), radius=9999px, font=11px JetBrains Mono/600

**Step 2: Create Tag component**

- fill=surface/raised, border=border/default, radius=4px
- removable variant: + × icon button on right

**Step 3: Screenshot and verify**

```
Use mcp__pencil__get_screenshot
```

**Step 4: Commit**

```bash
git commit -m "feat: add Badge and Tag components"
```

---

## Task 11: Component — Divider

**Files:**
- Modify: `design/genuine-design-system.pen`

**Step 1: Create Divider component**

Use `mcp__pencil__batch_design` (`reusable: true`):

Variants:
- horizontal: 1px line, color=border/default, full width
- vertical: 1px line, color=border/default, full height
- label: horizontal with centered text label (12px JetBrains Mono, text/disabled)
  Example: "──── OR ────"

**Step 2: Screenshot and verify**

```
Use mcp__pencil__get_screenshot
```

**Step 3: Commit**

```bash
git commit -m "feat: add Divider component"
```

---

## Task 12: Final Review & Component Library Page

**Files:**
- Modify: `design/genuine-design-system.pen`

**Step 1: Create a "Component Library" overview frame**

Arrange all components in a single overview frame:
- Grid layout showing all components in dark mode
- Labels for each component section

**Step 2: Check layout for problems**

```
Use mcp__pencil__snapshot_layout with problemsOnly=true
```
Expected: No clipping or overlap issues.

**Step 3: Full screenshot of overview**

```
Use mcp__pencil__get_screenshot
```

**Step 4: Push to GitHub**

```bash
git push origin master
```

---

## Summary

| Task | Component | Est. Operations |
|------|-----------|----------------|
| 1 | File setup | 2 |
| 2 | Variables/Tokens | 1 |
| 3 | Color Palette frame | 15 |
| 4 | Typography frame | 12 |
| 5 | Spacing/Radius/Shadow | 10 |
| 6 | Button | 20 |
| 7 | Input | 15 |
| 8 | Card | 12 |
| 9 | Modal | 15 |
| 10 | Badge + Tag | 12 |
| 11 | Divider | 6 |
| 12 | Overview + Push | 5 |
