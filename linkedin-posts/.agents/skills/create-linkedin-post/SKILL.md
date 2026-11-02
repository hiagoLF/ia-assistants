---
name: create-linkedin-post
description: Draft or revise an original LinkedIn programming post and image suggestion in chat for review, then adapt them to natural English when requested after validation. Save only the final English post as plain text; this skill does not generate images.
---

# Create a LinkedIn post

Use the requested programming topic. If no topic is available from the request or conversation, ask for it in the user's language. Default to beginner and intermediate developers, with a focus on JavaScript, TypeScript, React, and React Native when choosing an angle.

## Language and review workflow

1. First write the post and the image suggestion in the user's language, defaulting to Portuguese when no preference is known. Preserve programming syntax and API identifiers.
2. Present both only in the chat for review; do not save drafts or image suggestions to files. Invite the user to validate or request changes in the conversation. Apply requested revisions in the review language, keeping them in the chat.
3. Wait for the user to validate the content and request the English version before adapting it. Validation alone does not trigger translation. If the user has already validated the content and requested English in the conversation, proceed without asking again.
4. Adapt both the post and the image suggestion to natural, idiomatic English. Preserve the approved meaning and technical details, avoiding literal translations and invented claims. Save only the final English post as `post.txt` and link to it. Present the English image suggestion only in the chat.

## Post

- Write the review draft in the review language and the final English version entirely in English.
- Use at most 300 words for each version of the post, including any hashtags or code. The separate image suggestion is outside this limit.
- Make it engaging and easy to scan: a compelling, truthful opening, short paragraphs, a practical explanation, and a relevant closing question that invites discussion.
- Use a direct, educational tone. Avoid clickbait, forced engagement prompts, and promises of reach.
- Prefer placing code in the suggested image. When code is necessary in the post, keep it brief and readable as plain text, without backticks or code fences.
- Create original wording, examples, and framing. Do not copy or closely paraphrase another author's post. Do not claim that uniqueness has been exhaustively verified.
- Do not invent the user's personal experiences, outcomes, metrics, or quotations.
- Verify technical claims against official documentation when uncertain or version-dependent. Keep source notes separate from the publishable text when needed.

## Image suggestion

Suggest one minimalist image only in the chat, in the same language and review stage as the post. Never save the suggestion to a file, including its final English version. Describe only its content: the headline, labels, code, or comparison to show. Adapt all proposed image text to English at the English stage, preserving programming syntax and API identifiers. Do not discuss format, dimensions, background, or colors here. Keep the content brief enough to read at a glance.

Do not generate an image as part of this skill. If the user also requests image generation, use the companion `create-linkedin-image` skill after completing the English post and image suggestion.

## Save and review

Save only the final English post to `posts/<topic-slug>/post.txt`, using a descriptive English kebab-case slug. Do not create files or topic folders during the chat-only review stage. Preserve existing posts unless an update was requested; use a distinct slug for a new post on an existing topic.

- `post.txt` must contain only the final English post text. Never include instructions, review requests, status labels, source notes, image suggestions, or a wrapper heading such as "Post".
- Use plain text with line breaks and blank lines where needed for post copy and image suggestions, including in the chat. Do not use Markdown formatting such as headings, bold, Markdown lists, links, backticks, or code fences within that content. Ordinary hashtags remain allowed.
- Do not create `post.md` or `image-suggestion.txt`. When explicitly updating a legacy `post.md`, save only the final revised English post as `post.txt`; preserve the legacy file unless its removal was requested.

Before delivering either stage, count the words in the post, check technical accuracy and the stage's language, and confirm that the suggestion matches the post. Before saving the final English post, inspect it for plain-text formatting and content separation. Respond in the user's language and link to `post.txt` only after saving the final version. Keep explanations, validation requests, source notes, image suggestions, and next steps in the chat, separate from the post copy.
