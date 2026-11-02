# Project rules

- Draft posts and image suggestions in the user's language (Portuguese by default) for review. After validation and the user's request, adapt both to natural English. Final posts and generated image text must be in English. Skills may also be written in English.
- Interact with the user in their language; Portuguese is welcome.
- Store each post and its images together in `posts/<topic-slug>/`, using a descriptive English kebab-case topic slug, such as `javascript-filter`.
- Keep review drafts and all image suggestions only in the chat; do not save them to files. Save only the final English post as `post.txt`, containing only the post in plain text with appropriate line breaks, without Markdown or workflow instructions. Save the final generated image as `image.png`, and create it only when requested.
- For a new post on an existing topic, use a distinct descriptive slug. Preserve existing content unless the user requests an update.
- Use `.agents/skills/create-linkedin-post/SKILL.md` for writing posts and `.agents/skills/create-linkedin-image/SKILL.md` for generating images.
- Default to practical JavaScript, TypeScript, React, and React Native topics for beginner and intermediate developers; follow other requested programming topics.
- Use a clear, direct, educational voice. Keep content original and technically accurate; never invent personal experiences, achievements, statistics, or engagement guarantees.
