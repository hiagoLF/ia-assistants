---
name: create-linkedin-image
description: Generate or revise a minimalist English image for a LinkedIn programming post, using the project's purple diagonal gradient. Use when the user requests an actual post image, not just an image suggestion.
---

# Create a LinkedIn image

Read the selected topic's final `posts/<topic-slug>/post.txt` when available and use the image suggestion from the conversation. Do not require or save an image suggestion file. For legacy content without `post.txt`, read `post.md` and its image suggestion if available. When continuing the companion post skill's review workflow, wait until the user has validated the content and requested its English version before generating the image. If the user supplies image content directly, use that content. If neither the intended post nor image content can be identified, ask for the missing topic or content in the user's language.

## Visual requirements

- Create an image for a LinkedIn programming post with a minimalist style.
- Use a diagonal gradient from `#64559A` to `#836C8B` as the background.
- Use a square composition, targeting 1200 × 1200 pixels for the final asset when supported by the generation tool.
- The final result must be entirely in English, including all headings, labels, captions, and code comments. Preserve programming syntax and API identifiers.
- Show the supplied content with a clear hierarchy, readable typography, ample whitespace, and sufficient contrast against the gradient.
- Avoid unnecessary icons and decorative elements that detract from the minimalist style.
- Include short, accurate code only when it helps explain the concept. Favor one clear idea over a dense screenshot or a full tutorial.

## Generate and deliver

Use the available image-generation tool and follow its applicable image-generation instructions. Include the exact English copy and any exact code in the generation prompt. Generate the image itself, rather than returning only a prompt or suggestion.

Save the final image as `posts/<topic-slug>/image.png`, alongside its post. For an image-only request, create the topic folder without inventing an unrequested post. Preserve an existing image unless a revision was requested; save additional variants with descriptive names in the same folder.

Inspect the generated image before delivering. Check English-only text, spelling, code accuracy, readability, gradient, and consistency with the post. Correct defects before handing it over. If the target dimensions are unsupported, report the actual dimensions without claiming an exact size.

Show the final image and link to the saved file. Keep the accompanying interaction in the user's language.
