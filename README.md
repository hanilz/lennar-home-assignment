# lennar-home-assignment
This repository serves as the submission of the package truck loading problem home assignment

## Important Note
I wasn't able to complete the main logic of the assignment, but I was able to build a working FastAPI backend service
with a local SQLite DB schema.

I managed to create basic API routes (get and get_by_id), but didn't manage to complete the main logic of the assignment 
(although I have it figured out). 

## Assignment
You have a warehouse that stores various packages. 

Each package has dimensions (length, width, height). 

When it’s time to ship these packages, they need to be loaded onto trucks—each truck also has dimensions that represent its cargo space.

Your system must:
1. Model and store these trucks and packages.
2. Decide if a set of packages can fill a truck to at least 80% of its total volume. If it can’t
reach 80%, the system delays shipment until the following day.
3. (Optional Bonus) Use bin packing techniques to more accurately assess how packages
might be arranged in a truck, rather than relying solely on volume checks.

## Design Process
*This is me typing while thinking*
### Thoughts
- It's obvious that the truck data model will be composed from multiple packages (in a List probably).
- I'll need to create a delayed packages warehouse for any package that wasn't able to fill up a truck.
  - When filling a new truck, first get the delayed packages and then the new ones.


### Data Models
The Package data model will include:
- id: int
- height: float
- width: float
- depth: float
- volume: float
- is_shipped: float

The Truck data model will include:
- Fields:
  - id: int
  - height: float
  - width: float
  - depth: float
  - packages: list[Package]
  - containable_volume: float
  - filled_volume: float
- Functions:
  - load_package(package: Package) -> bool
  - load_packages(packages: list[Packages]) -> bool
  - is_truck_filled() -> bool
  - delay_packages(packages: list[Package])

Utils:
- calculate_volume(height: double, width: double, depth: double) -> double

I'll need to address the issues involving:
- Invalid height, width and depth packages and trucks.
- Trying to load packages that are larger than the truck in one of the dimensions (height, width or depth).
- Trying to load a package that it's volume is larger than the truck's filled volume.
- Delaying all packages that can't fill a truck to at least 80% to the next day.

## Endpoints
/package
- get
  - all 
  - by id
  - all shipped (?)
- put (create new)
  - require height, width, depth

/truck
- get
  - all
  - by id
  - shipped (If I have time)
  - not shipped (If I have time)
- put (create new)
  - require height, width, depth

/load (or add to truck)
- post
  - assign truck
    - List of packages as input.
    - Check all trucks to see which one fits the best to the list of packages. 

## Tech Stack
- FastAPI for backend
  - Easy to get going in the time constraint while also providing a Swagger documentation of the API.
- Pydantic for data type modeling
- SQLite for the database
  - Fast and easy database to get it going
- Docker and docker-compose if I'll have time to package it.
  - Lets anyone run the application fast and easy.

## Running the App
### locally
1. Clone Git Repository and cd into it:
```bash
git clone https://github.com/hanilz/lennar-home-assignment.git && cd lennar-home-assignment 
```

2. Install the requirements from requirements.txt:
```bash
pip3 install -r requirements.txt
```

3. Run the FastAPI app on port 8000:
```bash
fastapi dev app.py
```

## Docs
After running the app, you can access the docs using via http://127.0.0.1:8000/docs

## Resources Used:
1. Pydantic docs: https://docs.pydantic.dev/latest/
2. SQLite3 docs: https://docs.python.org/3/library/sqlite3.html
3. FastAPI docs: https://fastapi.tiangolo.com/
4. Google search

## Tools Used
- PyCharm IDE
- SQLite viewer: db-browser-for-sqlite