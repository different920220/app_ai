# server.py
import multiprocessing
import time
import logging


class Server:
    """
    A basic Server class that handles starting, stopping, and managing
    the multiprocessing environment.
    """

    def __init__(self, num_workers: int = 4):
        """
        Initializes the Server with the specified number of workers.

        :param num_workers: The number of workers to manage (default is 4).
        """
        self.num_workers = num_workers
        self.processes = []
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def start(self):
        """
        Starts the server by initializing and starting the worker processes.
        """
        self.logger.info(f"Starting server with {self.num_workers} workers.")
        for i in range(self.num_workers):
            p = multiprocessing.Process(target=self.worker_function, args=(i,))
            p.start()
            self.processes.append(p)

        self.logger.info("Server started with workers.")

    def worker_function(self, worker_id: int):
        """
        This is the function each worker will run. For now, it just sleeps
        and logs a message, simulating work.

        :param worker_id: The identifier for the worker.
        """
        self.logger.info(f"Worker {worker_id} started.")
        time.sleep(10)  # Simulate some work being done
        self.logger.info(f"Worker {worker_id} finished.")

    def stop(self):
        """
        Stops the server by terminating all worker processes.
        """
        self.logger.info("Stopping server.")
        for p in self.processes:
            p.terminate()
            p.join()  # Wait for each process to finish

        self.logger.info("Server stopped.")

    def restart(self):
        """
        Restarts the server by stopping and starting again.
        """
        self.stop()
        self.start()

    def status(self):
        """
        Returns the status of the server and its workers.
        """
        active_processes = [p.is_alive() for p in self.processes]
        return {
            "num_workers": self.num_workers,
            "active_workers": sum(active_processes),
            "total_workers": len(self.processes),
        }
