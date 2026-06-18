// Shape of the course data in units.json.
// Edit units.json to update the site — you never need to touch components.

export type ResourceType =
  | 'slides' // interactive HTML deck
  | 'notes' // PDF / printable notes
  | 'video' // video tutorial (YouTube, etc.)
  | 'key' // answer key
  | 'worksheet' // homework / practice
  | 'activity' // in-class activity / station
  | 'playground' // interactive sandbox
  | 'reference' // supplemental reference
  | 'freeresponse' // free-response / AP-style prompts
  | 'studyguide' // unit study guide
  | 'test'; // practice / old test

export interface Resource {
  type: ResourceType;
  title: string;
  /**
   * Either a bare filename of a deck at the repo root
   * (e.g. "4.3-trig-functions-unit-circle.html") — the base path is added
   * automatically — or a full external URL (https://...).
   */
  href?: string;
  /** Optional, e.g. "32:18" for a video. */
  duration?: string;
  /**
   * Optional track restriction. When set, the resource only appears for the
   * matching course (regular vs honors). Omit to show in both — same idea as
   * the per-variant notes PDF.
   */
  variant?: 'regular' | 'honors';
}

export interface Topic {
  number: string; // "1.1"
  title: string;
  resources: Resource[];
}

export interface Unit {
  number: number;
  title: string;
  /** Optional one-line blurb shown under the unit title. */
  blurb?: string;
  /**
   * Optional unit-wide resources (e.g. the full-unit notes PDF) shown in a
   * strip directly under the unit header, above the per-topic rows.
   */
  resources?: Resource[];
  topics: Topic[];
  /**
   * Optional end-of-unit "Review & Assessment" resources (free response,
   * study guide, old/practice tests), shown in a strip below the topics.
   * Use a resource's `variant` to scope an item to one track.
   */
  review?: Resource[];
}
