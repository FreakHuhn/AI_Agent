import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
import prompts
from call_function import available_functions, call_function


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    
    
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_input", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_input)])]

    client = genai.Client(api_key=api_key)

    for _ in range(20):
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=prompts.system_prompt,
            ),
        )

        if response.usage_metadata is None:
            raise RuntimeError("Usage metadata is None - API request may have failed")

        candidates = response.candidates or []
        for candidate in candidates:
            if candidate.content:
                messages.append(candidate.content)

        function_calls = response.function_calls if response.function_calls else []
        function_results = []

        if function_calls:
            for function_call in function_calls:
                function_call_result = call_function(function_call, verbose=args.verbose)

                if not function_call_result.parts:
                    raise RuntimeError("Function call returned no parts")

                first_part = function_call_result.parts[0]
                func_response = first_part.function_response

                if func_response is None:
                    raise RuntimeError("Function response is missing")

                if func_response.response is None:
                    raise RuntimeError("Function response payload is missing")

                function_results.append(first_part)

                if args.verbose:
                    print(f"-> {func_response.response}")

            messages.append(types.Content(role="user", parts=function_results))
        else:
            if args.verbose:
                print(f"User prompt: {args.user_input}")
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            print(response.text)
            break
    else:
        print("Agent loop reached maximum iterations without producing a final response")


if __name__ == "__main__":
    main()
