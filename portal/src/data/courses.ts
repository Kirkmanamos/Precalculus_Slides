// The classes offered on the site. Both share the same units/topics/slides
// (units.json); they differ only in which notes variant is linked and a few
// presentation details. Add a class by appending to this array.

export type NotesVariant = 'regular' | 'honors';

export interface Course {
  /** URL slug, e.g. "precalculus" -> /Precalculus_Slides/precalculus/ */
  id: string;
  /** Full display name. */
  name: string;
  /** Short label for the top nav (falls back to name). */
  nav?: string;
  /** Which notes PDFs to link: notes/unit-N-notes-<variant>.pdf */
  notesVariant: NotesVariant;
  /** One-line tagline shown on cards. */
  tagline: string;
  /** Paragraph shown in the class hero. */
  description: string;
  /** YouTube video id for the hero "start here" embed. Leave "" for a placeholder. */
  youtubeId?: string;
  /** Tailwind accent color family used for highlights. */
  accent: 'indigo' | 'violet' | 'emerald' | 'rose' | 'sky';
}

export const courses: Course[] = [
  {
    id: 'precalculus',
    name: 'Precalculus',
    notesVariant: 'regular',
    tagline: 'Functions, trig, and an on-ramp to calculus.',
    description:
      'A full year of Precalculus and Trigonometry. We study how the world ' +
      'changes through polynomial, rational, exponential, logarithmic, and ' +
      'trigonometric functions, then close with a first look at calculus.',
    youtubeId: '',
    accent: 'indigo',
  },
  {
    id: 'honors-precalculus',
    name: 'Honors Precalculus',
    nav: 'Honors Precalc',
    notesVariant: 'honors',
    tagline: 'The Precalculus sequence with honors extensions.',
    description:
      'Honors Precalculus covers the same sequence at a faster pace with ' +
      'added depth. The notes include honors-only extensions and challenge ' +
      'problems that go beyond the regular track.',
    youtubeId: '',
    accent: 'violet',
  },
];

export const getCourse = (id: string): Course | undefined =>
  courses.find((c) => c.id === id);
