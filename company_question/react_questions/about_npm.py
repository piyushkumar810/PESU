'''📦 NPM — Complete Questions & Answers
# 1. What is npm?

Answer:
npm stands for Node Package Manager. It is the default package manager for Node.js.

It is used to:

Install packages
Remove packages
Update packages
Manage dependencies
Run project scripts
Publish packages

Example:
npm install express


# 2. What is the difference between Node.js and npm?

Answer:

Node.js	npm
Runtime environment	Package manager
Runs JavaScript outside the browser	Manages packages
Executes .js files	Installs libraries
Provides Node APIs	Manages dependencies

Simple:
Node.js → Runs JavaScript
npm     → Manages packages

# 3. What is package.json?

Answer:
package.json is the configuration/description file of a Node.js project.

It contains information such as:

Project name
Version
Scripts
Dependencies
Dev dependencies
Project metadata

Example:

{
  "name": "my-project",
  "version": "1.0.0",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^5.1.0"
  }
}
Easy memory:

package.json = What my project needs

# 4. What is package-lock.json?

Answer:
package-lock.json records the exact versions of installed packages and their dependency tree.

It helps ensure that the same versions are installed across different machines.

Easy memory:

package-lock.json = Exactly what was installed

# 5. Difference between package.json and package-lock.json
package.json	package-lock.json
Describes project requirements	Records exact installed versions
Can be edited manually	Usually managed automatically by npm
Contains dependency ranges	Contains exact dependency information
Contains scripts	Does not define project scripts
Human-friendly	More detailed/lock information
Memory:
package.json
     ↓
"What do I need?"

package-lock.json
     ↓
"What exactly did npm install?"


# 6. What is node_modules?

Answer:
node_modules is the folder where npm stores the actual packages/libraries installed in your project.

Example:

project/
│
├── node_modules/
│   ├── express/
│   ├── dotenv/
│   └── ...
│
├── package.json
└── package-lock.json

# 7. What is inside node_modules?

Answer:
It contains:

Installed packages
Package source code
Package dependencies
Package configuration files
Nested dependencies

For example:

node_modules/
└── express/
    ├── lib/
    ├── index.js
    ├── package.json
    └── ...

# 8. Why does node_modules contain so many folders?

Answer:
Because packages themselves can depend on other packages.

For example:

Your Project
     ↓
   Express
     ↓
 ┌───┼────┐
 ↓   ↓    ↓
 A   B    C
     ↓
     D

npm installs the complete dependency tree.

# 9. What is a dependency?

Answer:
A dependency is a package/library that your application needs to perform some functionality.

Example:

"dependencies": {
  "express": "^5.1.0"
}

Here, express is a dependency.

# 10. What is a dependency tree?

Answer:
A dependency tree shows how packages depend on other packages.

Example:

My Project
    │
    └── Express
          │
          ├── Package A
          ├── Package B
          └── Package C

npm installs all required packages in this tree.

📥 INSTALLATION COMMANDS

# 11. What does npm install do?

Answer:
npm install reads your package.json and package-lock.json and installs the required packages into node_modules.

npm install

Commonly used after cloning a project.

# 12. What does npm install express do?

Answer:

npm install express

It:

Downloads Express
Downloads its dependencies
Places them in node_modules
Adds Express to package.json
Updates package-lock.json

# 13. What does npm install package-name mean?

Answer:
It installs the specified package into the current project.

Example:
npm install mongoose

# 14. What is npm i?

Answer:
npm i is a short form of:

npm install

For example:
npm i express

is equivalent to:

npm install express
🗑️ REMOVE / UPDATE

# 15. What does npm uninstall express do?

Answer:
It removes Express from the project.

npm uninstall express

It removes the package from:

node_modules

and updates:

package.json
package-lock.json

# 16. What does npm update do?

Answer:
npm update updates installed packages according to the version ranges allowed by your package.json.

npm update

# 17. What does npm outdated do?

Answer:
npm outdated checks which installed packages have newer versions available.

npm outdated

Example:

Package    Current    Wanted    Latest
express    5.0.0      5.1.0     5.1.0
mongoose   8.5.0      8.5.2     9.0.0

# 18. What does Current, Wanted and Latest mean?

Answer:

Current:- The version currently installed.

Wanted:- The newest version allowed by your package.json version range.

Latest:- The newest version published by the package author.

Example:

Current = 5.0.0
Wanted  = 5.1.0
Latest  = 6.0.0

This means your project can update to 5.1.0 under its current version range, but 6.0.0 requires changing the allowed range.

# 19. Difference between npm outdated and npm update

Answer:

npm outdated
      ↓
CHECK
      ↓
Shows outdated packages
npm update
      ↓
UPDATE
      ↓
Updates packages within allowed ranges

Important: npm outdated does not update anything.

🛠️ PROJECT CREATION

# 20. What does npm init do?

Answer:
It creates a package.json file for your Node.js project.

npm init

npm asks questions such as:

Package name
Version
Description
Entry point
Author
License

# 21. What does npm init -y do?

Answer:
It creates package.json using default values without asking the questions.

npm init -y
📦 DEPENDENCIES

# 22. What are dependencies?

Answer:
dependencies contain packages required by the application to run.

Example:

"dependencies": {
  "express": "^5.1.0",
  "mongoose": "^8.0.0"
}

# 23. What are devDependencies?

Answer:
devDependencies contain packages mainly needed during development.

Example:

"devDependencies": {
  "typescript": "^5.0.0",
  "nodemon": "^3.0.0"
}

# 24. Difference between dependencies and devDependencies

Answer:

dependencies	devDependencies
Needed by application	Mainly needed during development
Used when application runs	Used for development/build/testing tools
Example: Express	Example: TypeScript
Example: Mongoose	Example: Nodemon

Memory:

dependencies
    ↓
RUN application

devDependencies
    ↓
DEVELOP application

# 25. How do you install a development dependency?

Answer:

npm install typescript --save-dev

Short form:

npm i typescript -D
🌍 GLOBAL VS LOCAL

# 26. What does npm install -g mean?

Answer:
-g means global installation.

Example:

npm install -g nodemon

The package is installed globally so it can be used across projects, subject to your environment/PATH.

# 27. Difference between local and global installation

Answer:

Local
  ↓
Installed for one project
  ↓
node_modules/
Global
  ↓
Installed for the system/user environment
  ↓
Can be used across projects

For project dependencies, local installation is generally preferred.

📋 CHECKING PACKAGES

# 28. What does npm list do?

Answer:
It displays installed packages and their dependency tree.

npm list

# 29. What does npm list --depth=0 do?

Answer:
It displays mainly the packages directly installed by your project, without showing their deeper dependencies.

npm list --depth=0

Example:

my-project
├── express
├── mongoose
└── dotenv
▶️ NPM SCRIPTS

# 30. What are npm scripts?

Answer:
npm scripts are commands defined inside the scripts section of package.json.

Example:

"scripts": {
  "start": "node server.js",
  "dev": "nodemon server.js"
}

# 31. What does npm start do?

Answer:
It runs the start script from package.json.

npm start

which executes:

node server.js

# 32. What does npm run dev do?

Answer:
It runs the dev script.

If:

"scripts": {
  "dev": "nodemon server.js"
}

then:

npm run dev

runs:

nodemon server.js

# 33. Difference between npm start and npm run dev

Answer:

npm start
    ↓
Runs "start" script
npm run dev
    ↓
Runs "dev" script

The actual command depends on what is written in package.json.

# -------------------------------------------------------------------------------
🧠 IMPORTANT SCENARIO QUESTIONS
# 34. You cloned a Node.js project from GitHub, but there is no node_modules. What should you do?

Answer:

Run:

npm install

npm reads the dependency information and recreates node_modules.

# 35. You accidentally deleted node_modules. Is your project destroyed?

Answer:
No.

Your source code and dependency information are normally still present.

Run:

npm install

and npm will recreate node_modules.

# 36. Why don't we normally upload node_modules to GitHub?

Answer:
Because node_modules can be extremely large and contains packages that can be recreated from package.json and the lockfile.

Usually we add:

node_modules/

to .gitignore.

Then another developer can simply run:

npm install

# 37. Why should package-lock.json usually be uploaded to GitHub?

Answer:
Because it records exact dependency versions and helps developers/CI environments install a consistent dependency tree.

# 38. What happens when you run npm install express?

Answer:

npm install express
        ↓
Find Express
        ↓
Download Express
        ↓
Download its dependencies
        ↓
Store packages in node_modules
        ↓
Update package.json
        ↓
Update package-lock.json

# 39. What happens when you run npm uninstall express?

Answer:

npm uninstall express
        ↓
Remove Express
        ↓
Update package.json
        ↓
Update package-lock.json
        ↓
Remove it from node_modules

# 40. What happens when you run npm outdated?

Answer:

npm outdated
      ↓
Check installed versions
      ↓
Compare with available versions
      ↓
Show outdated packages

It does not automatically update them.
'''


# 
'''
|                        | `package.json`                                   | `package-lock.json`                          |
| ---------------------- | ------------------------------------------------ | -------------------------------------------- |
| **Purpose**            | Describes your project and its dependencies      | Locks the **exact versions** of dependencies |
| **Created by**         | Usually created manually / `npm init`            | Automatically created/updated by npm         |
| **Contains**           | Project info, scripts, dependency version ranges | Exact dependency tree and versions           |
| **Can edit manually?** | ✅ Yes                                            | ⚠️ Usually don't edit manually               |
| **Important for**      | Telling npm **what you want**                    | Telling npm **exactly what was installed**   |
| **Commit to GitHub?**  | ✅ Yes                                            | ✅ Yes                                        |

'''