---
name: schedule-to-linkedin
description: Schedule or correct an approved English LinkedIn post and verify its saved formatting. Use the next Monday, Wednesday, or Friday slot at 9:30 AM Brasília time for new posts.
---

# Schedule a LinkedIn post

## Choose the post and slot

1. Use the approved English text in `posts/<topic-slug>/post.txt` and the media selected for that post, such as `image.gif` or `image.png`. Use the post identified by the request or the conversation. Resolve any ambiguity about the post or media before submitting.
2. Open [LinkedIn's composer](https://www.linkedin.com/sharing/compose) in the requested browser. Open the clock control and then the Scheduled tab. Read the scheduled posts and their dates before choosing a slot. Use the latest scheduled date across the list, including any additional pages. If the same post is already scheduled, report its existing date and time. For a requested correction, edit the matching entry in place and keep its date, time, and media unless the user requests a change.
3. Schedule on **Monday, Wednesday, or Friday at 9:30 AM Brasília time** (`America/Sao_Paulo`). Choose the first eligible future slot on a date strictly after the latest scheduled post, even if earlier dates are empty. If the list is empty, choose the earliest eligible future slot the scheduler accepts, including today if possible. Allow one post per Brasília calendar date. Use Brasília dates for all comparisons and convert the selected date and time if the scheduler displays another time zone.

## Prepare the composer

1. Prepare a plain-text copy. Strip Markdown syntax while retaining heading text, emphasized text, list items in order, and all code inside inline markers or fences. Keep link labels and destinations as plain text and use the URL once if it also serves as the label. Preserve meaningful literal characters such as JavaScript operators, punctuation, and LinkedIn hashtags.
2. Paste the English text one paragraph at a time. Press Enter twice between paragraphs so the editor contains an empty paragraph block between them. Keep intentional line breaks within lists and code. A single multiline paste can look correct in the editor because of margins between blocks, while LinkedIn saves only one line break. When DOM inspection is available, check the actual empty blocks before submitting.
3. Attach the selected media by absolute path using the browser tool's supported file upload API. If the tool offers a direct file-input setter, use it. In Codex browser control, register `tab.playwright.waitForEvent("filechooser")` before clicking Media, which can open the chooser immediately, then call `chooser.setFiles(absolutePath)`. This supplies the file programmatically. Use the native file picker only if the browser tool cannot supply the file by path. Finish any separate media editor and verify the attachment in the composer.

## Schedule and verify

1. Set the date and time in the scheduler and compare the preview with the intended Brasília slot. If the queue has changed during preparation, recompute the slot from the current Scheduled list before submitting.
2. Use Schedule and reopen the Scheduled list. Verify the matching post's date, time, media, paragraph order, and one visible blank line between paragraphs in the saved preview. Where DOM inspection is available, check for two rendered line breaks (`<br><br>` in the current preview) or an equivalent empty block. If spacing collapsed, edit the existing entry, insert the missing empty blocks, save, and verify the saved preview again. If the result is unclear, check the list before retrying to avoid a duplicate.
3. Report the confirmed date and time in Brasília and mention any unresolved issue with the upload, formatting, or confirmation.
