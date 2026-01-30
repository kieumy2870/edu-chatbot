"""Database module for caching math problem solutions.

This module provides functions for initializing, reading from, and writing to
a SQLite database that caches math problem solutions.
"""
import hashlib
import sqlite3
from typing import Optional


def get_db_connection() -> sqlite3.Connection:
    """Establish and return a database connection.

    Returns:
        sqlite3.Connection: Database connection with Row factory.
    """
    conn = sqlite3.connect("math_cache.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """Initialize the database with required tables.

    Creates the math_cache table if it doesn't exist.
    """
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS math_cache (
            id_hash TEXT PRIMARY KEY,
            input_text TEXT,
            response TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def generate_hash(text: Optional[str], image_bytes: Optional[bytes] = None) -> str:
    """Generate a unique hash for the given text and optional image.

    Args:
        text: Input text to hash.
        image_bytes: Optional image bytes to include in hash.

    Returns:
        str: MD5 hash hexadecimal string.
    """
    hasher = hashlib.md5((text or "").encode())
    if image_bytes:
        hasher.update(image_bytes)
    return hasher.hexdigest()


def get_cached_response(id_hash: str) -> Optional[str]:
    """Retrieve a cached response by hash.

    Args:
        id_hash: The hash identifier for the cached response.

    Returns:
        Optional[str]: The cached response or None if not found.
    """
    conn = get_db_connection()
    row = conn.execute(
        "SELECT response FROM math_cache WHERE id_hash = ?", (id_hash,)
    ).fetchone()
    conn.close()
    return row["response"] if row else None


def save_to_cache(id_hash: str, text: Optional[str], response: str) -> None:
    """Save a response to the cache.

    Args:
        id_hash: The hash identifier for this cache entry.
        text: The input text that was processed.
        response: The generated response to cache.
    """
    try:
        conn = get_db_connection()
        conn.execute(
            "INSERT OR REPLACE INTO math_cache (id_hash, input_text, response) "
            "VALUES (?, ?, ?)",
            (id_hash, text, response),
        )
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Lỗi lưu cache: {e}")