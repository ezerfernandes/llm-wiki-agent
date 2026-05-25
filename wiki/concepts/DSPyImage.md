---
title: "dspy.Image"
type: concept
tags: [dspy, primitive, image, multimodal, vision]
sources: [dspy-image-generation-prompting-tutorial]
last_updated: 2026-05-24
---

# dspy.Image

`dspy.Image` is [[DSPy]]'s first-class **image primitive** — the type used inside [[DSPySignatures|Signatures]] to declare image-bearing `InputField`s. **First wiki receipt: [[dspy-image-generation-prompting-tutorial]]** (the dspy.ai *Image Generation Prompt Iteration* tutorial) declares the type inline in a string-spec [[DSPyPredict|`dspy.Predict`]] (`"... current_image: dspy.Image ..."`) and feeds it [[FluxPro|Flux Pro]] image URLs hosted by [[FAL]].

Structural sibling to [[DSPyAudio|`dspy.Audio`]] in the wiki's multimodal-primitive taxonomy; the two non-text primitives use **opposite transport disciplines** (see *Transport* below).

## Construction paths

| Path | Source data | Use case |
|---|---|---|
| `dspy.Image.from_url(url)` | A hosted HTTPS URL (e.g. `fal.media/files/.../*.jpg`) | The path exercised by [[dspy-image-generation-prompting-tutorial]] — image generator returns a URL; wrap the URL without re-downloading bytes. |
| `dspy.Image.from_file(path)` / `dspy.Image(...)` | Local file / base64-encoded bytes | Documented in the [[DSPyPrimitives|primitives surface]] (Image primitive entry in the API reference); not exercised by the first wiki receipt. Forward reference. |

The instance exposes `.url` as a public attribute usable for client-side downloads after construction (the tutorial's `display_image(image)` helper does `requests.get(image.url)`).

## Transport — URL passthrough vs base64

The load-bearing structural disclosure from [[dspy-image-generation-prompting-tutorial]]: **`dspy.Image` constructed via `from_url(...)` serializes through the [[DSPyAdapters|Adapter]] as URL passthrough, not base64 inlining**. The `dspy.inspect_history(...)` excerpt shows the wire shape as:

```
[[ ## current_image ## ]]
<image_url: https://fal.media/files/panda/HLKaiKFc_sN_fwBBN1C_2_1d1a72732e294452afb056a26d6b6c96.jpg>
```

i.e. the chat-completion request carries the URL string verbatim. The LM's vision modality reads the URL on its side, not locally-downloaded bytes.

**Contrast with [[DSPyAudio|`dspy.Audio`]]**, which stores its audio as base64-encoded WAV bytes in `data` and ships those bytes in the request payload. The two non-text primitives use **opposite transport disciplines** — `dspy.Image` favors URL passthrough (the common image-hosting case), `dspy.Audio` favors base64 inlining (the common HuggingFace-dataset-load case where audio arrives as a NumPy array).

## Modality-axis status

- **InputField (image-in)**: supported end-to-end via vision-capable LMs ([[GPT4oMini|`gpt-4o-mini`]] in [[dspy-image-generation-prompting-tutorial]]; any [[LiteLLM]]-supported vision model is expected to compose). The [[DSPyAdapters|Adapter]] handles the URL-passthrough wire shape.
- **OutputField (image-out)**: **not** first-class — [[dspy-image-generation-prompting-tutorial]] generates images via the [[FAL]] HTTP API (`fal_client.submit(...)` → `fal_client.result(...)`) **outside** the DSPy `LM` abstraction and wraps the returned URL into `dspy.Image.from_url(...)` for *input* on the next iteration. DSPy's LM client does not multiplex image-output endpoints. Symmetric to [[DSPyAudio|`dspy.Audio`]]'s "no first-class output" disclosure in [[dspy-audio-tutorial]].

## String-Signature parser support

`dspy.Image` is recognized **inline in string-spec Signatures** by the string-Signature parser:

```python
check_and_revise_prompt = dspy.Predict(
    "desired_prompt: str, current_image: dspy.Image, current_prompt:str "
    "-> feedback:str, image_strictly_matches_desired_prompt: bool, revised_prompt: str"
)
```

First wiki receipt of `dspy.Image` (and by symmetry `dspy.Audio`) named inline in a string Signature — prior receipts ([[dspy-signatures]], [[dspy-modules]]) showed only primitive Python types (`str`/`bool`/`int`/`list[str]`) in string-spec form. The string-Signature parser resolves the `dspy.` namespace prefix as a typed field reference rather than treating it as a generic-type string.

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-conversation-history]] — cross-reference receipt: positions `dspy.Image` as the **tier-five DSPy-special-type sibling** of [[DSPyHistory|`dspy.History`]] in the [[DSPySignatures|Signatures]] page's five-tier type system; no end-to-end image program, but the type-system mapping is the cleanest forward-reference receipt prior to the minting tutorial.
- [[dspy-image-generation-prompting-tutorial]] — minting tutorial; first wiki receipt of `dspy.Image.from_url(url)` as a construction path, of **URL-passthrough Adapter serialization** (chat-completion wire shape `<image_url: https://fal.media/files/.../*.jpg>` visible in `dspy.inspect_history(5)` — not base64 inlining), and of `dspy.Image` named **inline in a string-spec [[DSPyPredict|`dspy.Predict`]] Signature** (`"... current_image: dspy.Image ..."`) — proves the string-Signature parser resolves the `dspy.` namespace as typed field reference. The end-to-end loop: [[FluxPro|Flux Pro v1.1 Ultra]] via [[FAL]] returns a hosted URL → `dspy.Image.from_url(...)` → fed into a critic-then-revise [[DSPyPredict|`dspy.Predict`]] backed by [[GPT4oMini|`gpt-4o-mini`]] vision.
- [[dspy-saving-tutorial]] — cross-reference receipt: names `dspy.Image` as the **canonical non-JSON-serializable Signature field** that forces the pickle fallback (`.pkl` extension on state-only saves with `allow_pickle=True`) or the whole-program `cloudpickle` path — i.e. `dspy.Image` is the load-bearing example for *why* the JSON/pickle/whole-program three-mode persistence surface exists at all.

## Connections

- [[DSPy]] / [[DSPySignatures]] / [[DSPyPredict]] / [[DSPyAdapters]] — the primitive composes into the standard DSPy programming model.
- [[DSPyAudio]] — sibling non-text primitive; opposite transport discipline (base64 in `data` vs URL passthrough in `dspy.Image`).
- [[GPT4oMini]] — vision-capable LM compatible with `dspy.Image` InputFields in the first wiki receipt.
- [[FluxPro]] — the image-generation model whose output URLs are wrapped via `dspy.Image.from_url(...)` in [[dspy-image-generation-prompting-tutorial]].
- [[FAL]] — the hosting service whose `result["images"][0]["url"]` is the URL source for `from_url(...)` in the first wiki receipt.
- [[MultimodalLLM]] — broader concept; vision-LM with `dspy.Image` InputField is one instance of the family.
- [[DSPySaving|`dspy.Image` triggers pickle fallback in `program.save(...)`]] — the [[dspy-saving-tutorial|Saving tutorial]] names `dspy.Image` as the canonical example of a non-JSON-serializable Signature field that forces `.pkl` extension on state-only saves.
- [[dspy-image-generation-prompting-tutorial]] — first wiki receipt.
