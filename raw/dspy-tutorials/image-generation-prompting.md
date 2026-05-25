# Image Generation Prompt iteration

> Source: https://dspy.ai/tutorials/image_generation_prompting/
> Fetched: 2026-05-24

This is based off of a tweet from [@ThorondorLLC](https://x.com/ThorondorLLC) ([tweet link](https://x.com/ThorondorLLC/status/1880048546382221313)).

This will take an initial desired prompt, and iteratively refine it until the image generated matches the desired prompt.

This is not DSPy prompt optimization as it is normally used, but it is a good example of how to use multimodal DSPy.

A future upgrade would be to create a dataset of initial, final prompts to optimize the prompt generation.

## Install

```
pip install -U dspy
```

For this example, we'll use Flux Pro from FAL. You can get an API key at https://fal.com/flux-pro

We will also need to install Pillow and dotenv.

```
pip install fal-client pillow dotenv
```

## Imports / setup

```python
# Optional
#os.environ["FAL_API_KEY"] = "your_fal_api_key"
#os.environ["OPENAI_API_KEY"] = "your_openai_api_key"
```

```python
import dspy

from PIL import Image
from io import BytesIO
import requests
import fal_client

from dotenv import load_dotenv
load_dotenv()

# import display
from IPython.display import display

lm = dspy.LM(model="gpt-4o-mini", temperature=0.5)
dspy.configure(lm=lm)
```

## Helper functions

```python
def generate_image(prompt):

    request_id = fal_client.submit(
        "fal-ai/flux-pro/v1.1-ultra",
        arguments={
            "prompt": prompt
        },
    ).request_id

    result = fal_client.result("fal-ai/flux-pro/v1.1-ultra", request_id)
    url = result["images"][0]["url"]

    return dspy.Image.from_url(url)

def display_image(image):
    url = image.url
    # download the image
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))

    # display at 25% of original size
    display(image.resize((image.width // 4, image.height // 4)))
```

## Iteration loop

```python
check_and_revise_prompt = dspy.Predict(
    "desired_prompt: str, current_image: dspy.Image, current_prompt:str "
    "-> feedback:str, image_strictly_matches_desired_prompt: bool, revised_prompt: str"
)

initial_prompt = "A scene that's both peaceful and tense"
current_prompt = initial_prompt

max_iter = 5
for i in range(max_iter):
    print(f"Iteration {i+1} of {max_iter}")
    current_image = generate_image(current_prompt)
    result = check_and_revise_prompt(
        desired_prompt=initial_prompt,
        current_image=current_image,
        current_prompt=current_prompt,
    )
    display_image(current_image)
    if result.image_strictly_matches_desired_prompt:
        break
    else:
        current_prompt = result.revised_prompt
        print(f"Feedback: {result.feedback}")
        print(f"Revised prompt: {result.revised_prompt}")

print(f"Final prompt: {current_prompt}")
```

## Sample run (5 iterations, abridged)

```
Iteration 1 of 5
Feedback: The image depicts a peaceful autumn scene with people walking among colorful leaves, which aligns with the peaceful aspect of the prompt. However, it lacks any elements that convey tension, making it not fully representative of the desired prompt.

Iteration 2 of 5
Feedback: The image depicts a serene autumn scene with vibrant foliage and a calm river, which aligns well with the idea of peace. However, it lacks explicit elements that suggest underlying tension, making it less effective in conveying both aspects of the desired prompt.

Iteration 3 of 5
Feedback: The image depicts a serene autumn scene with warm colors and soft lighting, which aligns with the peaceful aspect of the desired prompt. However, it lacks elements that evoke tension or unease, making it not fully meet the requirement for a scene that is both peaceful and tense.

Iteration 4 of 5
(match — loop breaks)

Final prompt: A serene autumn scene with fog and shadows, capturing both peace and tension.
```

## `dspy.inspect_history(5)` excerpt

```
[2025-01-17T11:36:55.947579]

System message:

Your input fields are:
1. `desired_prompt` (str)
2. `current_image` (Image)
3. `current_prompt` (str)

Your output fields are:
1. `feedback` (str)
2. `revised_prompt` (str)
3. `image_strictly_matches_desired_prompt` (bool)

All interactions will be structured in the following way, with the appropriate values filled in.

[[ ## desired_prompt ## ]]
{desired_prompt}

[[ ## current_image ## ]]
{current_image}

[[ ## current_prompt ## ]]
{current_prompt}

[[ ## feedback ## ]]
{feedback}

[[ ## revised_prompt ## ]]
{revised_prompt}

[[ ## image_strictly_matches_desired_prompt ## ]]
{image_strictly_matches_desired_prompt}        # note: the value you produce must be True or False

[[ ## completed ## ]]

In adhering to this structure, your objective is:
        Given the fields `desired_prompt`, `current_image`, `current_prompt`, produce the fields `feedback`, `revised_prompt`, `image_strictly_matches_desired_prompt`.

User message:

[[ ## desired_prompt ## ]]
A scene that's both peaceful and tense

[[ ## current_image ## ]]
<image_url: https://fal.media/files/panda/HLKaiKFc_sN_fwBBN1C_2_1d1a72732e294452afb056a26d6b6c96.jpg>

[[ ## current_prompt ## ]]
A scene that's both peaceful and tense

Respond with the corresponding output fields, starting with the field `[[ ## feedback ## ]]`, then `[[ ## revised_prompt ## ]]`, then `[[ ## image_strictly_matches_desired_prompt ## ]]` (must be formatted as a valid Python bool), and then ending with the marker for `[[ ## completed ## ]]`.

Response:

[[ ## feedback ## ]]
The image depicts a calm café scene with two individuals engaged in conversation, which conveys a sense of peace. However, the woman's posture and expression suggest an underlying tension, as she appears to be contemplative or distressed. This duality aligns well with the desired prompt of being both peaceful and tense.

[[ ## revised_prompt ## ]]
A scene that captures the duality of peace and tension in a café setting.

[[ ## image_strictly_matches_desired_prompt ## ]]
True

[[ ## completed ## ]]
```

(Four additional run records appear in the rendered tutorial, all with the same Signature shape — `<image_url: https://fal.media/...>` is how `dspy.Image` serializes into the prompt's `current_image` slot, i.e. URL passthrough rather than base64 inlining.)
