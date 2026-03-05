# Student Q&A Supabase Setup (Unit 5 Decks)

This setup enables anonymous student question submissions from the static GitHub Pages decks and teacher moderation with a passcode. Each question now records the slide it came from so the final Q&A stage can show slide context and support spotlight-style discussion views.

## 1. Create Supabase Project
1. Create a new Supabase project.
2. Copy:
   - `SUPABASE_URL`
   - `SUPABASE_ANON_KEY`
   - `SUPABASE_SERVICE_ROLE_KEY`

## 2. Apply SQL Schema
1. Open Supabase SQL editor.
2. Run:
   - [`supabase/sql/qa_schema.sql`](/Users/kirkmanamos/Documents/GitHub/precalculus_slides/supabase/sql/qa_schema.sql)

## 3. Add Function Secrets
Set these secrets for Edge Functions:
1. `SUPABASE_URL`
2. `SUPABASE_SERVICE_ROLE_KEY`
3. `QA_TEACHER_JWT_SECRET`
   - Generate a strong random string (at least 32 chars).

## 4. Deploy Edge Functions
Deploy:
1. [`supabase/functions/qa-submit/index.ts`](/Users/kirkmanamos/Documents/GitHub/precalculus_slides/supabase/functions/qa-submit/index.ts)
2. [`supabase/functions/qa-teacher-login/index.ts`](/Users/kirkmanamos/Documents/GitHub/precalculus_slides/supabase/functions/qa-teacher-login/index.ts)
3. [`supabase/functions/qa-moderate/index.ts`](/Users/kirkmanamos/Documents/GitHub/precalculus_slides/supabase/functions/qa-moderate/index.ts)

## 5. Configure the Deck
Edit the deck you want to run and update its `QA_CONFIG`, for example:
1. [`5.1-fundamental-identities.html`](/Users/kirkmanamos/Documents/GitHub/Precalculus_Slides/5.1-fundamental-identities.html)
2. [`5.5-double-half-angle.html`](/Users/kirkmanamos/Documents/GitHub/Precalculus_Slides/5.5-double-half-angle.html)

Update:
1. `SUPABASE_URL`
2. `SUPABASE_ANON_KEY`
3. `EDGE_BASE_URL`
   - Typically: `https://<project-ref>.supabase.co/functions/v1`

## 6. Create a Class Session
Insert a session row for the deck you want to run (replace placeholders):

```sql
insert into public.qa_sessions (
  session_code,
  deck_slug,
  teacher_passcode_hash,
  is_active,
  expires_at
)
values (
  'u5-1-p3-2026-03-04',
  '5.1-fundamental-identities',
  encode(digest('YOUR_TEACHER_PASSCODE', 'sha256'), 'hex'),
  true,
  now() + interval '12 hours'
);
```

## 7. Classroom URLs
1. Student URL:
   - `.../5.1-fundamental-identities.html?session=u5-1-p3-2026-03-04`
2. Teacher URL:
   - `.../5.1-fundamental-identities.html?session=u5-1-p3-2026-03-04&mode=teacher`

Teacher then clicks `Unlock Moderation`, enters passcode, and can approve/hide questions. Approved questions appear on the deck’s Q&A stage with slide labels such as `Slide 4 · Using Double-Angle Identities`.

## 8. Security Notes
1. Students only get anonymous approved-question reads directly from REST (RLS policy).
2. All writes/moderation use Edge Functions with service-role credentials on server side.
3. Teacher moderation token expires automatically (default 8 hours).
4. CORS allowlist is currently:
   - `https://kirkmanamos.github.io`
   - `http://localhost:4173`
   - `http://localhost:5500`

## 9. Schema Upgrade Notes
If you already ran the earlier pilot schema, re-run [`supabase/sql/qa_schema.sql`](/Users/kirkmanamos/Documents/GitHub/Precalculus_Slides/supabase/sql/qa_schema.sql). It now adds these nullable columns to `public.qa_questions`:
1. `slide_id`
2. `slide_index`
3. `slide_title`

## 10. Operational Notes
1. Keep one unique `session_code` per class period to avoid mixed queues.
2. Deactivate old sessions:

```sql
update public.qa_sessions
set is_active = false
where session_code = 'u5-1-p3-2026-03-04';
```

3. To clear pilot data:

```sql
delete from public.qa_questions where session_code = 'u5-1-p3-2026-03-04';
delete from public.qa_rate_limit where session_code = 'u5-1-p3-2026-03-04';
```
