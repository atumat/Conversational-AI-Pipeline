"""
Context-aware response generation via the Anthropic API.
Keeps conversation history so follow-ups have context, and streams
the response so TTS can start on the first finished sentence instead
of waiting for the whole reply (this is what makes it feel "real-time").
"""
import re
from typing import Callable, List, Dict
from anthropic import Anthropic

client = Anthropic()
MODEL = "claude-sonnet-4-6"

SYSTEM_PROMPT = (
    "You are a helpful voice assistant. Keep responses concise and "
    "conversational — you are being read aloud by a TTS engine, so "
    "avoid bullet points, markdown, or anything that doesn't sound "
    "natural when spoken."
)

SENTENCE_END_RE = re.compile(r"(?<=[.!?])\s+")


class Conversation:
    def __init__(self) -> None:
        self.history: List[Dict[str, str]] = []

    def respond_streaming(
        self, user_text: str, on_sentence_complete: Callable[[str], None]
    ) -> str:
        """
        Streams the model's reply, firing on_sentence_complete(sentence)
        each time a full sentence is ready — so the caller can kick off
        TTS immediately instead of waiting for the full response.
        Returns the full response text for storing in history.
        """
        self.history.append({"role": "user", "content": user_text})

        full_reply = ""
        buffer = ""
        with client.messages.stream(
            model=MODEL,
            max_tokens=500,
            system=SYSTEM_PROMPT,
            messages=self.history,
        ) as stream:
            for chunk in stream.text_stream:
                buffer += chunk
                full_reply += chunk
                parts = SENTENCE_END_RE.split(buffer)
                if len(parts) > 1:
                    # everything except the last (possibly incomplete) part is done
                    for sentence in parts[:-1]:
                        if sentence.strip():
                            on_sentence_complete(sentence.strip())
                    buffer = parts[-1]

        if buffer.strip():
            on_sentence_complete(buffer.strip())

        self.history.append({"role": "assistant", "content": full_reply})
        return full_reply
