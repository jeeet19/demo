import collections

class MovieGraph:
    def __init__(self):
        self.graph = collections.defaultdict(list)

    def add_movie(self, movie, actors):
        # For each movie, add a connection between all pairs of actors
        for i in range(len(actors)):
            for j in range(i + 1, len(actors)):
                self.graph[actors[i]].append((actors[j], movie))
                self.graph[actors[j]].append((actors[i], movie))

    def find_degrees_of_separation(self, start_actor, end_actor):
        # Use BFS to find the shortest path
        visited = set()
        queue = collections.deque([(start_actor, [])])

        while queue:
            actor, path = queue.popleft()
            if actor == end_actor:
                return path

            if actor not in visited:
                visited.add(actor)
                for neighbor, movie in self.graph[actor]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [(actor, neighbor, movie)]))
        return None


def load_data():
    # Simulate loading data from a file or database
    # Add movie data: each movie is associated with a list of actors
    graph = MovieGraph()

    graph.add_movie("Harry Potter and the Order of the Phoenix", ["Emma Watson", "Brendan Gleeson", "Daniel Radcliffe", "Rupert Grint"])
    graph.add_movie("Trespass Against Us", ["Brendan Gleeson", "Michael Fassbender", "Lindsay Duncan"])
    graph.add_movie("X-Men: First Class", ["Michael Fassbender", "Jennifer Lawrence", "James McAvoy", "Kevin Bacon"])

    return graph


def print_degrees_of_separation(path):
    if path:
        print(f"{len(path)} degrees of separation.")
        for i, (actor1, actor2, movie) in enumerate(path, start=1):
            print(f"{i}: {actor1} and {actor2} starred in {movie}")
    else:
        print("No connection found.")


if __name__ == "__main__":
    print("Loading data...")
    movie_graph = load_data()
    print("Data loaded.")

    # Set start and end actors
    start_actor = "Emma Watson"
    end_actor = "Jennifer Lawrence"

    # Find the degrees of separation
    print(f"Finding degrees of separation between {start_actor} and {end_actor}...")
    path = movie_graph.find_degrees_of_separation(start_actor, end_actor)

    # Print the degrees of separation
    print_degrees_of_separation(path)
