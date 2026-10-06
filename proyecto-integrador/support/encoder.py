"""Small typed adapter around Sentence Transformers."""

from collections.abc import Sequence
from typing import Any, Protocol

import numpy as np
import numpy.typing as npt
from sentence_transformers import SentenceTransformer

FloatMatrix = npt.NDArray[np.float32]


class TextEncoder(Protocol):
    def encode(self, texts: Sequence[str], batch_size: int) -> FloatMatrix:
        """Return one normalized row per input text."""


class SentenceEncoder:
    """Encode English text with the configured pretrained model."""

    def __init__(self, model_name: str, device: str) -> None:
        self._model: Any = SentenceTransformer(model_name, device=device)

    def encode(self, texts: Sequence[str], batch_size: int) -> FloatMatrix:
        if not texts:
            raise ValueError("At least one text is required")
        encoded = self._model.encode(
            list(texts),
            batch_size=batch_size,
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=False,
        )
        matrix = np.asarray(encoded, dtype=np.float32)
        if matrix.ndim != 2 or matrix.shape[0] != len(texts):
            raise ValueError("The encoder returned an unexpected matrix shape")
        return matrix
