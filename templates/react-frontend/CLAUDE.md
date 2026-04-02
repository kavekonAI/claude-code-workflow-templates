# Claude Configuration - React Frontend

## Project Context
Modern React application with functional components and hooks.

## Memory Patterns
- Remember component hierarchy
- Track state management strategy
- Maintain consistent prop types
- Document custom hook dependencies

## Workflow Preferences
1. Plan component structure
2. Create presentational components first
3. Add state and logic with hooks
4. Implement routing and data fetching
5. Add styling and animations

## Code Style Guidelines
- Functional components over classes
- Named exports for components
- Descriptive prop and state names
- Use TypeScript when possible

## Component Structure
- One component per file
- Separate concerns: presentation vs logic
- Reusable hooks for shared behavior
- Container components for data fetching

## State Management
- useState for local component state
- useContext for app-wide state
- Consider Zustand/Redux for complex apps
- Keep state as local as possible

## Styling Approach
- CSS Modules or styled-components
- Design system with variables
- Responsive utility classes
- Consistent spacing scale

## Common Tasks
- Create reusable button/input components
- Implement form validation
- Handle loading and error states
- Optimize performance with memoization

## Hooks to Configure
- Auto-format on save
- ESLint with React rules
- Hot module replacement
- Bundle size analysis

## Avoid
- Prop drilling beyond 2 levels
- Large monolithic components
- Inline styles except for dynamic values
- Direct DOM manipulation
