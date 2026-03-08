# Modal Component

## Description

Modals are overlays that require user interaction before returning to the main content. They focus the user's attention on a specific task or piece of information.

## When to Use

Use modals when you need to:
- Request critical user input or decisions
- Display important information that requires acknowledgment
- Present complex forms that shouldn't navigate away from current page
- Show confirmations for destructive actions

## Anatomy

A modal consists of:
1. **Backdrop** - Semi-transparent overlay covering page content
2. **Container** - White surface containing modal content
3. **Header** - Title and close button
4. **Body** - Main content area
5. **Footer** - Action buttons (optional)

## Sizes

### Small (400px)

Used for simple confirmations or alerts.

```jsx
<Modal size="small">
  <Modal.Header>Delete Item?</Modal.Header>
  <Modal.Body>This action cannot be undone.</Modal.Body>
  <Modal.Footer>
    <Button variant="secondary">Cancel</Button>
    <Button variant="primary">Delete</Button>
  </Modal.Footer>
</Modal>
```

### Medium (600px)

Default size for most use cases.

### Large (800px)

Used for complex forms or detailed content.

## Behavior

**Opening:**
- Fade in animation (200ms)
- Trap focus within modal
- Prevent body scroll

**Closing:**
- Click backdrop (configurable)
- Press Escape key
- Click close button
- Click cancel/submit button

## Accessibility Features

- Focus trap prevents tabbing outside modal
- `role="dialog"` and `aria-modal="true"` attributes
- Restore focus to trigger element on close
- `aria-labelledby` references header text
- `aria-describedby` references body content

## Best Practices

**Do:**
- Keep modal content focused on a single task
- Provide clear primary and secondary actions
- Allow Escape key to close non-critical modals
- Use sparingly to avoid interrupting user flow

**Don't:**
- Stack modals on top of each other
- Make modals full screen on desktop (use page navigation instead)
- Hide the close button without good reason
- Use for non-essential content (consider tooltips or popovers)
