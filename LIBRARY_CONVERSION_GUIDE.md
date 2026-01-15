# How to Convert a Normal Python Module into an Installable Library

This guide explains the mandatory steps to convert a standard Python module into a proper, installable library that can be shared and reused across projects.

Think of it like preparing a product for shipping. You can't just put the item in a box; you need the right packaging, a shipping label, and instructions.

---

### Step 1: A Standard Project Structure

You need to organize your files in a specific way so that packaging tools know where to find your code. The modern, standard way is the "src" layout.

#### What to do:

Your project should be structured like this:

```
my_project/
├── src/
│   └── your_module/
│       ├── __init__.py
│       └── your_code.py
├── setup.py
└── ... (README.md, LICENSE, etc.)
```

#### The 'Why':

*   **Clarity and Disambiguation:** This structure creates a clean separation between your actual source code (`src`) and other project files like tests, documentation, and examples.
*   **Prevents Import Errors:** It solves a common, tricky problem where your code might accidentally import local files instead of the installed library, leading to "it works on my machine" issues. With the `src` layout, this is impossible. The only way to use the library is to install it first, which guarantees you are testing the *installed* version.

---

### Step 2: The "Recipe" File (`setup.py`)

This file is the most important part. It's the "shipping label" and "assembly instructions" for your library. It tells `pip` and other tools everything they need to know about your project.

#### What to do:

Create a `setup.py` file in the root of your project with the following essential parameters:

```python
from setuptools import setup, find_packages

setup(
    # The name pip will use (e.g., 'pip install my-library')
    name="my-cool-library",

    # The version of your library. Crucial for updates.
    version="0.1.0",

    # Tells setuptools to automatically find all Python packages in the 'src' directory.
    packages=find_packages(where="src"),

    # Specifies that the packages are located in the 'src' directory.
    package_dir={"": "src"},

    # (Optional but vital) Lists other libraries your code depends on.
    # install_requires=["requests", "numpy"],
)
```

#### The 'Why':

*   `name` and `version`: These are the primary identifiers. Without them, `pip` wouldn't know what it's installing or be able to handle updates.
*   `packages` and `package_dir`: This is how you tell the packaging tools **what code to include in the final package**. `find_packages(where="src")` is a powerful helper that automatically discovers your module so you don't have to list it manually. This prevents you from forgetting to include parts of your library.

---

### Step 3: The Build Process

You need to run a command that takes your source code and the `setup.py` "recipe" and generates the actual distributable package files.

#### What to do:

From your project's root directory, you would typically run a command to build the package (though for direct GitHub installs, this is done automatically). The standard is to create a "wheel," which is the modern format for Python distributions.

For local testing and distribution, you would run: `python setup.py bdist_wheel`

This command creates a `dist/` folder containing a `.whl` (wheel) file.

#### The 'Why':

*   **Standardization:** The wheel file (`.whl`) is a standardized ZIP format. `pip` knows exactly how to handle it, making installations fast and reliable across different operating systems. It's a "pre-compiled" package, so the user's machine doesn't have to do much work.

---

### Summary: The Absolute Minimum

| Step                   | What it is                                 | Why it's Mandatory                                                                                             |
| ---------------------- | ------------------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| **Project Structure**  | Organizing your files into a `src` layout. | To ensure packaging tools can find your code and to prevent ambiguous import errors.                           |
| **`setup.py` file**    | The central configuration "recipe."        | To define your library's name, version, and contents for `pip` and other tools. It's the brain of the package. |
| **Build Process**      | Creating a distributable file (a wheel).   | To create the actual standardized artifact that `pip` installs. It's the final "shippable product."               |

**Note:** While not strictly mandatory to make a package *installable*, no one would ever use a library without a **`README.md`** (the instruction manual) and a **`LICENSE`** (the legal terms of use). They are practically mandatory for any real-world project.
