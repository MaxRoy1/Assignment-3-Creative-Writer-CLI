from google import genai

client = genai.Client()


def generate_text(prompt, max_tokens):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
        config={
            "system_instruction": """
You are a creative professional writer.
Follow the user's requested subject, format, audience, and tone.
Produce original and engaging writing.
Avoid unnecessary repetition.
""",
            "max_output_tokens": max_tokens,
        },
    )

    return response.text


def main():
    print("Creative Writer - Gemini")

    request = input("What would you like me to write? ").strip()

    if not request:
        print("Please provide a writing request.")
        return

    try:
        max_tokens = int(
            input("Maximum output tokens [500]: ") or "500"
        )
    except ValueError:
        print("Invalid value. Using 500 tokens.")
        max_tokens = 500

    for i in range(3):
        try:
            result = generate_text(request, max_tokens)

            print(f"\n--- Version {i + 1} ---")
            print(result)

        except Exception as error:
            print(f"\nVersion {i + 1} failed: {error}")


if __name__ == "__main__":
    main()