"""Simple watchlist management."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class Watchlist:
    """Store a list of symbols or sectors to watch."""

    symbols: List[str] = field(default_factory=list)

    def add(self, symbol: str) -> None:
        """Add a symbol to the watchlist if not already present."""
        if symbol not in self.symbols:
            self.symbols.append(symbol)

    def remove(self, symbol: str) -> None:
        """Remove a symbol from the watchlist."""
        if symbol in self.symbols:
            self.symbols.remove(symbol)

    def list(self) -> List[str]:
        """Return current watchlist."""
        return self.symbols
