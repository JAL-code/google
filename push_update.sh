#!/bin/bash

git status > current_update.txt

./process_current_update.py current_update.txt

