# Geometry Dash RNG Analysis

This repository contains a Python script developed to analyze the RNG in the Geometry Dash level "Chompstep".

The goal was to calculate the theoretical maximum completion percentage for a level that relies heavily on randomness, by reverse-engineering the game's LCG algorithm.

### Results
*   **Discovery:** Proved that the theoretical maximum for the level is **100%** if we use an old copy of the level. The findings were published on Reddit.
    *   [🔗 Link to Reddit Thread 1](https://www.reddit.com/r/geometrydash/comments/1owrrzh/chompsteps_theoretical_maximum_is_95_i_checked/)
    *   [🔗 Link to Reddit Thread 2](https://www.reddit.com/r/geometrydash/comments/1oxtj1u/chompstep_100_is_possible_i_checked_every/)

### Details

The script simulates the internal RNG of the game to predict safe paths through obstacles.

*   **Algorithm:** Implements the standard LCG formula used by the game engine:
    ```python
    State = (State * 214013 + 2531011) & 0xFFFFFFFF
    ```
*   **Logic:** It iterates through possible seeds to find a sequence of random numbers that aligns with the level's obstacle pattern

### Usage

```bash
python main_updated.py
