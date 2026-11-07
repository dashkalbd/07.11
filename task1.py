from collections import deque


class Queue:
    def __init__(self):
        self.requests = deque()
        self.next_number = 1
        self.processed = 0

    # 1. add a new request
    def add_request(self, name, topic, description):
        request = {
            "number": self.next_number,
            "name": name,
            "topic": topic,
            "description": description
        }
        self.requests.append(request)
        print(f"Request #{self.next_number} added")
        self.next_number = self.next_number + 1

    # 2. look at the next request without removing it
    def show_next(self):
        if len(self.requests) == 0:
            print("Queue is empty")
        else:
            request = self.requests[0]
            print("Next request:")
            self.print_request(request)

    # 3. take the next request and remove it
    def process_next(self):
        if len(self.requests) == 0:
            print("Queue is empty, nothing to process")
        else:
            request = self.requests.popleft()
            self.processed = self.processed + 1
            print("Processing request:")
            self.print_request(request)

    # 4. show all waiting requests
    def show_all(self):
        if len(self.requests) == 0:
            print("Queue is empty")
        else:
            print("Waiting requests:")
            for request in self.requests:
                self.print_request(request)

    # 5. number of requests in the queue
    def show_count(self):
        print(f"Requests in queue: {len(self.requests)}")

    # 6. number of processed requests
    def show_processed(self):
        print(f"Processed requests: {self.processed}")

    # helper: print one request
    def print_request(self, request):
        print(f"#{request['number']} | {request['name']} | {request['topic']} | {request['description']}")


# 8. menu
def menu():
    queue = Queue()

    while True:
        print()
        print("1 - Add request")
        print("2 - Show next request")
        print("3 - Process next request")
        print("4 - Show all waiting requests")
        print("5 - Number of requests in queue")
        print("6 - Number of processed requests")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            name = input("Student name: ")
            topic = input("Topic: ")
            description = input("Problem description: ")
            queue.add_request(name, topic, description)
        elif choice == "2":
            queue.show_next()
        elif choice == "3":
            queue.process_next()
        elif choice == "4":
            queue.show_all()
        elif choice == "5":
            queue.show_count()
        elif choice == "6":
            queue.show_processed()
        elif choice == "0":
            print("Goodbye")
            break
        else:
            print("Wrong choice, try again")


menu()
