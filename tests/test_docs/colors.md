# Color System

## Overview

Our color system is designed to be accessible, consistent, and expressive. All colors meet WCAG 2.1 AA standards for contrast ratios.

## Primary Colors

### Brand Blue

Our primary brand color used for key actions and interactive elements.

- **blue-50**: `#E3F2FD` - Lightest tint, backgrounds
- **blue-100**: `#BBDEFB` - Light backgrounds, hover states
- **blue-500**: `#2196F3` - Primary brand color
- **blue-700**: `#1976D2` - Active states, focus rings
- **blue-900**: `#0D47A1` - Darkest shade, high emphasis text

**Usage:**
- Primary buttons and links
- Active navigation items
- Focus indicators
- Selected states

### Supporting Colors

#### Green (Success)

- **green-500**: `#4CAF50` - Success messages, confirmations
- **green-700**: `#388E3C` - Hover states

#### Red (Error)

- **red-500**: `#F44336` - Error messages, destructive actions
- **red-700**: `#D32F2F` - Hover states for destructive buttons

#### Orange (Warning)

- **orange-500**: `#FF9800` - Warnings, cautionary messages
- **orange-700**: `#F57C00` - Hover states

#### Blue-Grey (Info)

- **blue-grey-500**: `#607D8B` - Informational messages
- **blue-grey-700**: `#455A64` - Hover states

## Neutral Colors

### Grey Scale

Used for text, backgrounds, borders, and surfaces.

- **grey-50**: `#FAFAFA` - Page backgrounds
- **grey-100**: `#F5F5F5` - Card backgrounds
- **grey-200**: `#EEEEEE` - Dividers, disabled backgrounds
- **grey-300**: `#E0E0E0` - Borders
- **grey-400**: `#BDBDBD` - Disabled text
- **grey-500**: `#9E9E9E` - Placeholder text
- **grey-600**: `#757575` - Secondary text
- **grey-700**: `#616161` - Primary text on light backgrounds
- **grey-900**: `#212121` - Headings, high emphasis text

## Semantic Colors

Colors mapped to specific semantic meanings:

```css
--color-primary: var(--blue-500);
--color-success: var(--green-500);
--color-error: var(--red-500);
--color-warning: var(--orange-500);
--color-info: var(--blue-grey-500);

--color-text-primary: var(--grey-900);
--color-text-secondary: var(--grey-600);
--color-text-disabled: var(--grey-400);

--color-background-primary: #FFFFFF;
--color-background-secondary: var(--grey-50);
--color-border: var(--grey-300);
```

## Accessibility

All color combinations meet WCAG 2.1 standards:

- **AA Standard**: Minimum 4.5:1 contrast ratio for normal text
- **AAA Standard**: Minimum 7:1 contrast ratio for normal text (where possible)
- **Large Text**: Minimum 3:1 contrast ratio for text 18px+ or 14px+ bold

**Color Contrast Examples:**
- `grey-900` on `white`: 16.1:1 (AAA)
- `blue-500` on `white`: 4.6:1 (AA)
- `grey-600` on `white`: 7.2:1 (AAA)

**Never use color as the only indicator:**
- Combine with icons or text labels
- Use patterns or textures for charts
- Provide text alternatives for color-coded information

## Dark Mode

Dark mode variants use inverted luminance:

- **Background**: `grey-900` (`#212121`)
- **Surface**: `grey-800` (`#424242`)
- **Primary Text**: `grey-50` (`#FAFAFA`)
- **Secondary Text**: `grey-400` (`#BDBDBD`)

Primary colors remain mostly unchanged but may be slightly desaturated for reduced eye strain.
