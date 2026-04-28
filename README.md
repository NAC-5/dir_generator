# Directory Generator

A command-line tool that automates project folder structure creation.

## Usage
python dir_generator.py

## What it does
- Creates a root directory with the name you provide
- Creates any subdirectories you specify
- Automatically creates `source` and `test` directories if not included
- Replaces spaces in directory names with underscores
- Skips creation safely if directories already exist

## Example
Enter root name: my_project
Enter subdirectories: docs, assets

Creates:
my_project/
├── source/
├── test/
├── docs/
└── assets/
