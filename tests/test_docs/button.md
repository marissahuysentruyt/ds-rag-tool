# Button Component

## Overview

Buttons allow users to take actions and make choices with a single tap. They communicate actions that users can take and are typically placed throughout your UI.

## Variants

### Primary Button

The primary button is used for the main call-to-action on a page. Use it sparingly to draw attention to the most important action.

```jsx
<Button variant="primary">Submit Form</Button>
```

**Usage Guidelines:**
- Use only one primary button per page or section
- Label should clearly describe the action
- Minimum width of 88px for accessibility

### Secondary Button

Secondary buttons are used for less prominent actions. They can be used multiple times on a page.

```jsx
<Button variant="secondary">Cancel</Button>
```

### Tertiary Button

Tertiary buttons are used for the least important actions, often appearing as text-only buttons.

```jsx
<Button variant="tertiary">Learn More</Button>
```

## Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| variant | 'primary' \| 'secondary' \| 'tertiary' | 'primary' | Visual style variant |
| size | 'small' \| 'medium' \| 'large' | 'medium' | Button size |
| disabled | boolean | false | Whether button is disabled |
| fullWidth | boolean | false | Whether button takes full width |
| onClick | function | - | Click handler function |

## Accessibility

- All buttons must have accessible text or `aria-label`
- Use `disabled` attribute instead of pointer-events
- Maintain 44x44px minimum touch target on mobile
- Support keyboard navigation (Enter and Space keys)

## Best Practices

**Do:**
- Use clear, action-oriented labels
- Place primary action on the right in dialog boxes
- Maintain consistent button heights across variants

**Don't:**
- Use multiple primary buttons in the same context
- Make buttons too small (below 88px width)
- Use disabled buttons without explanation
