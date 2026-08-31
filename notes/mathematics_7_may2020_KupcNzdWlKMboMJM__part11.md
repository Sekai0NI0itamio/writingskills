# Idea Flow Notes: mathematics_7_may2020_KupcNzdWlKMboMJM — References

## Paragraph Flow (move by move)

This section is not a narrative argument; it is a numbered list of ten bibliographic entries with no prose sentences. I will therefore treat the section as a single "paragraph" (the full list) and map each entry field-by-field, because the field order is the only logical structure present.

**Entry [1] — Authored Q&A source with hyperlinked user handle:**
- Field 1 (author handle + profile link): *"Peter Petrov (https://math.stackexchange.com/users/116591/peter-petrov)"* — credits a named contributor and links their profile. Hands to Field 2 by **credit-then-artifact**: once authorship is fixed, the reader needs to know what was written.
- Field 2 (work title): *"Normalizing a quater-nion"* — names the specific answer/post. Hands to Field 3 by **artifact-then-locator**: a named work needs a retrieval address.
- Field 3 (URL): *"url: https://math.stackexchange.com/q/1703467"* — supplies the retrieval address. Hands to Field 4 by **locator-then-timestamp**: a snapshot must be dated.
- Field 4 (access date): *"visited on 02/10/2020"* — pins the snapshot.

**Entry [3] — Unauthored institutional landing page:**
- Field 1 (title, author omitted): *"About OpenGL"* — opens directly on the work because no individual author exists. Hands to Field 2 by the same **artifact-then-locator** logic.
- Field 2 (URL): *"url: https://www.opengl.org/about/"* — retrieval address.
- Field 3 (access date): *"visited on 03/04/2020"* — timestamp.

**Entry [8] — Collective-author encyclopedia entry:**
- Field 1 (collective author): *"Wikipedia contributors."* — attributes the article to the editor group. Hands to Field 2 by **author-then-edition**: an encyclopedic source needs a year.
- Field 2 (publication identity + year): *"Wikipedia, The Free Encyclopedia. 2020."* — fixes the edition consulted. Hands to Field 3 by **edition-then-locator**.
- Field 3 (URL): *"url: https://en.wikipedia.org/wiki/Euler_angles"* — retrieval address. Hands to Field 4 by **locator-then-timestamp**.
- Field 4 (access date): *"visited on 02/10/2019"* — timestamp.

Across the whole list, each entry hands forward to the next by **enumeration** (the bracketed number signals a new, independent record), and the entries cluster implicitly by topic: quaternions ([1], [9], [10]), rendering/OpenGL infrastructure ([2], [3], [5]), and Euler angles ([4], [6], [7], [8]).

## What This Section Does (content sequence)

A References section executes the following ordered moves:

1. **Author attribution** — names the responsible party, or signals that none exists. This sets up the credibility anchor.
2. **Work title** — names the specific artifact consulted. This sets up the need for an edition stamp.
3. **Publication/edition year** (only when the source is versioned) — pins which snapshot of the work was used. This sets up the need for a locator.
4. **URL / locator** — gives the retrieval address. This sets up the need for a verification date.
5. **Access date** — dates the retrieval so the snapshot can be re-checked.

The order is **identity → artifact → time → place → timestamp**: the question a reader asks first ("Who wrote this?") is answered first, and each subsequent move answers the next question a reader would naturally ask. Skipping any slot leaves the reader unable to retrace the source.

## Paragraph Skeletons (replicable templates)

**SKELETON A — Authored web source with user handle:**
`[Author handle + profile URL]. [Work title]. url: [URL] (visited on [DD/MM/YYYY]).`

1. What each slot holds: Slot 1 is a noun phrase (proper name) followed by a hyperlinked profile URL in parentheses. Slot 2 is a noun phrase (the exact page/question title). Slot 3 is the keyword `url:` plus a full web address. Slot 4 is the fixed phrase `visited on` plus a date in DD/MM/YYYY form.
2. How to fill it with a different idea: pick a Q&A site answer whose username you can link; transcribe the question title verbatim; copy the question permalink; record the date you opened it.
3. Original fill: *"Peter Petrov (https://math.stackexchange.com/users/116591/peter-petrov). Normalizing a quater-nion. url: https://math.stackexchange.com/q/1703467 (visited on 02/10/2020)."*
4. Demonstration fill with a different idea: *"JaneDoe (https://physics.stackexchange.com/users/4521/janedoe). Why does ice float on water. url: https://physics.stackexchange.com/q/5012 (visited on 15/06/2024)."*

**SKELETON B — Collective-author encyclopedia entry:**
`[Collective author]. [Article title] — [Encyclopedia name], The Free Encyclopedia. [Year]. url: [URL] (visited on [DD/MM/YYYY]).`

1. What each slot holds: Slot 1 is a plural-author noun phrase. Slot 2 is the article title (noun phrase). Slot 3 is the encyclopedia name + a 4-digit year, separated by an em-dash from Slot 2. Slot 4 is `url:` + address. Slot 5 is `visited on` + date.
2. How to fill it with a different idea: open a Wikipedia article, copy the "Wikipedia contributors" prefix from the citation-export page, paste the article title, append the encyclopedia label and the year shown in the export, copy the article URL, record the date you accessed it.
3. Original fill: *"Wikipedia contributors. Euler angles — Wikipedia, The Free Encyclopedia. 2020. url: https://en.wikipedia.org/wiki/Euler_angles (visited on 02/10/2019)."*
4. Demonstration fill with a different idea: *"Wikipedia contributors. Black hole — Wikipedia, The Free Encyclopedia. 2023. url: https://en.wikipedia.org/wiki/Black_hole (visited on 22/03/2024)."*

**SKELETON C — Unauthored institutional page:**
`[Page title]. url: [URL] (visited on [DD/MM/YYYY]).`

1. What each slot holds: Slot 1 is a noun phrase (the page title) with the author slot deliberately omitted. Slot 2 is `url:` + address. Slot 3 is `visited on` + date.
2. How to fill it with a different idea: pick an official "About" or landing page whose publisher is an institution rather than an individual; skip the author field; copy the URL; record the access date.
3. Original fill: *"About OpenGL. url: https://www.opengl.org/about/ (visited on 03/04/2020)."*
4. Demonstration fill with a different idea: *"About the IUCN. url: https://www.iucn.org/about (visited on 01/02/2024)."*

## Express-Idea Vocabulary

A References section uses structural labels rather than connective prose, but it does have a small fixed vocabulary:

- **Sequencing (implicit, not verbal):** bracketed numbers carry order — *[1], [2], [3] … [10]*; no prose connective is used between entries.
- **Attribution connector:** *"Wikipedia contributors."* introduces a collective author — e.g. in *"Wikipedia contributors. Euler angles"* ([8]).
- **Location connector:** *"url:"* introduces the retrieval address in every entry — e.g. *"url: https://math.stackexchange.com/q/1703467"* in [1].
- **Time-stamp connector:** *"visited on"* introduces the access date in every entry — e.g. *"visited on 02/10/2020"* in [1].
- **Edition connector:** *"The Free Encyclopedia"* identifies the host publication — e.g. *"Wikipedia, The Free Encyclopedia. 2020."* in [8].
- **Subtitle/em-dash separator:** *" — "* joins a generic article to its host encyclopedia — e.g. *"Euler angles — Wikipedia"* in [8].

## How to Explain an Idea (replication steps)

The pattern this section relies on is **identity → artifact → edition → location → timestamp**, a citation-chaining pattern. It is an attribution pattern, not an argumentative one: it lets a reader retrace any source.

To cite a NEW web source using the same pattern:

1. **Identify the author.** Decide whether the source has an individual, a collective, or no named author. State it as the first element; if it is an individual or collective with a profile, append the profile URL in parentheses.
2. **Name the work.** Transcribe the exact title of the page, question, article, or video. End with a period.
3. **Stamp the edition (only for versioned sources).** For encyclopedias or documents with dated revisions, add the publication name plus the year. For a stable web page or a single forum post, skip this slot.
4. **Give the locator.** Begin with `url: ` and paste the full URL.
5. **Date the retrieval.** Append `(visited on DD/MM/YYYY)` in parentheses at the end. Use the date the page was actually opened.

Each step hands the reader the next piece of information they would need to re-trace the source: once they know who wrote it, they need to know what was written; once they know what, they need to know which version; once they know the version, they need to know where to find it; once they know where, they need to know the link was live on the date claimed.
