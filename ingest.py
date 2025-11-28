from __future__ import annotations

from email import policy
from email.parser import BytesParser
from typing import Iterable, Tuple
import pathlib
import re


def _strip_html(html: str) -> str:
    html = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", html)
    html = re.sub(r"(?i)<br\s*/?>", "\n", html)
    html = re.sub(r"(?i)</p>", "\n", html)
    html = re.sub(r"(?s)<.*?>", "", html)
    html = (html.replace("&nbsp;", " ")
                 .replace("&amp;", "&")
                 .replace("&lt;", "<")
                 .replace("&gt;", ">")
                 .replace("&quot;", '"'))
    html = re.sub(r"[ \t]+", " ", html)
    html = re.sub(r"\s*\n\s*", "\n", html).strip()
    return html


def _best_body(msg) -> str:
    if msg.is_multipart():
        for part in msg.walk():
            if (part.get_content_type() or "").lower() == "text/plain":
                return part.get_content()
        for part in msg.walk():
            if (part.get_content_type() or "").lower() == "text/html":
                return _strip_html(part.get_content())
        for part in msg.walk():
            if (part.get_content_type() or "").lower().startswith("text/"):
                return part.get_content()
        return ""
    else:
        ct = (msg.get_content_type() or "").lower()
        content = msg.get_content() or ""
        return _strip_html(content) if ct == "text/html" else content


def load_eml_texts(cy_dir: pathlib.Path | str) -> Iterable[Tuple[pathlib.Path, str]]:
    cy_path = pathlib.Path(cy_dir)
    for p in sorted(cy_path.glob("*.eml")):
        with p.open("rb") as f:
            msg = BytesParser(policy=policy.default).parse(f)
        subject = msg.get("subject", "") or ""
        sender = msg.get("from", "") or ""
        date = msg.get("date", "") or ""
        body = _best_body(msg)
        unified = f"From: {sender}\nDate: {date}\nSubject: {subject}\n\n{body}".strip()
        yield p, unified
