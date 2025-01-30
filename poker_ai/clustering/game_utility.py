import numpy as np
from poker_ai.poker.card import Card
import sys
import importlib

if "poker_ai.poker.hand_evaluator" in sys.modules:
    importlib.reload(sys.modules["poker_ai.poker.hand_evaluator"])

from poker_ai.poker.hand_evaluator import HandEvaluator

class GameUtility:
    def __init__(self, board: np.ndarray, our_hand: np.ndarray):
        self.board = board
        self.our_hand = our_hand
        self._evaluator = HandEvaluator()

    def evaluate_hand(self, hand, board):
        """
        Evaluates the hand and returns the hand rank information.

        Parameters
        ----------
        hand : np.ndarray
            The hand (hole cards) of the player.

        Returns
        -------
        dict
            The result containing hand strength (rank) and other relevant details.
        """
        # Replace np.int with int (Python's built-in int)
        return self._evaluator.evaluate(
            board=self.board.astype(int).tolist(),  # Use Python's built-in int
            cards=hand.astype(int).tolist(),       # Use Python's built-in int
        )

    def get_winner(self) -> int:
        """
        Determine the winner between two hands on the board.

        Returns
        -------
        int
            Index of the winning hand (either 0 or 1 depending on the winner).
        """
        # Evaluate both hands (our hand vs opponent's hand)
        our_hand_rank = self.evaluate_hand(self.our_hand, self.board)
        # opponent_hand_rank = self.evaluate_hand(self.board, self.board)
        opponent_hand_rank = self.evaluate_hand(self.board, self.our_hand)

        # Logic to determine the winner based on hand ranks.
        if our_hand_rank["rank"] > opponent_hand_rank["rank"]:
            return 0  # Our hand is better
        elif our_hand_rank["rank"] < opponent_hand_rank["rank"]:
            return 1  # Opponent's hand is better
        else:
            return -1  # It's a tie (same rank)

# Usage Example:
# game = GameUtility(board=np.array([...]), our_hand=np.array([...]))
# winner = game.get_winner()
