# The Story of Node

2009

- Node
- [Febryary 2009] MongoDB - NoSQL database

2010

- NPM

2011

- Mongoose
- ExpressJS
- AngularJS

2015 

- First no-beta release

# What is v8, exactly?

The chrome V8 Javascripot engine.

Modern computers only understands machine code. Instead of writing machine code, most devs write in high level languages.

In order to execute high level code, the computers use:

- Interpreters
- Compilers
- Transpilars

# What is Node.js exactly?

Nodejs was written in C++ to embbed V8 engine. It's really hard manipulater V8 itself. Nodejs facilities it for yout.

V8 its like a car engine, Nodeje is everything else on the car, and the developer is a driver.

Nodejs now presents itself as two applications:

- **A script processor**: ``node {spript name}`` initialize the process called the **event loop** (its a process the execute continually checking if there's any new task for Node.js to do).
  - Non-blocking tasks get added to the todolist, and Node proceses them whenever it can
  - Nodejs has a single thread
  - Node's event loop and non blocking IO don't allow Node to do multiple things at one time, they just allow Node to schedule things later.
  - When processing a request, most web apps are actually sitting around waiting for most the time.
  - A Non blocling IO allows an app to do other things while it's sitting around waitng.
- **A REPL (Read Eval Print Loop)**: 

A Nodejs applications don't specitfy all files of the application, just the entiry file.

To read the content of a file by another file, we use `var lib = require("./lib")`, this statement get the content from the file *lib* and put it inside the variable **lib**.

Similary, to especify the peace of code to be used for another file we use `module.exports = whatever` 

In summary: Node's script processor do:

1. Reads in the file you specify
2. Reads in all the dependencies that file specifies, and all the dependencies of those files, etc.
3. Begins executing the sunchronous tasks in this files.
4. Begins processing the "todo list" by repeating the event loop until it has nothing to do.

REPL it's a way to execute the Javascript code against the V8. When we invoke the comand node at the terminal, the REPL is execute autoaticaly.

REAL start the event loop on the background.

The REPL is a interactive JS runtime. You can write any javascript you want, and have it executed.

# Anatomy of a Node Application

### Option 1

Start you app with

NODE_ENV=myEnvironmentName node index.js

Put your configurations in a file, (ex config.js) which has a switch(process.env.NODE_ENV) to determine the corrente environment, and export only the config variables for that environment.

### Option 2

Start yout app with every configuration variable you're going to need for that environment:

DBpassword=myDBpassword apiToken=myScretToken port=thePortIShouldRunOn foo=bar node index.js

### Option 3

Read all yout configuration from a .env file which gets ignored by source control.

Each dev would put their .env file in the project prior to beginning locahost work

Your deployment pipeline would inset an .env file into the repo before it deploys anewhere

