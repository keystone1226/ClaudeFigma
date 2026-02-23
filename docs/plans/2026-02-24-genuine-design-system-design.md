# Genuine Design System — Design Document

**Date:** 2026-02-24
**Status:** Approved
**Scope:** Foundation + Core Components
**Platforms:** Web App / SaaS, Marketing / Landing Pages
**Theme:** Dark + Light (token-based switching)
**Design Language:** Claude Code — Futuristic

---

## Overview

Genuine Design System은 Claude Code의 디자인 랭귀지(다크 터미널 미학, 앰버 액센트, 모노스페이스 타이포그래피)를 기반으로 미래지향적인 UI를 구성하는 시스템이다. Hybrid 아키텍처(Token-First + Component 즉시 구축)를 채택해 확장성과 속도를 동시에 확보한다.

---

## Architecture

**Hybrid (Token-First + Core Components)**

```
Primitive Tokens
      ↓
Semantic Tokens (Dark / Light Mode)
      ↓
Core Components (Button, Input, Card, Modal, Badge, Tag, Divider)
```

---

## Section 1: Foundation

### Color Tokens

#### Primitive Palette

| Group   | Values |
|---------|--------|
| Neutral | #0A0A0A · #141414 · #1C1C1C · #262626 · #404040 · #737373 · #A3A3A3 · #D4D4D4 · #F5F5F5 · #FFFFFF |
| Amber   | #1C1508 · #451A03 · #92400E · #D97706 · #F59E0B · #FBBF24 · #FEF3C7 |

#### Semantic Tokens

| Token | Dark | Light |
|-------|------|-------|
| `surface/base` | #0A0A0A | #FFFFFF |
| `surface/raised` | #1C1C1C | #F5F5F5 |
| `surface/overlay` | #262626 | #EDEDED |
| `text/default` | #F5F5F5 | #0A0A0A |
| `text/subtle` | #A3A3A3 | #737373 |
| `text/disabled` | #404040 | #D4D4D4 |
| `border/default` | #262626 | #E5E5E5 |
| `border/strong` | #404040 | #D4D4D4 |
| `accent/default` | #F59E0B | #D97706 |
| `accent/hover` | #FBBF24 | #B45309 |
| `accent/subtle` | #1C1508 | #FEF3C7 |

### Typography

| Role | Font | Sizes | Weight |
|------|------|-------|--------|
| UI (Sans) | Inter | 12 / 14 / 16 / 18 / 24 / 32 / 48px | 400 · 500 · 600 · 700 |
| Code (Mono) | JetBrains Mono | 12 / 14px | 400 · 600 |

### Spacing Scale (4px base)

| Token | Value |
|-------|-------|
| space/1 | 4px |
| space/2 | 8px |
| space/3 | 12px |
| space/4 | 16px |
| space/5 | 20px |
| space/6 | 24px |
| space/8 | 32px |
| space/10 | 40px |
| space/12 | 48px |
| space/16 | 64px |

### Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `radius/none` | 0px | 터미널 블록, 코드 |
| `radius/sm` | 4px | 버튼, 인풋 |
| `radius/md` | 8px | 카드, 모달 |
| `radius/full` | 9999px | 배지, 태그 |

### Shadow / Glow

| Token | Value |
|-------|-------|
| `shadow/sm` | 0 1px 4px rgba(0,0,0,0.4) |
| `shadow/md` | 0 4px 16px rgba(0,0,0,0.5) |
| `glow/accent` | 0 0 12px rgba(245,158,11,0.25) |
| `glow/strong` | 0 0 24px rgba(245,158,11,0.40) |

---

## Section 2: Core Components

### Button

- **Variants:** primary · secondary · ghost · destructive
- **Sizes:** sm · md · lg
- **States:** default · hover · focus · disabled · loading

| Variant | Background | Text | Border | Hover |
|---------|-----------|------|--------|-------|
| primary | accent/default | black | — | + glow/accent |
| secondary | surface/raised | text/default | border/strong | border/accent |
| ghost | transparent | text/subtle | — | text/default |
| destructive | #DC2626 | white | — | #B91C1C |

- radius: radius/sm · padding: 8px 16px (md) · font: 14px/500

### Input / Textarea

- **Variants:** default · error · disabled
- **Types:** text · search · password · textarea

```
bg: surface/raised
border: border/default
focus: accent/default (1px→2px) + glow/accent
text: text/default
placeholder: text/disabled
radius: radius/sm
font: 14px, mono 옵션
```

### Card

- **Variants:** flat · raised · bordered · interactive

| Variant | Background | Border | Shadow | Hover |
|---------|-----------|--------|--------|-------|
| flat | surface/base | — | — | — |
| raised | surface/raised | — | shadow/sm | — |
| bordered | surface/raised | border/default | — | — |
| interactive | surface/raised | border/default | — | border/accent + glow/accent |

- radius: radius/md · padding: space/6 (24px)

### Modal / Dialog

```
Overlay:   rgba(0,0,0,0.7) + backdrop-blur: 4px
Container: bg=surface/overlay, border=border/strong
           radius=radius/md, shadow/md
Sizes:     default(480px) · large(640px)
Structure: Header(18px/600) + Body(14px/400) + Footer(Button 조합)
```

### Badge

- **Variants:** default · success · warning · error · accent
- **Sizes:** xs · sm

```
radius: radius/full
font: 11px / JetBrains Mono / weight 600
```

| Variant | Background | Text |
|---------|-----------|------|
| default | surface/overlay | text/subtle |
| success | #14532D | #86EFAC |
| warning | accent/subtle | accent/default |
| error | #450A0A | #FCA5A5 |
| accent | accent/default | black |

### Tag

```
bg: surface/raised
border: border/default
radius: radius/sm
removable: × 버튼 포함 variant
```

### Divider

```
color: border/default (1px solid)
orientation: horizontal · vertical
label variant: text/disabled / 12px mono ("──── OR ────")
```

---

## Component Summary

| Component | Variants | States |
|-----------|---------|--------|
| Button | 4 | 5 |
| Input | 3 | 4 |
| Card | 4 | — |
| Modal | 2 sizes | — |
| Badge | 5 | — |
| Tag | 1 | 2 |
| Divider | 2 | — |

---

## Design Principles

1. **Glow as Interaction Signal** — focus/hover에 `glow/accent` 일관 적용
2. **Mono for Technical** — 코드, 배지, 레이블에 JetBrains Mono 사용
3. **Token-Driven Theming** — 컴포넌트는 semantic 토큰만 참조, 다크/라이트는 토큰 레이어에서 처리
4. **Sharp + Minimal** — radius 최소화, 여백 중심의 레이아웃
