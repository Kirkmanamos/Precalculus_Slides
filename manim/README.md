# Manim Scenes

Manim animation scenes for the Precalculus curriculum.
Each scene exports a video that is embedded into the corresponding Slidev deck.

## Directory Structure

```
manim/
├── shared/
│   ├── colors.py     Color and font constants (synchronized with Slidev palette)
│   ├── styles.py     Text and Mobject styles (create when needed)
│   └── helpers.py    Reusable scene utilities (create when needed)
└── scenes/
    └── (scene files go here)
```

## Starting a New Scene

```python
from manim import *
from shared.colors import *

class MyScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # ...
```

## Render Command

```bash
# Standard quality (for slide embedding)
manim -pql scenes/my_scene.py MyScene

# High quality (for final export)
manim -pqh scenes/my_scene.py MyScene
```

Output goes to `media/videos/`. Copy the final `.mp4` to
`public/manim/` inside the target Slidev deck.

## Naming Conventions

- Scene files: `unit_topic_scene.py` (snake_case)
- Scene classes: `PascalCase` matching the topic
- Exported videos: `scene-name.mp4` in `public/manim/`

## Log New Scenes

After building any scene, add it to `COMPONENT_REGISTRY.md`
and update `CHANGELOG.md`.
