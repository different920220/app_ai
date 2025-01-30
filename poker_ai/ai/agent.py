import multiprocessing as mp
import os
from pathlib import Path
from typing import Callable, Optional, Union

import joblib


# Move manager initialization into method scope to avoid issues during setup.py processing
class Agent:
    """
    Create agent, optionally initialise to agent specified at path.

    ...

    Attributes
    ----------
    strategy : Dict[str, Dict[str, int]]
        The preflop strategy for an agent.
    regret : Dict[str, Dict[strategy, int]]
        The regret for an agent.
    """

    def __init__(
            self,
            agent_path: Optional[Union[str, Path]] = None,
            use_manager: bool = True,
    ):
        """Construct an agent."""
        # Don't use manager if we are running tests.
        testing_suite = bool(os.environ.get("TESTING_SUITE", False))
        use_manager = use_manager and not testing_suite

        # Initialize manager here instead of at the module level.
        if use_manager:
            self.manager = mp.Manager()
            dict_constructor: Callable = self.manager.dict
        else:
            self.manager = None
            dict_constructor: Callable = dict

        self.strategy = dict_constructor()
        self.regret = dict_constructor()
        if agent_path is not None:
            saved_agent = joblib.load(agent_path)
            # Assign keys manually because I don't trust the manager proxy.
            for info_set, value in saved_agent["regret"].items():
                self.regret[info_set] = value
            for info_set, value in saved_agent["strategy"].items():
                self.strategy[info_set] = value


if __name__ == '__main__':
    # Example: Create Agent object and perform necessary actions.
    agent = Agent(agent_path="path_to_agent_data")
    # You can call any methods you need from Agent here.
    # Example: agent.some_method()
