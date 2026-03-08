# Typography Guidelines

## Overview

Typography is the foundation of our design system. It establishes hierarchy, improves readability, and reinforces our brand identity.

## Type Scale

Our type scale uses a modular scale with a 1.25 ratio (major third).

| Style | Size | Line Height | Weight | Usage |
|-------|------|-------------|--------|-------|
| Display | 48px | 56px | 700 | Marketing headers, hero sections |
| H1 | 36px | 44px | 700 | Page titles |
| H2 | 28px | 36px | 600 | Section headers |
| H3 | 22px | 32px | 600 | Subsection headers |
| H4 | 18px | 28px | 600 | Card titles, group labels |
| Body Large | 16px | 24px | 400 | Emphasized body text |
| Body | 14px | 22px | 400 | Default body text |
| Body Small | 12px | 18px | 400 | Captions, helper text |
| Label | 14px | 20px | 500 | Form labels, button text |

## Font Families

### Primary Font: Inter

Inter is our primary typeface for UI and content.

```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

**Weights Used:**
- Regular (400) - Body text
- Medium (500) - Labels, emphasized text
- Semibold (600) - Headings H2-H4
- Bold (700) - Main headings, display text

### Monospace Font: JetBrains Mono

Used for code snippets and technical content.

```css
font-family: 'JetBrains Mono', 'Monaco', 'Courier New', monospace;
```

## Text Styles

### Headings

Headings should use sentence case by default.

```jsx
<h1>This is a page title</h1>
<h2>This is a section header</h2>
```

**Spacing:**
- Add 32px margin-top and 16px margin-bottom for H1
- Add 24px margin-top and 12px margin-bottom for H2-H3
- Add 16px margin-top and 8px margin-bottom for H4

### Body Text

Body text should be comfortable to read:
- Maximum line length: 70 characters (680px)
- Paragraph spacing: 16px between paragraphs
- Justified text: Never use justified alignment

### Lists

```markdown
Unordered lists:
- Use bullet points for unordered lists
- Maintain 8px spacing between items
- Indent nested lists by 24px

Ordered lists:
1. Use numbers for sequential steps
2. Maintain consistent spacing
3. Use periods after numbers
```

## Accessibility

**Minimum Sizes:**
- Body text: 14px minimum (16px preferred)
- Touch targets: 14px minimum for tap targets

**Contrast Requirements:**
- Normal text: 4.5:1 minimum contrast ratio
- Large text (18px+): 3:1 minimum contrast ratio

**Readable Hierarchy:**
- Limit to 3-4 heading levels per page
- Maintain consistent heading order (don't skip levels)
- Use semantic HTML tags (`<h1>`, `<h2>`, etc.)

## Responsive Typography

Typography scales down on smaller screens:

```css
/* Mobile (< 768px) */
h1 { font-size: 28px; line-height: 36px; }
h2 { font-size: 22px; line-height: 30px; }
body { font-size: 14px; line-height: 22px; }

/* Tablet (768px - 1024px) */
h1 { font-size: 32px; line-height: 40px; }
h2 { font-size: 24px; line-height: 32px; }
body { font-size: 14px; line-height: 22px; }

/* Desktop (> 1024px) */
h1 { font-size: 36px; line-height: 44px; }
h2 { font-size: 28px; line-height: 36px; }
body { font-size: 14px; line-height: 22px; }
```

## Best Practices

**Do:**
- Use consistent type scales throughout the application
- Maintain sufficient line height for readability (1.5x font size minimum)
- Left-align body text in most cases
- Use medium or semibold weights for emphasis rather than bold

**Don't:**
- Use more than 2-3 font families in a single application
- Set body text smaller than 14px
- Use all caps for long passages of text
- Underline text unless it's a link
